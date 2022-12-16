import numpy as np
from math import sqrt

myfile = open("input2.txt")
content = myfile.read()

ranges = []

# Merging the ranges
j = 0
for line in content.splitlines():
  j += 1
  mini = int(line.split('-')[0])
  maxi = int(line.split('-')[1])
  intersecting_range_found = False
  for i in range(len(ranges)):
    rangi = ranges[i]
    if (mini in rangi) or (maxi in rangi):
      ranges[i] = range(min(mini, rangi[0]), max(maxi, rangi[-1])+1)
      intersecting_range_found = True
      break
  if not intersecting_range_found:
    ranges.append(range(mini, maxi+1))

# Finding the smallest
ranges = sorted(ranges, key = lambda x: x[0])
for i in range(len(ranges)):
  if ranges[i][-1] != ranges[i+1][0]-1:
    print(ranges[i][-1]+1)
    break
