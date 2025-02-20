import requests

from fetch_codes import *
from kafka import KafkaProducer
from serializers import serializer

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

    producer.send('stock-news', message)
    producer.flush()


def main():
    codes = fetch_company_codes()
    # TODO remove [:3]
    for code in codes[:3]:
        send_stock_data(code)

    producer.send('stock-data', 'Change to news')

    for code in codes[:3]:
        send_stock_news(code)

    producer.send('stock-data', 'No more data')

if __name__ == '__main__':
    main()