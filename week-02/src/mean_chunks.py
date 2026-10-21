import pandas as pd
from statistics import mean

avgs = []
meds = []
sums = []
lens = []

for chunk in pd.read_csv("/data/yellow_tripdata_2024-01.csv", chunksize=1_000_000):
    avg = chunk["trip_distance"].mean()
    med = chunk["trip_distance"].median()
    sum = chunk["trip_distance"].sum()
    length = len(chunk)

    avgs.append(avg)
    meds.append(med)
    sums.append(sum)
    lens.append(length)

    print(avg)
    print(med)
    print(length)
    print("=" * 10, "\n")

print(mean(avgs))

sum = 0
for i in sums:
    sum += i

nrows = 0
for i in lens:
    nrows += i

print(sum / nrows)
