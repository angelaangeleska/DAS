from tokenize import String

import ta
import numpy as np


def calc_technical_indicators(df):
    df["SMA_10"] = df["close_price"].rolling(window=10).mean()  # Simple Moving Average
    df["EMA_10"] = df["close_price"].ewm(span=10, adjust=False).mean()  # Exponential Moving Average

    df["WMA_10"] = df["close_price"].rolling(window=10).apply(lambda x: np.average(x, weights=range(1, 11)))  # Weighted MA

    # MACD (12-day EMA - 26-day EMA)
    df["MACD"] = df["close_price"].ewm(span=12, adjust=False).mean() - df["close_price"].ewm(span=26, adjust=False).mean()

    # Bollinger Bands
    df["BB_High"] = df["close_price"].rolling(window=20).mean() + 2 * df["close_price"].rolling(window=20).std()
    df["BB_Low"] = df["close_price"].rolling(window=20).mean() - 2 * df["close_price"].rolling(window=20).std()

    # RSI (Relative Strength Index)
    df["RSI"] = ta.momentum.RSIIndicator(df["close_price"], window=14).rsi()

    # Stochastic Oscillator
    stoch = ta.momentum.StochasticOscillator(df["high_price"], df["low_price"], df["close_price"], window=14)
    df["Stochastic"] = stoch.stoch()

    # CCI (Commodity Channel Index)
    df["CCI"] = ta.trend.CCIIndicator(df["high_price"], df["low_price"], df["close_price"], window=14).cci()

    # ADX (Average Directional Index)
    df["ADX"] = ta.trend.ADXIndicator(df["high_price"], df["low_price"], df["close_price"], window=14).adx()

    # Williams %R
    df["WilliamsR"] = ta.momentum.WilliamsRIndicator(df["high_price"], df["low_price"], df["close_price"], lbp=14).williams_r()

    return df


# use this func
def analyze_report(df):
    df = calc_technical_indicators(df)

    df["Signal"] = df.apply(generate_signal, axis=1)

    return df, str(df['Signal'][-1:].iloc[0])


def generate_signal(row):
    if row["RSI"] < 30 and row["Stochastic"] < 20 and row["WilliamsR"] < -80:
        return "Buy"
    elif row["RSI"] > 70 and row["Stochastic"] > 80 and row["WilliamsR"] > -20:
        return "Sell"
    else:
        return "Hold"

