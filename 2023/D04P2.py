import numpy as np
from collections import defaultdict
import re
from math import inf
from functools import lru_cache

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

def to_num(arr):
  return list(map(int, arr.split()))

card_to_matches =[] 
for line in content.splitlines():
  all_nums = line.split(":")
  winning_nums, your_nums = list(map(to_num, all_nums[1].split("|")))
  inter = set(winning_nums).intersection(your_nums)
  card_to_matches.append(len(inter))

@lru_cache(maxsize=None)
def score(card_num):
  matches = card_to_matches[card_num]
  if matches == 0:
    return 1
  tote = 1
  for x in range(1,matches+1):
    tote += score(card_num+x)
  return tote
  
print(sum([score(x) for x in range(len(content.splitlines()))]))
