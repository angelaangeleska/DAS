from data_ingestion_service.fetchers.filters.filter import Filter

import requests
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
from django.db import connection


class FetchAndSaveStocksData(Filter):
    def task(self, data):
        # TODO prvite 5 se skrejpnati [:5]
        for code in data[:0]:
            print(f"Fetching data for {code}...")
            try:
                stock_data = self.scrape_stock_info(code)

                self.create_table_for_stock_code(code)

                self.insert_data_into_table(code, stock_data)

                print(f"Data for {code} saved to the database table '{code}_stocks'")
            except Exception as e:
                print(f"Failed to fetch or save data for {code}: {e}")
        return data

    def create_table_for_stock_code(self, code):
        """Creates a table for the given stock code if it doesn't already exist."""
        table_name = f"{code}_stocks"
        with connection.cursor() as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    date DATE,
                    open_price FLOAT,
                    high_price FLOAT,
                    low_price FLOAT,
                    close_price FLOAT,
                    volume INTEGER,
                    dividend FLOAT,
                    stock_splits FLOAT
                );
            """)
        print(f"Table '{table_name}' created (if not already existing).")

    def insert_data_into_table(self, code, stock_data):
        """Inserts stock data into the corresponding table."""
        table_name = f"{code}_stocks"

        records = [
            (
                row.name.date(),
                float(row['Open']),
                float(row['High']),
                float(row['Low']),
                float(row['Close']),
                int(row['Volume']),
                float(row.get('Dividends', 0.0)),
                float(row.get('Stock Splits', 0.0))
            )
            for _, row in stock_data.iterrows()
        ]

        with connection.cursor() as cursor:
            cursor.executemany(
                f"""
                INSERT INTO {table_name} (date, open_price, high_price, low_price, close_price, volume, dividend, stock_splits)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """,
                records
            )
        print(f"Inserted {len(records)} rows into '{table_name}'.")

    def scrape_stock_info(self, stock_code):
        """Fetches historical stock data using yfinance."""
        end_date = datetime.today()
        start_date = end_date - timedelta(days=365 * 10)

        stock = yf.Ticker(stock_code)
        historical_data = stock.history(start=start_date, end=end_date)

        return historical_data

    # def get_alpha_vantage_stocks(self, code):
    #     API_KEY = '7LT5400PT9D4CVHZ'
    #     BASE_URL = 'https://www.alphavantage.co/query'
    #
    #     params = {
    #         'function': 'TIME_SERIES_INTRADAY',
    #         'symbol': code,
    #         'interval': '30min',
    #         'apikey': API_KEY
    #     }
    #     response = requests.get(BASE_URL, params=params)
    #     data = response.json()
    #     return data
