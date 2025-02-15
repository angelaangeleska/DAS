from data_ingestion_service.fetchers.filters.filter_1 import StocksCodes
from data_ingestion_service.fetchers.filters.filter_2 import FetchAndSaveStocksData
from data_ingestion_service.fetchers.filters.filter_3 import FetchNewsData


class StockPipeline:
    def __init__(self):
        self.filters = []
        self.filters.append(StocksCodes())
        self.filters.append(FetchAndSaveStocksData())
        self.filters.append(FetchNewsData())

    def execute(self, data):
        for filter in self.filters:
            data = filter.task(data)
        return data

def run_pipeline():
    print("Pipeline starting...")

    pipeline = StockPipeline()
    data = pipeline.execute([])

    print("Pipeline finished!!!")