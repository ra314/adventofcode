myfile = open("input2.txt")
content = myfile.read()

import re
import numpy as np
keys = re.findall(r'[a-z]', content)
content = content.splitlines()

def generate_adjacents(coordinate, grid_size):
  coordinate = np.array(coordinate)
  adjacents = []
  for diff in np.array([[0,1],[1,0],[0,-1],[-1,0]]):
    adjacents.append(coordinate + diff)
  # Remove coordinates that are out of grid
  adjacents = list(filter(lambda x: x[0]>=0 and x[0]<grid_size[0] and x[1]>=0 and x[1]<grid_size[1], adjacents)) 
  return list(map(tuple, adjacents))

grid_size = [len(content), len(content[0])]
def generate_adjacent_nodes(node):
  global grid_size, content
  nodes = []
  for coordinate in generate_adjacents(node[0], grid_size):
    curr_cell = content[coordinate[0]][coordinate[1]]
    # Skip if it's a wall
    if curr_cell == "#":
      continue
    if curr_cell.isalpha():
      if curr_cell.isupper():
        # Skip if you arrive at a door that you don't have a key for
        if curr_cell.lower() not in node[1]:
          continue
      else:
        # If you arrive at a new key, add it to your collection
        if curr_cell not in node[1]:
          nodes.append((coordinate, node[1]+tuple(curr_cell), node[2]+1))
          continue
    nodes.append((coordinate, node[1], node[2]+1))
  return nodes

def find_start(content):
  for i in range(len(content)):
    for j in range(len(content[0])):
      if content[i][j] == '@':
        return tuple([i,j])
  return None

from collections import deque
from random import randint
def bfs():
  global content, keys
curr_coordinate = find_start(content)
bfs_queue = deque()
bfs_queue.append((curr_coordinate, (), 0))
visited_nodes = set()

while bfs_queue:
  if randint(1, 10000) == 10000:
    print(len(visited_nodes), len(bfs_queue))
  curr_node = bfs_queue.popleft()
  for node in generate_adjacent_nodes(curr_node):
    if node[:2] in visited_nodes:
      continue
    visited_nodes.add(node[:2])
    bfs_queue.append(node)
      if len(keys) == len(node[1]):
        return node[2]

print(bfs())
        
