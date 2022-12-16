import re, numpy as np
from collections import defaultdict
myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()

grid = []
for i, line in enumerate(content):
  row = []
  for j, char in enumerate(line):
    if char.isupper():
      match char:
        case "S":
          start = (i,j)
          char = "a"
        case "E":
          end = (i,j)
          char = "z"
        case _:
          assert(False)
    row.append(ord(char)-ord('a'))
  grid.append(row)

grid = np.array(grid)

from dijkstar import Graph, find_path
graph = Graph()
for i in range(len(grid)):
  for j in range(len(grid[0])):
    for delta in np.array([[1,0],[-1,0],[0,1],[0,-1]]):
      di, dj = delta
      ni, nj = di+i, dj+j
      if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
        if abs(grid[ni,nj]-grid[i,j]) <= 1:
          graph.add_edge(f"{i},{j}", f"{ni},{nj}", 1)

si, sj = start
ei, ej = end
path = find_path(graph, f"{si},{sj}", f"{ei},{ej}")
print(path)
print(path.total_cost)
