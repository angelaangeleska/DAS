import json
import pandas as pd

from utils import *
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'output_stock_data',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

def process_stock_data():
    for message in consumer:
        print("print")
        print(message.value)

        code = message.value['code']
        message = json.loads(message.value['data'])
        message = pd.DataFrame(message)
        print("creating table stocks")
        create_table_for_stock_code(code)
        insert_data_into_table(code, message)
        print("print insert data stocks")


if __name__ == '__main__':
    process_stock_data()
