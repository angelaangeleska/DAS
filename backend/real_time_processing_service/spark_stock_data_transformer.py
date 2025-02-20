from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import *

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 pyspark-shell'

kafka_input_config = {
    "kafka.bootstrap.servers": "kafka:9092",
    "subscribe": "stock-data",
    "startingOffsets": "earliest",
    "failOnDataLoss": "false"
}
kafka_output_config = {
    "kafka.bootstrap.servers": "kafka:9092",
    "topic": "output_stock_data",
    "checkpointLocation": "./check.txt"
}


spark = SparkSession \
    .builder \
    .appName("SparkStockDataTransformer") \
    .config("spark.sql.streaming.forceDeleteTempCheckpointLocation", True) \
    .master("local[*]") \
    .getOrCreate()

df_schema = StructType([
    StructField("code", StringType(), True),
    StructField("data", MapType(StringType(), MapType(StringType(), FloatType())), True)
])

## Read Stream
df = spark \
    .readStream \
    .format("kafka") \
    .options(**kafka_input_config) \
    .load() \
    .select(F.from_json(F.col("value").cast("string"), df_schema).alias("json_data")) \
    .select("json_data.*")

# Filter for eligible transactions
df = df.select(
    F.col("code"),
    F.explode(F.col("data")).alias("key", "nested_map")
).select(
    F.col("code"),
    F.col("key"),
    F.explode(F.col("nested_map")).alias("sub_key", "values")
).select(
    F.col("code"),
    F.col("key"),
    F.col("sub_key"),
    F.explode(F.col("values")).alias("value")
)

# Filter rows where the value is not empty
filtered_df = df.filter(F.col("value") > 0)


# Apply foreachBatch to process and print each micro-batch
write = df.writeStream \
    .format("kafka")\
    .options(**kafka_output_config)\
    .start()

write.awaitTermination()