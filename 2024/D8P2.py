import reader
content = reader.read()

import numpy as np
from collections import defaultdict
content = np.array([list(line) for line in content.splitlines()])

# Find the list of uniuqe non-period characters.
display = content.copy()
antennas = set(content[content != "."].tolist())
antinode_count = set()
for antenna in antennas:
  # Find the location of all antennas with the same antenna type.
  locs = np.where(content==antenna)
  locs = list(zip(locs[0].tolist(), locs[1].tolist()))
  # Iterate over the locations pairwise.
  for i, loc1 in enumerate(locs):
    for j, loc2 in enumerate(locs):
      if i == j:
        continue
      loc1, loc2 = np.array(loc1), np.array(loc2)
      delta = loc1 - loc2
      curr = loc1+delta
      while curr[0] >= 0 and curr[0] < content.shape[0] and curr[1] >= 0 and curr[1] < content.shape[1]:
        display[curr[0]][curr[1]] = "#"
        antinode_count.add(tuple(curr.tolist()))
        curr += delta

print(display)
print(np.sum(display!="."))
