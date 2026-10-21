import pandas as pd

csv = pd.read_csv('/data/yellow_tripdata_2024-01.csv', nrows=200_000)
parquet = pd.read_parquet('/data/yellow_tripdata_2024-01.parquet').head(200_000)

print(f"{csv.dtypes=}")
print(f"{parquet.dtypes=}")
print(f"{csv.memory_usage(deep=True).sum()}")
print(f"{parquet.memory_usage(deep=True).sum()}")
