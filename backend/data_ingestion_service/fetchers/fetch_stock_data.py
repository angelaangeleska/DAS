import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd


def stock_fetcher(code):
    print(f"Fetching data for {code}...")
    stock_data = pd.DataFrame()
    try:
        stock_data = scrape_stock_info(code)

        stock_data = stock_data.reset_index()
        stock_data['Date'] = stock_data['Date'].astype(str)
        stock_data.set_index('Date', inplace=True)

    except Exception as e:
        print(f"Failed to fetch or save data for {code}: {e}")

    return stock_data.to_json()  # CONVERT THE DATAFRAME TO JSON


def scrape_stock_info(stock_code):
    """Fetches historical stock data using yfinance."""
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * 10)

    stock = yf.Ticker(stock_code)
    historical_data = stock.history(start=start_date, end=end_date)

    return historical_data