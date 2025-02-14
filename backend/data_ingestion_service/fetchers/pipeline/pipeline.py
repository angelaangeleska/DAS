from data_ingestion_service.fetchers.filters.filter_1 import StocksCodes
from data_ingestion_service.fetchers.filters.filter_2 import FetchAndSaveStocksData


class StockPipeline:
    def __init__(self):
        self.filters = []
        self.filters.append(StocksCodes())
        self.filters.append(FetchAndSaveStocksData())

    def execute(self, data):
        for filter in self.filters:
            data = filter.task(data)
        return data

def run_pipeline():
    print("Pipeline starting...")

    pipeline = StockPipeline()
    data = pipeline.execute([])

    print("Pipeline finished!!!")