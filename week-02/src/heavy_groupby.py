import pandas as pd

data = pd.read_parquet("/data/yellow_tripdata_2024-01.parquet")

res = data.groupby(["PULocationID", "DOLocationID"]).apply(
    lambda g: g.sort_values("trip_distance"), include_groups=False
)
