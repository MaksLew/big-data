import sys

current_location: int | None = None
current_distance: float = 0.0
current_count: int = 0

for line in sys.stdin:
    location, distance, count = line.strip().split('\t')
    location = int(location)
    distance = float(distance)
    count = int(count)

    if location == current_location:
        current_distance += distance
        current_count += count
    else:
        if current_location is not None:
            print(f"{current_location}\t{current_distance}\t{current_count}")

        current_location = location
        current_distance = distance
        current_count = count

if current_location is not None:
        print(f"{current_location}\t{current_distance}\t{current_count}")
