kafka_input_config = {
    "kafka.bootstrap.servers": "kafka:9092",
    "subscribe": "stock-data",
    "startingOffsets": "earliest",
    "failOnDataLoss": "false"
}
kafka_output_config = {
    "kafka.bootstrap.servers": "kafka:9092",
    "topic": "output",
    "checkpointLocation": "./check.txt"
}

spark = SparkSession \
    .builder \
    .appName("SparkDemo") \
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
df = df.filter((F.col("code") != ""))

## Create an output and produce to kafka target
output_df = df.select(F.to_json(F.struct(*df.columns)).alias("value"))

utput_df = df.select(F.to_json(F.struct(*df.columns)).alias("value"))

write = output_df \
    .writeStream \
    .format("kafka") \
    .options(**kafka_output_config) \
    .start()

write.awaitTermination()
