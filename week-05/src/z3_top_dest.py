import pyspark.sql.functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.parquet("hdfs://namenode:9000/taxi/yellow_tripdata_2024-01.parquet")

counts = df.groupBy("PULocationID", "DOLocationID").agg(
    F.count("*").alias("count")
)

query = counts.groupBy("PULocationID").agg(
    F.max_by("DOLocationID", "count"),
    F.max("count")
)

print(query.explain())

rows = query.collect()

for row in rows:
    print(*row, sep="\t")

spark.stop()
