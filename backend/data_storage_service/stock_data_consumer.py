import json
import pandas as pd

from .utils import *
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'stock-data',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

def process_stock_data():
    INSERTING_DATA = True
    for message in consumer:
        print("print")
        print(message.value)
        if message.value == 'No more data':
            print("print no more data")
            break

        if message.value == 'Change to news':
            INSERTING_DATA = False
            print("print change to news")
            continue

        if INSERTING_DATA:
            code = message.value['code']
            message = json.loads(message.value['data'])
            message = pd.DataFrame(message)
            print("creating table")
            create_table_for_stock_code(code)
            insert_data_into_table(code, message)
            print("print insert data")
        else:
            code = message.value['code']
            message = json.loads(message.value['news'])
            message = pd.DataFrame(message)
            print("creating table news")
            create_table_for_stock_news(code)
            insert_data_into_news_table(code, message)
            print("print insert data news")

if __name__ == '__main__':
    process_stock_data()

