from django.db import models

# Create your models here.
class CompanyStockData(models.Model):
    date = models.DateField()
    open_price = models.FloatField()
    close_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    volume = models.IntegerField()
    dividend = models.FloatField()
    stock_splits = models.FloatField()

    def __str__(self):
        return self.date + " " + self.open_price

    class Meta:
        abstract = True


def create_stock_model(table_name):
    """Factory function to create a dynamic stock model."""
    class DynamicCompanyStock(CompanyStockData):
        class Meta:
            db_table = table_name

        @classmethod
        def kafka_schema(cls):
            return {
                'type': 'object',
                'properties': {
                    'date': {'type': 'string', 'format': 'date'},
                    'open_price': {'type': 'number'},
                    'close_price': {'type': 'number'},
                    'high_price': {'type': 'number'},
                    'low_price': {'type': 'number'},
                    'volume': {'type': 'integer'},
                    'dividend': {'type': 'number'},
                    'stock_splits': {'type': 'number'},
                }
            }

    return DynamicCompanyStock

class CompanyNewsData(models.Model):
    title = models.TextField()
    summary = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

def create_news_model(table_name):
    """Factory function to create a dynamic stock model."""
    class DynamicCompanyNews(CompanyNewsData):
        class Meta:
            db_table = table_name
    return DynamicCompanyNews

