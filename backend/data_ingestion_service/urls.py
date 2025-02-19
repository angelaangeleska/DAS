from django.urls import path
from .views import StockDataView, StockNewsView

urlpatterns = [
    path('api/stocks/', StockDataView.as_view(), name='stock-data'),
    path('api/news/', StockNewsView.as_view(), name='stock-news'),
]