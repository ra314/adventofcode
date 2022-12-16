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
score = np.ones((len(grid), len(grid[0])))
grid = np.array(grid)

# Ray cast from every tree to the edge of the grid
for i in range(len(grid)):
  for j in range(len(grid[0])):
    views = [grid[i,:j][::-1], grid[i, j+1:], grid[:i,j][::-1], grid[i+1:,j]]
    for view in views:
      curr_score = 0
      for x in view:
        if x < grid[i,j]:
          curr_score += 1
          curr = x
        else:
          curr_score += 1
          break
      if i == 1 and j == 2:
        print(curr_score, view)
      score[i,j] *= curr_score
    
print(np.max(score))
