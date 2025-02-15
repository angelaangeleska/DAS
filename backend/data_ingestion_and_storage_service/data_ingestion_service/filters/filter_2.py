import yfinance as yf
from datetime import datetime, timedelta

from data_ingestion_and_storage_service.data_ingestion_service.filters.filter import Filter
from data_ingestion_and_storage_service.data_storage_service.utils import create_table_for_stock_code, insert_data_into_table

class FetchAndSaveStocksData(Filter):
    def task(self, data):
        # TODO prvite 5 se skrejpnati [:5]
        for code in data[:1]:
            print(f"Fetching data for {code}...")
            try:
                stock_data = self.scrape_stock_info(code)

                create_table_for_stock_code(code)

                insert_data_into_table(code, stock_data)

                print(f"Data for {code} saved to the database table '{code}_stocks'")
            except Exception as e:
                print(f"Failed to fetch or save data for {code}: {e}")
        return data

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
