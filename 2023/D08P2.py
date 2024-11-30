import numpy as np
from collections import defaultdict
from collections import Counter
import re
import itertools
from math import inf
from math import lcm

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

dirs = content.splitlines()[0]
graph_lines = content.splitlines()[2:]
graph = {}
for line in graph_lines:
  key = line.split(" = ")[0]
  nodes = line.split(" = ")[1][1:-1].split(", ")
  graph[key] = nodes

curr_nodes = set(filter(lambda x: x[-1] == "A", list(graph.keys())))
count = 0



cache = {}
def counts_to_end(node, dir_index):
  global cache
  history = []
  count = 0
  
  while node[-1] != "Z":
    key = (node, dir_index)
    if key in cache: return cache[key]
    
    char = dirs[dir_index]
    if char == "L":
      node = graph[node][0]
    else:
      node = graph[node][1]
    dir_index += 1
    dir_index %= len(dirs)
    count += 1
    history.append((node, dir_index, count))
  
  for hist in history:
    node, dir_index, count = hist
    cache[(node, dir_index)] = count
  return count

counts = [counts_to_end(curr_node, 0) for curr_node in curr_nodes]
print(lcm(*counts))
print(counts)

