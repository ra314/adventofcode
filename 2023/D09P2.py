import numpy as np
from collections import defaultdict
from collections import Counter
import re
import itertools
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

def my_diff(numbers):
  return [numbers[i+1]-numbers[i] for i in range(len(numbers)-1)]

pluses = []
for line in content.splitlines():
  nums = list(map(int, line.split()))
  diffs = [nums]
  diff = nums
  while sum([x==0 for x in diff]) != len(diff):
    diff = my_diff(diff)
    diffs.append(diff)
  for i in reversed(range(1, len(diffs))):
    plus = diffs[i-1][0] - diffs[i][0]
    diffs[i-1].insert(0, plus)
  pluses.append(plus)

print(pluses)
print(sum(pluses))
