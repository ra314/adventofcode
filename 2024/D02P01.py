import reader
content = reader.read()

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
safe_count = 0
for line in content.splitlines():
  nums = [int(x) for x in line.split()]
  arr = np.array(nums)
  diffs = np.diff(sliding_window_view(arr, 2))
  if np.all(diffs >= 1) and np.all(diffs <= 3):
    safe_count += 1
  if np.all(diffs <= -1) and np.all(diffs >= -3):
    safe_count += 1
print(safe_count)

# Cleaned up solution.
def is_safe(arr):
  diffs = np.diff(sliding_window_view(arr, 2))
  lo, hi = np.min(diffs), np.max(diffs)
  return (lo >= 1 and hi <= 3) or (hi <= -1 and lo >= -3)

safe_count = 0
for line in content.splitlines():
  nums = [int(x) for x in line.split()]
  safe_count += is_safe(nums)
print(safe_count)
