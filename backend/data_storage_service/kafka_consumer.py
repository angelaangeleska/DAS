import json
from array import ArrayType
from xml.dom.minicompat import StringTypes

import pandas as pd

from utils import *
from kafka import KafkaConsumer

from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import *

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 pyspark-shell'

consumer = KafkaConsumer(
    'output',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

def process_stock_messages():
    INSERTING_DATA = True
    for message in consumer:
        print("print")
        print(message.value)
        # TODO apache spark
        if message.value == 'No more data':
            print("print no more data")
            break

        if message.value == 'Change to news':
            INSERTING_DATA = False
            print("print change to news")
            continue

        if INSERTING_DATA:
            # json_loads = json.loads(message.value)
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
    process_stock_messages()
    print("FINISHED WITH CONSUMER")
