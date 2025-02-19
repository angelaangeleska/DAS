from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from data_ingestion_service.fetchers.fetch_stock_data import stock_fetcher
from data_ingestion_service.fetchers.fetch_stock_news import news_fetcher

# Create your views here.
class StockDataView(APIView):
    def get(self, request):
        stock_data = stock_fetcher(request.GET.get('code'))
        return Response(stock_data)

class StockNewsView(APIView):
    def get(self, request):
        stock_news = news_fetcher(request.GET.get('code'))
        return Response(stock_news)