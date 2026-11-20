import pyspark.sql.functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.parquet("hdfs://namenode:9000/taxi/yellow_tripdata_2024-01.parquet")

rows = (
    df.groupBy("PULocationID")
    .agg(
        F.median("trip_distance"),
        F.count("*"),
        F.percentile_approx("trip_distance", 0.5),
    )
    .collect()
)

for row in rows:
    print(*row, sep="\t")

spark.stop()
