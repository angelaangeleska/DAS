import os

from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql import SparkSession

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 pyspark-shell'

kafka_input_config = {
    "kafka.bootstrap.servers": "kafka:9092",
    "subscribe": "stock-news",
    "startingOffsets": "earliest",
    "failOnDataLoss": "false"
}
kafka_output_config = {
    "kafka.bootstrap.servers": "kafka:9092",
    "topic": "output_stock_news",
    "checkpointLocation": "./check.txt"
}

spark = SparkSession \
    .builder \
    .appName("SparkStockNewsTransformer") \
    .master("local[*]") \
    .getOrCreate()

df_schema = StructType([
    StructField("code", StringType(), True),
    StructField("news", MapType(StringType(), MapType(StringType(), StringType())), True)
])

## Read Stream
df = spark \
    .readStream \
    .format("kafka") \
    .options(**kafka_input_config) \
    .load() \
    .select(F.from_json(F.col("value").cast("string"), df_schema).alias("json_data")) \
    .select("json_data.*")

## Filter for eligible transactions
df_exploded = df.select(
    F.col("code"),
    F.explode(F.col("news")).alias("key", "nested_map")
).select(
    F.col("code"),
    F.col("key"),
    F.explode(F.col("nested_map")).alias("sub_key", "value")
)

## Create an output and produce to kafka target
output_df = df.select(F.to_json(F.struct(*df.columns)).alias("value"))

write = output_df \
    .writeStream \
    .format("kafka") \
    .options(**kafka_output_config) \
    .start()

write.awaitTermination()
