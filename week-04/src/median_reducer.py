import sys
from collections import defaultdict


def median(counts: dict[float, int], total: int) -> float | None:
    left_position = (total + 1) // 2
    right_position = (total + 2) // 2

    cumulative = 0
    right = 0.0
    left: float | None = None

    for distance in sorted(counts):
        cumulative += counts[distance]

        if cumulative >= left_position and left is None:
            left = distance
        if cumulative >= right_position:
            right = distance
            break

    if left is not None:
        return (left + right) / 2


current_location: int | None = None
distance_counts: dict[float, int] = defaultdict(int)
total = 0

for line in sys.stdin:
    location, distance, count = line.rstrip().split("\t")
    location = int(location)
    distance = float(distance)
    count = int(count)

    if current_location is not None and location != current_location:
        print(
            f"{current_location}\t{median(distance_counts, total)}"
            f"\t{total}\t{len(distance_counts)}"
        )
        distance_counts.clear()
        total = 0

    current_location = location
    distance_counts[distance] += count
    total += count

if current_location is not None:
    print(
        f"{current_location}\t{median(distance_counts, total)}"
        f"\t{total}\t{len(distance_counts)}"
    )
