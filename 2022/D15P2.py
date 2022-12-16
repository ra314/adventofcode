import re
myfile = open("input.txt")
coord_lim = 4000000
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

unique_beacons = set([x.beacon for x in SBs])
for y in range(coord_lim+1):
  if y % 100000 == 0:
    print(y)
  no_beacon_ranges = []
  for sb in SBs:
    dist_to_row = abs(sb.sensor[1] - y)
    if dist_to_row > sb.dist:
      continue
    remaining_dist = sb.dist - dist_to_row
    no_beacon_ranges.append(range(max(sb.sensor[0]-remaining_dist,0), min(sb.sensor[0]+remaining_dist,coord_lim)))

  # Merge ranges
  # Could be made faster by not using a list to store the ranges.
  # Since we do a lot of deletion and insertion
  no_beacon_ranges = sorted(no_beacon_ranges, key=lambda x: x.start)
  i = 0
  while i < len(no_beacon_ranges)-1:
    first = no_beacon_ranges[i]
    second = no_beacon_ranges[i+1]
    if first.stop >= second.stop:
      no_beacon_ranges.pop(i+1)
    elif first.stop >= second.start:
      no_beacon_ranges.pop(i)
      no_beacon_ranges.pop(i)
      no_beacon_ranges.insert(i, range(first.start, second.stop))
    else:
      i += 1
  
  no_beacon_count = 0
  for nbr in no_beacon_ranges:
    no_beacon_count += ((nbr.stop - nbr.start)+1)
  if no_beacon_count != coord_lim + 1:
    print(y, no_beacon_ranges)
    break

print(2889605*4000000 + 3398893)
