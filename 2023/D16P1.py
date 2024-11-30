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
content = np.array(list(map(list, content.splitlines())))
clean_grid = np.zeros(content.shape)
cache = set()

curr = [np.array((0,0)), np.array((0,1))]

L = np.array((0,-1))
R = np.array((0,1))
U = np.array((-1,0))
D = np.array((1,0))

def show(grid):
  return "\n".join(["".join([str(int(x)) for x in line]) for line in grid])

live = [curr]
while live:
  new_live = []
  for beam in live:
    pos, dirc = beam
    if pos[0] < [0] or pos[1] < 0 or pos[0] >= content.shape[0] or pos[1] >= content.shape[1]:
      continue
    key = (tuple(pos), tuple(dirc))
    if key in cache:
      continue
    next = pos+dirc
    clean_grid[tuple(pos)] = 1
    cache.add(key)
    char = content[tuple(pos)]
    match char:
      case ".":
        new_live.append([next, dirc])
      case "|":
        if dirc[0] != 0:
          new_live.append([next, dirc])
        else:
          new_live.append([pos+U,U])
          new_live.append([pos+D,D])
      case "-":
        if dirc[0] == 0:
          new_live.append([next, dirc])
        else:
          new_live.append([pos+L,L])
          new_live.append([pos+R,R])
      case "\\":
        ndir = np.flip(dirc)
        new_live.append([pos+ndir, ndir])
      case "/":
        ndir = np.flip(dirc)*-1
        new_live.append([pos+ndir, ndir])
      case _:
        assert(False)
  live = new_live
  print(show(clean_grid))
  print()
  print(live)
  print()

print(np.sum(clean_grid))
