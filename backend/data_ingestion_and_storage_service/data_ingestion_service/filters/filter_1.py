import pandas as pd

from data_ingestion_and_storage_service.data_ingestion_service.filters.filter import Filter

class StocksCodes(Filter):

    def task(self, data):
        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

        tables = pd.read_html(url)
        stock_table = tables[0]

        data = stock_table["Symbol"].tolist()
        return data