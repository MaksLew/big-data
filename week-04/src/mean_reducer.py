import sys

current_location: int | None = None
current_distance: float = 0.0
current_trip_count: int = 0

for line in sys.stdin:
    location, distance = line.strip().split('\t')
    location = int(location)
    distance = float(distance)

    if location == current_location:
        current_distance += distance
        current_trip_count += 1
    else:
        if current_location is not None:
            print(f"{current_location}\t{current_distance / current_trip_count}")

        current_location = location
        current_distance = distance
        current_trip_count = 1

if current_location is not None:
    print(f"{current_location}\t{current_distance / current_trip_count}")
