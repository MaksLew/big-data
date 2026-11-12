import sys
from collections import defaultdict

current_location: int | None = None
counts: dict[float, int] = defaultdict(int)

for line in sys.stdin:
    location_text, distance_text, count_text = line.rstrip().split("\t")
    location = int(location_text)
    distance = float(distance_text)
    count = int(count_text)

    if current_location is not None and location != current_location:
        for value, value_count in counts.items():
            print(f"{current_location}\t{value}\t{value_count}")
        counts.clear()

    current_location = location
    counts[distance] += count

if current_location is not None:
    for value, value_count in counts.items():
        print(f"{current_location}\t{value}\t{value_count}")
