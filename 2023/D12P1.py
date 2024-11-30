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

def is_valid(springs, nums):
  groups = []
  in_group = False
  group_len = 0
  for i in range(len(springs)):
    if springs[i] == "#":
      if in_group:
        group_len += 1
      else:
        in_group = True
        group_len += 1
    else:
      if in_group:
       groups.append(group_len)
       in_group = False
       group_len = 0
      else:
        pass
  if group_len != 0: groups.append(group_len)
  return groups == nums
      

counts = []
arrangements = []
for i, line in enumerate(content.splitlines()):
  print(i)
  springs, nums = line.split()
  nums = list(map(int, nums.split(',')))
  count = springs.count("?")
  counts.append(count)
  arrangements_for_line = 0
  for combo in itertools.product(['#','.'], repeat=count):
    new_springs = list(springs)
    j = 0
    for i in range(len(new_springs)):
      if new_springs[i] == "?":
        new_springs[i] = combo[j]
        j += 1
    #print(combo)
    #print(new_springs)
    arrangements_for_line += is_valid(new_springs, nums)
  arrangements.append(arrangements_for_line)

print(counts)
print(max(counts))
print(sum([2**n for n in counts]))
print(arrangements)
print(sum(arrangements))
