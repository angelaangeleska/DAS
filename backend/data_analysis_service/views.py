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


def get_company_stocks(request):
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

    print(response_data)

    return JsonResponse(response_data, safe=False)

