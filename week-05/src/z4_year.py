import time

import pyspark.sql.functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("z4-year").getOrCreate()

df = spark.read.parquet("hdfs://namenode:9000/taxi/yellow_tripdata_2024-*.parquet")

start = time.time()
partitions = df.rdd.getNumPartitions()
print(f"partitions\t{partitions}\tseconds\t{time.time() - start:.3f}")

start = time.time()
trips = df.count()
print(f"trips\t{trips}\tseconds\t{time.time() - start:.3f}")

start = time.time()
mean_distance = df.agg(F.avg("trip_distance")).first()[0] # ty: ignore
print(f"mean_distance\t{mean_distance}\tseconds\t{time.time() - start:.3f}")

start = time.time()
rows = (
    df.groupBy("PULocationID")
    .agg(F.avg("trip_distance").alias("mean_distance"))
    .orderBy("PULocationID")
    .collect()
)
elapsed = time.time() - start
print(f"mean_distance_by_zone\tseconds\t{elapsed:.3f}")

spark.stop()
