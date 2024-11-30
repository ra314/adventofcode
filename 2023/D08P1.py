import numpy as np
from collections import defaultdict
from collections import Counter
import re
import itertools
from math import inf

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

curr = "AAA"
count = 0
for char in itertools.cycle(list(dirs)):
  count += 1
  if char == "L":
    curr = graph[curr][0]
  else:
    curr = graph[curr][1]
  if curr == "ZZZ":
    break

print(count)
