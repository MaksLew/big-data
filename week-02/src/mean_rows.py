import sys
import pandas as pd

try:
    n = int(sys.argv[1])
    data = pd.read_csv("/data/yellow_tripdata_2024-01.csv", nrows=n)
except IndexError:
    data = pd.read_csv("/data/yellow_tripdata_2024-01.csv")

print(f"{len(data)=}")
print(f"{data.memory_usage(deep=True).sum()}")
