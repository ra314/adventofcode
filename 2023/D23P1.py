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

def adjacents(y,x, char):
  match char:
    case ">":
      return [(y,x+1)]
    case "<":
      return [(y,x-1)]
    case "^":
      return [(y-1,x)]
    case "v":
      return [(y+1,x)]
  return [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]

graph = defaultdict(list)

for y in range(nrows):
  for x in range(ncols):
    curr = content[y][x]
    if curr == "#": continue
    for adj in adjacents(y,x, curr):
      y2, x2 = adj
      if y2 < 0 or x2 < 0 or y2 >= nrows or x2 >= ncols: continue
      next = content[y2][x2]
      if next == "#": continue
      graph[(y,x)].append((y2,x2))

sys.setrecursionlimit(10000)
def DFS(y,x,seen):
  if y == (nrows-1):
    return 1
  max_len = 0
  for next in graph[(y,x)]:
    if next in seen: continue
    y2, x2 = next
    seen.add(next)
    max_len = max(max_len, DFS(y2, x2, seen))
    seen.remove(next)
  return 1+max_len

print(DFS(0,1, set()))
