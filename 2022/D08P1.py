# num, frm, to = list(map(int, re.search(r'move (\d+) from (\d+) to (\d+)', line).groups()))
# from dijkstar import Graph, find_path
# graph = Graph()
# graph.add_edge(node1, node2, weight)
# path = find_path(graph, create_node_name((0,0)), create_node_name(np.array(array.shape)-1))

import re
myfile = open("input.txt")
content = myfile.read()

grid = []
for line in content.splitlines():
  grid.append([int(x) for x in line])

import numpy as np
seen = np.zeros((len(grid), len(grid[0])))
grid = np.array(grid)

# Ray cast from every tree to the edge of the grid
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
      seen[i,j] = 1
      continue
    views = [grid[i,:j], grid[i, j+1:], grid[:i,j], grid[i+1:,j]]
    for view in views:
      if np.all(grid[i,j]>view):
        seen[i,j] = 1
        break
    
print(int(np.sum(seen)))
