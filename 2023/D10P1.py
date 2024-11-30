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

if len(content) > 200:
  s_replacement = "J"
else:
  s_replacement = "F"

heigth = len(content.splitlines())
width = len(content.splitlines()[0])
start = content.find("S")
start = (start%(width+1), start//(width+1))
content = content.replace("S", s_replacement)
content = content.splitlines()

def neighbours(char):
  match char:
    case "|":
      return [[0,-1],[0,1]]
    case "-":
      return [[-1,0],[1,0]]
    case "L":
      return [[0,-1],[1,0]]
    case "J":
      return [[0,-1],[-1,0]]
    case "7":
      return [[-1,0],[0,1]]
    case "F":
      return [[1,0],[0,1]]
    case ".":
      return []
    case _:
      assert(False)

visited = set()
nodes = deque([(start,0)])
while nodes:
  curr, dist = nodes.popleft()
  visited.add(curr)
  char = content[curr[1]][curr[0]]
  neighs = neighbours(char)
  for n in neighs:
    n = tuple(n)
    new = tuple(np.array(curr)+np.array(n))
    if new in visited: continue
    if new[0] < 0 or new[1] < 0 or new[0] >=width or new[1] >= heigth: continue
    nodes.append((new, dist+1))
  print(char, curr, dist)
