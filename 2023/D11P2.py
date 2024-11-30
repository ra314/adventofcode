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

graph = Graph()
for y in range(content.shape[0]):
  for x in range(content.shape[1]):
    cost = 1
    if y in empty_rows or x in empty_cols:
      cost = 1000000
    for adj in np.array((y,x)) + np.array([[1,0],[0,1],[-1,0],[0,-1]]):
      if adj[0] < 0 or adj[1] < 0 or adj[0] >= content.shape[0] or adj[1] >= content.shape[1]:
        continue
      graph.add_edge((y,x), tuple(adj), cost)

print()

galaxies = list(zip(*np.where(content == "#")))
pairs = set()
for i in range(len(galaxies)):
  for j in range(len(galaxies)):
    if i==j: continue
    start, end = galaxies[i], galaxies[j]
    pairs.add(tuple(sorted([start,end])))

pairs = list(pairs)



def manhat(pair):
  start, end = pair
  return find_path(graph, start, end).total_cost


if __name__ == '__main__':
  retval = []
  pool = Pool(processes=8)
  for x in tqdm.tqdm(pool.imap_unordered(manhat, pairs), total=len(pairs)):
    retval.append(x)

print(len(retval), sum(retval))
