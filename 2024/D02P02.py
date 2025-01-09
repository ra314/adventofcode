import reader
content = reader.read()

import numpy as np
import itertools
from numpy.lib.stride_tricks import sliding_window_view
safe_count = 0
for line in content.splitlines():
  nums = [int(x) for x in line.split()]
  combos = list(itertools.combinations(nums, len(nums)-1))
  combos.append(nums)
  for combo in combos:
    arr = np.array(combo)
    diffs = np.diff(sliding_window_view(arr, 2))
    if np.all(diffs >= 1) and np.all(diffs <= 3):
      safe_count += 1
      break
    if np.all(diffs <= -1) and np.all(diffs >= -3):
      safe_count += 1
      break
print(safe_count)

# Cleaned up solution.
def is_safe(arr):
  diffs = np.diff(sliding_window_view(arr, 2))
  lo, hi = np.min(diffs), np.max(diffs)
  return (lo >= 1 and hi <= 3) or (hi <= -1 and lo >= -3)

safe_count = 0
for line in content.splitlines():
  nums = [int(x) for x in line.split()]
  combos = list(itertools.combinations(nums, len(nums)-1))
  combos.append(nums)
  safe_count += max([is_safe(combo) for combo in combos])
print(safe_count)
