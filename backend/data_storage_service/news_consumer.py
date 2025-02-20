import json
import pandas as pd

from utils import *
from kafka import KafkaConsumer

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 pyspark-shell'

consumer = KafkaConsumer(
    'output_stock_news',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

def process_stock_news():
    for message in consumer:
        print("print")
        print(message.value)

        code = message.value['code']
        message = json.loads(message.value['news'])
        message = pd.DataFrame(message)
        print("creating table news")
        create_table_for_stock_news(code)
        insert_data_into_news_table(code, message)
        print("print insert data news")

if __name__ == '__main__':
    process_stock_news()
