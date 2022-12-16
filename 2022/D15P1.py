import re, numpy as np
from collections import defaultdict
myfile = open("input.txt")
y = 2000000
content = myfile.read().splitlines()

SBs = []
class SB:
  def __init__(self, sensor, beacon):
    self.sensor = sensor
    self.beacon = beacon
    self.dist = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

xs = []
for line in content:
  sx, sy, bx, by = [int(x) for x in re.findall(r'-?\d+', line)]
  xs.extend([sx, bx])
  SBs.append(SB((sx,sy), (bx, by)))

x_range = max(xs) - min(xs)
no_beacon_ranges = []
for sb in SBs:
  dist_to_row = abs(sb.sensor[1] - y)
  if dist_to_row > sb.dist:
    continue
  remaining_dist = sb.dist - dist_to_row
  no_range = range(sb.sensor[0]-remaining_dist, sb.sensor[0]+remaining_dist)
  no_beacon_ranges.append(no_range)

# Merge ranges
no_beacon_ranges = sorted(no_beacon_ranges, key=lambda x: x.start)
print(no_beacon_ranges)
i = 0
while i < len(no_beacon_ranges)-1:
  first = no_beacon_ranges[i]
  second = no_beacon_ranges[i+1]
  if first.stop >= second.stop:
    no_beacon_ranges.pop(i+1)
    print(no_beacon_ranges)
  elif first.stop >= second.start:
    no_beacon_ranges.pop(i)
    no_beacon_ranges.pop(i)
    no_beacon_ranges.insert(i, range(first.start, second.stop))
    print(no_beacon_ranges)
  else:
    i += 1

# Remove any places where a beacon is
no_beacon_count = 0
unique_beacons = set([x.beacon for x in SBs])
for ub in unique_beacons:
  if ub[1] != y:
    continue
  for nbr in no_beacon_ranges:
    if ub[0] in nbr:
      no_beacon_count -= 1
      print(ub[0], nbr)
print(no_beacon_count)
for nbr in no_beacon_ranges:
  no_beacon_count += ((nbr.stop - nbr.start)+1)
print(no_beacon_count)
