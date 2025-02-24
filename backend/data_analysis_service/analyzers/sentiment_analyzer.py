import nltk
import pandas as pd

from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_sentiment(df):
    sia = SentimentIntensityAnalyzer()
    # print(df[:2])
    scores = df['summary'].apply(sia.polarity_scores)

    scores_df = pd.DataFrame.from_records(scores)
    df = df.join(scores_df)

    df = df.apply(compound_transform, axis=1)
    df.drop(columns=['neu', 'neg', 'pos', 'compound'], axis=1, inplace=True)

    return df

def assign_points(row):
    if row["sentiment"] == "Good news":
        return 1
    elif row["sentiment"] == "Bad news":
        return -1
    else:
        return 0

# call this func
def news_analyzer(df):
    df = analyze_sentiment(df)
    df["points"] = df.apply(assign_points, axis=1)
    total_points = df["points"].sum()

    threshold = 1
    if total_points >= threshold:
        return 'Buy'
    elif -threshold < total_points < threshold:
        return 'Hold'
    else:
        return 'Sell'

def compound_transform(row):
    if row['compound'] > 0.05:
        row['sentiment'] = "Good news"
    elif row['compound'] < -0.05:
        row['sentiment'] = "Bad news"
    else:
        row['sentiment'] = "Neutral news"
    return row