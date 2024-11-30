import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
import itertools
from math import inf
from dijkstar import Graph, find_path
from multiprocessing import Pool
import tqdm

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

content = np.array(list(map(list, content.splitlines())))
print(content)
print()

empty_rows = set()
for y in range(content.shape[0]):
  if np.all(content[y]=="."): empty_rows.add(y)
empty_cols = set()
for x in range(content.shape[1]):
  if np.all(content[:,x]=="."): empty_cols.add(x)
print(empty_rows)
print(empty_cols)

galaxies = list(zip(*np.where(content == "#")))
pairs = set()
for i in range(len(galaxies)):
  for j in range(len(galaxies)):
    if i==j: continue
    start, end = galaxies[i], galaxies[j]
    pairs.add(tuple(sorted([start,end])))
pairs = list(pairs)

big_cost = 1000000
def manhat(pair):
  start, end = pair
  y1, x1 = start
  y2, x2 = end
  cost = 0
  for i in range(*sorted([x1,x2])):
    curr = i+1
    if curr in empty_cols:
      cost += big_cost
    else:
      cost += 1
  for i in range(*sorted([y1,y2])):
    curr = i+1
    if curr in empty_rows:
      cost += big_cost
    else:
      cost += 1
  return cost


retval = []
for pair in pairs:
  retval.append(manhat(pair))

print(len(retval), sum(retval))
