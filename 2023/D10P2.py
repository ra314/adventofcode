import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
import itertools
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f1.read()

s_replacement = "F"

height = len(content.splitlines())
width = len(content.splitlines()[0])
start = content.find("S")
start = (start%(width+1), start//(width+1))
content = content.replace("S", s_replacement)
content = content.splitlines()

def neighbours(char):
  match char:
    case "|":
      return [[-1,0],[1,0]]
    case "-":
      return [[0,-1],[0,1]]
    case "L":
      return [[-1,0],[0,1]]
    case "J":
      return [[-1,0],[0,-1]]
    case "7":
      return [[0,-1],[1,0]]
    case "F":
      return [[0,1],[1,0]]
    case ".":
      return []
    case _:
      assert(False)

visited = set()
nodes = deque([(start,0)])
while nodes:
  curr, dist = nodes.popleft()
  char = content[curr[0]][curr[1]]
  visited.add(curr)
  neighs = neighbours(char)
  for n in neighs:
    n = tuple(n)
    new = tuple(np.array(curr)+np.array(n))
    if new in visited: continue
    visited.add(new)
    if new[0] < 0 or new[1] < 0 or new[0] >= height or new[1] >= width: continue
    nodes.append((new, dist+1))
  #print(char, curr, dist)

remap = np.zeros((height, width), dtype='<U11')

for y in range(height):
  for x in range(width):
    if not((y,x) in visited):
      remap[y,x] = "."
    else:
      remap[y,x] = content[y][x]
content = remap

print()
print("\n".join(["".join(x) for x in content]))

bigcontent = np.zeros((height*2, width*2), dtype='<U11')
for node in visited:
  bigcontent[node[0]*2][node[1]*2] = content[node]
bigcontent[bigcontent==""] = "."
print()
print("\n".join(["".join(x) for x in bigcontent]))

for y in range(bigcontent.shape[0]):
  for x in range(bigcontent.shape[1]):
    char = bigcontent[y,x]
    neighs = neighbours(char)
    for n in neighs:
      new = np.array([y,x])+np.array(n)
      if new[0] < 0 or new[1] < 0 or new[0] >=(bigcontent.shape[0]) or new[1] >= (bigcontent.shape[1]): continue
      if bigcontent[tuple(new)] == ".":
        if n[0] == 0:
          bigcontent[tuple(new)] = "-"
        else:
          bigcontent[tuple(new)] = "|"

print()
print("\n".join(["".join(x) for x in bigcontent]))

flood_visit = set()
nodes = deque()
nodes.append(tuple([0,0]))
bigcontent = np.pad(bigcontent, (1,1))
bigcontent[bigcontent=='0'] = "."
while nodes:
  curr = nodes.popleft()
  flood_visit.add(curr)
  curr = np.array(curr)
  neighs = curr + np.array([[1,0],[-1,0],[0,-1],[0,1]])
  for new in neighs:
    new = tuple(new)
    if new in flood_visit: continue
    if new[0] < 0 or new[1] < 0 or new[0] >=(bigcontent.shape[0]) or new[1] >= (bigcontent.shape[1]): continue
    char = bigcontent[tuple(new)]
    if char != ".": continue
    flood_visit.add(new)
    nodes.append(new)

for node in flood_visit:
  bigcontent[node] = "X"
bigcontent = bigcontent[1:-1,1:-1]

print()
print("\n".join(["".join(x) for x in bigcontent]))

isolated_count = 0
for y in range(height):
  for x in range(width):
    char = content[y,x]
    if char == ".":
      y2, x2 = y*2, x*2
      if np.all(bigcontent[y2:y2+2,x2:x2+2] == "."):
        isolated_count += 1

print(isolated_count)
