import pandas as pd

data = pd.read_parquet("/data/yellow_tripdata_2024-01.parquet")

# Za mało pamięci
# res = data.groupby(["PULocationID", "DOLocationID"]).apply(
#     lambda g: g["trip_distance"].agg(["count", "mean"])
# )

# Zły kształt danych
# res = data["trip_distance"].agg(["count", "mean"])

res = data.groupby(["PULocationID", "DOLocationID"])["trip_distance"].agg(["count", "mean"])

print(res[res["count"] == res["count"].max()])
