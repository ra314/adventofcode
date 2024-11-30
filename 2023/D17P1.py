import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
import itertools
from math import inf
import itertools
from dataclasses import dataclass

@dataclass
class Node:
  pos: tuple
  prev: tuple
  dirc: tuple
  cost: int
  
  def __eq__(self, other): 
    return self.pos == other.pos and self.prev == other.prev and self.dirc == other.dirc
  
  def __hash__(self):
    return hash((self.pos, self.prev, self.dirc))

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f1.read()
content = np.array(list(map(list, content.splitlines()))).astype(int)

L = (0,-1)
R = (0,1)
U = (-1,0)
D = (1,0)
new_dirs_map = {U: [L, R], D: [L, R], R: [U, D], L: [U, D]}

start = (0,0)
end = tuple(np.array(content.shape)-np.array([1,1]))

# TODO consider each cell along with the direction when on that cell

frontier = {}
frontier[Node(start, None, R, 0)] = 0
frontier[Node(start, None, D, 0)] = 0
processed = {}

def find_key(target):
  retval = []
  for key, value in processed.items():
    if key.pos == target:
      retval.append(key)
  return min(retval, key=lambda x: x.cost)

def get_last_n(n, key):
  retval = []
  for i in range(n):
    key = find_key(key.pos)
    if not key:
      return retval
    retval.append(key)
  return retval

def plus(x, y):
  return tuple(np.array(x) + np.array(y))

while frontier:
  node, _ = min(list(frontier.items()), key=lambda x: x[0].cost)
  del frontier[node]
  processed[node] = node.prev
  prev_2 = get_last_n(2, node)
  can_continue_in_dirc = True
  if len(prev_2) == 2:
    if prev_2[0].dirc == node.dirc and prev_2[1].dirc == node.dirc:
      can_continue_in_dirc = False
  print(can_continue_in_dirc)
  new_dirs = new_dirs_map[node.dirc].copy()
  if can_continue_in_dirc:
    new_dirs.append(node.dirc)
  for ndir in new_dirs:
    npos = plus(ndir, node.pos)
    if npos[0] < 0 or npos[1] < 0 or npos[1] >= content.shape[1] or npos[0] >= content.shape[0]:
      continue
    ncost = content[npos]+node.cost
    nnode = Node(npos, node.pos, ndir, ncost)
    if nnode in processed:
      continue
    if nnode in frontier:
      if frontier[nnode] <= ncost:
        continue
    frontier[nnode] = ncost

new_graph = np.zeros(content.shape)
curr = end
while curr != start:
  new_graph[curr] = 1
  curr = find_key(curr).prev

print(new_graph)
