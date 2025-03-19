from django.shortcuts import render
from .stock_producer import update_stock_data
from data_storage_service.stock_data_consumer import process_stock_data

def update_company_table(request):
    update_stock_data(request.GET.get('code'))
    process_stock_data()


