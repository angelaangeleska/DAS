import requests
import pandas as pd
import yfinance as yf

from .fetch_codes import *
from kafka import KafkaProducer
from django.db import connection
from .serializers import serializer
from datetime import datetime, timedelta, date

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=serializer,
)


def send_stock_data(code):
    # TODO change host
    url = f"http://localhost:8000/api/stocks/?code={code}"
    response = requests.get(url)
    data = response.json()

    message = {"code": code, "data": data}

    producer.send('stock-data', message)
    producer.flush()


def send_stock_news(code):
    # TODO change host
    url = f"http://localhost:8000/api/news/?code={code}"
    response = requests.get(url)
    news = response.json()

    message = {"code": code, "news": news}

    producer.send('stock-data', message)
    producer.flush()


def update_stock_data(code):
    stock_table = f"{code}_stocks"

    with connection.cursor() as cursor:
        last_date = f"SELECT MAX(date) FROM {stock_table}"
        cursor.execute(last_date)

        columns = [col[0] for col in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        last_day = result[0]['max']
        if last_day == date.today():
            return "Already updated"

        data = stock_fetcher(code, last_day)

        message = {"code": code, "data": data}

        producer.send('stock-data', message)
        producer.flush()

    return "Updated successfully"

def stock_fetcher(code, last_date):
    print(f"Updating data for {code}...")
    stock_data = pd.DataFrame()
    try:
        stock_data = scrape_stock_info(code, last_date)

        stock_data = stock_data.reset_index()
        stock_data['Date'] = stock_data['Date'].astype(str)
        stock_data.set_index('Date', inplace=True)

    except Exception as e:
        print(f"Failed to fetch or save data for {code}: {e}")

    return stock_data.to_json()  # CONVERT THE DATAFRAME TO JSON


def scrape_stock_info(stock_code, last_date):
    """Fetches historical stock data using yfinance."""
    end_date = datetime.today()
    start_date = last_date + timedelta(days=1)

    stock = yf.Ticker(stock_code)
    updated_data = stock.history(start=start_date, end=end_date)

    return updated_data

def main():
    codes = fetch_company_codes()
    # TODO remove [:30]
    codes = codes[:30]

    for code in codes:
        send_stock_data(code)

    producer.send('stock-data', 'Change to news')

    for code in codes:
        send_stock_news(code)

    producer.send('stock-data', 'No more data')


if __name__ == '__main__':
    main()

