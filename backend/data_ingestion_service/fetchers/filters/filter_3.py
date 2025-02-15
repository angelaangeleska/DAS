import requests
import pandas as pd
import yfinance as yf
from django.db import connection
from data_ingestion_service.fetchers.filters.filter import Filter

class FetchNewsData(Filter):
    def task(self, data):
        # TODO change zagradi [:5]
        for code in data[:5]:
            print(f"Fetching news for {code}...")
            try:
                news_data_yf = self.get_yf_company_news(code)
                news_data_marketaux = self.get_marketaux_company_news(code)
                df = pd.concat([news_data_yf, news_data_marketaux], ignore_index=True)

                self.create_table_for_stock_code(code)

                self.insert_data_into_table(code, df)
            except Exception as e:
                print(f"Failed to fetch news for {code}: {e}")

        return data

    def get_yf_company_news(self, stock_code):
        stock = yf.Ticker(stock_code)
        news = stock.news
        data = []
        for new in news:
            tmp = {
                'title': new['content']['title'],
                'summary': new['content']['summary']
            }
            data.append(tmp)

        return pd.DataFrame(data)

    def create_table_for_stock_code(self, code):
        """Creates a table for the given stock code if it doesn't already exist."""
        table_name = f"{code}_news"
        with connection.cursor() as cursor:
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    summary TEXT
                );
            """)
        print(f"Table '{table_name}' created (if not already existing).")

    def insert_data_into_table(self, code, news_data):
        """Inserts stock data into the corresponding table."""
        table_name = f"{code}_news"

        records = [
            (
                row.title,
                row.summary
            )
            for _, row in news_data.iterrows()
        ]

        with connection.cursor() as cursor:
            cursor.executemany(
                f"""
                INSERT INTO {table_name} (title, summary)
                VALUES (%s, %s);
                """,
                records
            )
        print(f"Inserted {len(records)} rows into '{table_name}'.")

    def get_marketaux_company_news(self, code):
        BASE_URL = f"https://api.marketaux.com/v1/news/all?symbols=AAPL&filter_entities=true&language=en"
        API_KEY = "4HP7j7IdLGl3uDHrgFajWEBPRT5XekcjmjX36mpX"

        params = {
            'symbols': code,
            'filter_entities': 'true',
            'language': 'en',
            'api_token': API_KEY
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        company_data = []
        for row in data['data']:
            tmp = {
                'title': row['title'],
                'summary': row['description']
            }
            company_data.append(tmp)

        return pd.DataFrame(company_data)
