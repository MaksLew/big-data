import argparse

import pyspark.sql.functions as F
from pyspark.sql import SparkSession

ALLOWED_FILETYPES = ["csv", "parquet"]

parser = argparse.ArgumentParser()
parser.add_argument("filetype")
parser.add_argument("time")
args = parser.parse_args()

filetype = str(args.filetype)
time = int(args.time)

if filetype.lower() not in ALLOWED_FILETYPES:
    raise ValueError(f"{filetype} is not an allowed filetype.")


spark = SparkSession.builder.getOrCreate()

if filetype.lower() == "csv":
    df = spark.read.csv(
        "hdfs://namenode:9000/csv/yellow_tripdata_2024-01.csv",
        header=True,
        inferSchema=True,
    )

else:
    df = spark.read.parquet("hdfs://namenode:9000/taxi/yellow_tripdata_2024-01.parquet")

rows = df.groupBy("PULocationID").agg(F.avg("trip_distance"), F.count("*")).collect()

for row in rows:
    print(*row, sep="\t")

spark.stop()
