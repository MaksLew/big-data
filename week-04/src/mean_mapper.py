import sys

for line in sys.stdin:
    els = line.strip().split(',')
    try:
        trip_distance = float(els[4])
        location = int(els[7])
        print(f"{location}\t{trip_distance}")
    except ValueError:
        continue
