import numpy as np
import re
from collections import defaultdict
import sys


f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f1.read()
content = content.splitlines()
nrows = len(content)
ncols = len(content[0])

def adjacents(y,x):
  return [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]

graph = defaultdict(list)

for y in range(nrows):
  for x in range(ncols):
    curr = content[y][x]
    if curr == "#": continue
    for y2, x2 in adjacents(y,x):
      if y2 < 0 or x2 < 0 or y2 >= nrows or x2 >= ncols: continue
      next = content[y2][x2]
      if next == "#": continue
      graph[(y,x)].append((y2,x2))

stack = [[(0,1)]]
path_tree = []
seen = set()
depth = 0
best_path = set()
while True:
  cstack = stack[depth]
  curr = stack.pop()
  y, x = curr
  path_tree.append(curr)
  seen.add(curr)
  nstack = []
  for next in graph[(y,x)]:
    if next in seen: continue
    y2, x2 = next
    nstack.append((y2,x2))
  del path_tree[-1]
  seen.remove(curr)

def DFS(y,x,seen):
  if y == (nrows-1):
    return 1, [(y,x)]
  max_len = 0
  best_path = []
  adj_found = False
  for next in graph[(y,x)]:
    if next in seen: continue
    adj_found = True
    y2, x2 = next
    seen.add(next)
    nmax_len, npath = DFS(y2, x2, seen)
    if nmax_len > max_len:
      max_len = nmax_len
      best_path = npath
    seen.remove(next)
  if not adj_found:
    return -10000, []
  return 1+max_len, [(y,x)] + best_path

mlen, path = DFS(0,1, set())

content = list(map(list, content))
for y, x in path:
  content[y][x] = "O"

print("\n".join(["".join(x) for x in content]))
