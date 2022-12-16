content = open("input.txt").read()

import numpy as np
grid = np.array([list(line) for line in content.splitlines()])

from collections import Counter
message = ""
for column in grid.swapaxes(1,0):
  counts = Counter(column)
  message += (min(counts, key=counts.get))

print(message)
