import requests
import pandas as pd
import yfinance as yf

from data_ingestion_and_storage_service.data_ingestion_service.filters.filter import Filter
from data_ingestion_and_storage_service.data_storage_service.utils import create_table_for_stock_news, insert_data_into_news_table

class FetchNewsData(Filter):
    def task(self, data):
        # TODO change zagradi [:5]
        for code in data[:1]:
            print(f"Fetching news for {code}...")
            try:
                news_data_yf = self.get_yf_company_news(code)
                news_data_marketaux = self.get_marketaux_company_news(code)
                df = pd.concat([news_data_yf, news_data_marketaux], ignore_index=True)

                create_table_for_stock_news(code)

                insert_data_into_news_table(code, df)
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
