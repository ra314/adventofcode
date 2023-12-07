import numpy as np
from collections import defaultdict
import re
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

times = list(map(int, content.splitlines()[0].split(":")[1].split()))
distances = list(map(int, content.splitlines()[1].split(":")[1].split()))

print(times, distances)

ways = []
for x in range(len(times)):
  time, distance = times[x], distances[x]
  ways_to_win = 0
  for i in range(time):
    speed = i
    time_left = time-i
    dist_covered = time_left*speed
    if dist_covered > distance:
      ways_to_win += 1
  print(ways_to_win)
  ways.append(ways_to_win)

print(np.prod(np.array(ways)))
