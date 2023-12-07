import numpy as np
from collections import defaultdict
import re
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

def to_num(arr):
  return list(map(int, arr.split()))

total = 0
for line in content.splitlines():
  all_nums = line.split(":")
  winning_nums, your_nums = list(map(to_num, all_nums[1].split("|")))
  inter = set(winning_nums).intersection(your_nums)
  print(inter)
  score = 2**(len(inter)-1)
  print(score)
  if len(inter):
    total += score

print(total)
