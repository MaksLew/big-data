import pandas as pd


data = pd.read_csv('/data/yellow_tripdata_2024-01.csv')

print(len(data))
print(data['trip_distance'].mean)
