import pandas as pd

def fetch_company_codes():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    tables = pd.read_html(url)
    stock_table = tables[0]

    data = stock_table["Symbol"].tolist()
    return data