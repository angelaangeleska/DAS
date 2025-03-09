import pandas as pd

from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from .analyzers.decision_maker import decision_maker


# Create your views here.
def make_decision(signals):
    signals_series = pd.Series(signals)
    return signals_series.mode()[0]


def get_company_predictions(request):
    company_code = request.GET.get('code')
    stock_table = f"{company_code}_stocks"
    news_table = f"{company_code}_news"

    with connection.cursor() as cursor:
        query_stocks = f"SELECT * FROM {stock_table}"
        query_news = f"SELECT * FROM {news_table}"

        cursor.execute(query_stocks)
        columns = [col[0] for col in cursor.description]
        results_stocks = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.execute(query_news)
        columns = [col[0] for col in cursor.description]
        results_news = [dict(zip(columns, row)) for row in cursor.fetchall()]

        report_df, last_report_signal, news_signal, prediction_signal = decision_maker(results_stocks, results_news)

    final_decision = make_decision([last_report_signal, news_signal, prediction_signal])

    response_data = {
        "final_decision": final_decision,
        "news_signal": news_signal,
        "last_report_signal": last_report_signal,
        "prediction_signal": prediction_signal,
    }

    return JsonResponse(response_data, safe=False)


def transform_stock_data(data):
    return [{"date": item["date"], "price": item["close_price"]} for item in data]


def get_company_table(request):
    company_code = request.GET.get('code')
    stock_table = f"{company_code}_stocks"

    with connection.cursor() as cursor:
        query_stocks = f"SELECT * FROM {stock_table}"

        cursor.execute(query_stocks)
        columns = [col[0] for col in cursor.description]
        results_stocks = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(transform_stock_data(results_stocks), safe=False)


def get_company_info(request):
    company_code = request.GET.get('code')
    stock_table = f"{company_code}_stocks"
    news_table = f"{company_code}_news"

    with connection.cursor() as cursor:
        query_stocks = f"SELECT * FROM {stock_table}"
        query_news = f"SELECT * FROM {news_table}"

        cursor.execute(query_stocks)
        columns = [col[0] for col in cursor.description]
        results_stocks = [dict(zip(columns, row)) for row in cursor.fetchall()]

        cursor.execute(query_news)
        columns = [col[0] for col in cursor.description]
        results_news = [dict(zip(columns, row)) for row in cursor.fetchall()]

        report_df, last_report_signal, news_signal, prediction_signal = decision_maker(results_stocks, results_news)

    final_decision = make_decision([last_report_signal, news_signal, prediction_signal])

    response_data = {
        "final_decision": final_decision,
        "news_signal": news_signal,
        "last_report_signal": last_report_signal,
        "prediction_signal": prediction_signal,
    }

    return JsonResponse(response_data, safe=False)


def get_company_news(request):
    company_code = request.GET.get('code')
    news_table = f"{company_code}_news"
    print(news_table)
    with connection.cursor() as cursor:
        query_news = f"SELECT * FROM {news_table}"

        cursor.execute(query_news)
        columns = [col[0] for col in cursor.description]
        results_news = [dict(zip(columns, row)) for row in cursor.fetchall()]

    return JsonResponse(results_news, safe=False)


def get_codes(request):
    return JsonResponse(fetch_company_codes(), safe=False)

def fetch_company_codes():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    tables = pd.read_html(url)
    stock_table = tables[0]

    data = stock_table["Symbol"].tolist()
    return data