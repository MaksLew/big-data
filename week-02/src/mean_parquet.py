
import pandas as pd


data = pd.read_parquet('/data/yellow_tripdata_2024-01.parquet')

print(len(data))
print(data.memory_usage(deep=True).sum())
print(data['trip_distance'].mean)
