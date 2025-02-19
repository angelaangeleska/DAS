import requests
import pandas as pd
import yfinance as yf


def news_fetcher(code):
    print(f"Fetching news for {code}...")

    df = pd.DataFrame()
    try:
        news_data_yf = get_yf_company_news(code)
        news_data_marketaux = get_marketaux_company_news(code)
        df = pd.concat([news_data_yf, news_data_marketaux], ignore_index=True)

    except Exception as e:
        print(f"Failed to fetch news for {code}: {e}")

    return df.to_json()


def get_yf_company_news(stock_code):
    stock = yf.Ticker(stock_code)
    news = stock.news
    data = []
    for new in news:
        tmp = {
            'title': new['content']['title'],
            'summary': new['content']['summary']
        }
        data.append(tmp)

    return pd.DataFrame(data)


def get_marketaux_company_news(code):
    BASE_URL = f"https://api.marketaux.com/v1/news/all?symbols=AAPL&filter_entities=true&language=en"
    API_KEY = "4HP7j7IdLGl3uDHrgFajWEBPRT5XekcjmjX36mpX"

    params = {
        'symbols': code,
        'filter_entities': 'true',
        'language': 'en',
        'api_token': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    company_data = []
    for row in data['data']:
        tmp = {
            'title': row['title'],
            'summary': row['description']
        }
        company_data.append(tmp)

    return pd.DataFrame(company_data)
