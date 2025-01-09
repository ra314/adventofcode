import reader
content = reader.read()

import numpy as np
from collections import defaultdict
content = np.array([list(line) for line in content.splitlines()])

# Find the list of uniuqe non-period characters.
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
      antinode = loc1 + (loc1 - loc2)
      if antinode[0] < 0 or antinode[0] >= content.shape[0] or antinode[1] < 0 or antinode[1] >= content.shape[1]:
        continue
      #content[antinode[0]][antinode[1]] = "#"
      antinode_count.add(tuple(antinode.tolist()))

print(content)
print(len(antinode_count))
