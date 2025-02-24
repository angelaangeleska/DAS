import joblib
import pandas as pd

def transform_dataframe(df):
    features = ["open_price", "close_price", "volume"]

    df = df.drop(columns=['dividend', 'stock_splits'])
    df = df[len(df) - 7:]

    b = pd.DataFrame({'open_price': [0.0], "close_price": [0.0], 'high_price': [0.0], 'low_price': [0.0], 'volume': [0]})
    df = pd.concat([df, b], axis=0)

    lags = range(7, 0, -1)
    list(lags)
    for lag in lags:
        for column in features:
            df[f"{column}_{lag}"] = df[column].shift(lag)

    df.set_index('date', inplace=True)
    df = df.drop(columns=['open_price', "high_price", "close_price", "volume", 'low_price'])

    column_mapping = {
        "open_price_7": "Open_7",
        "close_price_7": "Close_7",
        "volume_7": "Volume_7",
        "open_price_6": "Open_6",
        "close_price_6": "Close_6",
        "volume_6": "Volume_6",
        "open_price_5": "Open_5",
        "close_price_5": "Close_5",
        "volume_5": "Volume_5",
        "open_price_4": "Open_4",
        "close_price_4": "Close_4",
        "volume_4": "Volume_4",
        "open_price_3": "Open_3",
        "close_price_3": "Close_3",
        "volume_3": "Volume_3",
        "open_price_2": "Open_2",
        "close_price_2": "Close_2",
        "volume_2": "Volume_2",
        "open_price_1": "Open_1",
        "close_price_1": "Close_1",
        "volume_1": "Volume_1"
    }

    df.rename(columns=column_mapping, inplace=True)
    df.drop(columns=["id"], inplace=True)

    return df

# call this func
def predict_signal(df):
    last_day = df["close_price"][-1:]
    last_day = float(last_day.iloc[0])
    df = transform_dataframe(df)
    model = joblib.load('./data_analysis_service/analyzers/stock_prediction_model.pkl')

    prediction = model.predict(df[-1:])
    prediction = float(prediction[0])

    threshold = last_day*0.005 # 0.5% from the last day
    if prediction > last_day:
        return 'Buy'
    elif -threshold < prediction - last_day < threshold:
        return 'Hold'
    else:
        return 'Sell'


def load_model(filename):
    return joblib.load(filename)