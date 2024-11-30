import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
import itertools
from math import inf
import itertools

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

content = list(map(list, content.splitlines()))
content = np.array(content)
records = []
cache = {}
i = 0

def hesh(x):
  return "\n".join(["".join(x) for x in content])

def total_load(x):
  total = 0
  for i, line in enumerate(x[::-1]):
    total += (np.sum(line==["O"])*(i+1))
  return total

while True:
  h = hesh(content)
  if h in cache:
    break
  cache[h] = i
  records.append(content.copy())
  i += 1
  for _ in range(4):
    # Go through each col try and shift each round rock as far up as possible
    for x in range(len(content[0])):
      lowest_open = -1
      for y in range(len(content)):
        char = content[y][x]
        match char:
          case "O":
            if lowest_open != -1:
              content[lowest_open][x] = "O"
              content[y][x] = "."
              lowest_open += 1
          case ".":
            if lowest_open == -1:
              lowest_open = y
          case "#":
            lowest_open = -1
          case _:
            assert(False)
    content = np.rot90(content, k=-1)
    #print("\n".join(["".join(x) for x in content]))
    #print()

for x in records:
  print(total_load(x))

steps_before_cycle_start = cache[hesh(content)]
cycle_length = len(records) - steps_before_cycle_start
print(steps_before_cycle_start, cycle_length)
record_index = (1000000000-steps_before_cycle_start)%cycle_length
print(record_index, total_load(records[record_index+steps_before_cycle_start]))
