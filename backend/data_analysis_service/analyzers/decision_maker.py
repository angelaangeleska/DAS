import pandas as pd

from .report_analyzer import analyze_report
from .sentiment_analyzer import news_analyzer
from  .signal_prediction import predict_signal

def decision_maker(df_stocks, df_news):
    df_stocks = pd.DataFrame(df_stocks)
    df_news = pd.DataFrame(df_news)

    # print( 'OVDE',df[:-1])

    report_df, last_report_signal = analyze_report(df_stocks.copy())

    news_signal = news_analyzer(df_news.copy())

    prediction_signal = predict_signal(df_stocks.copy())

    return report_df, last_report_signal, news_signal, prediction_signal