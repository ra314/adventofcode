ROCK = 0
WET = 1
NARROW = 2

content = open("input.txt").read().splitlines()

import re
DEPTH = int(content[0].split()[-1])
x = re.search(r'(\d+),(\d+)', content[1])
# Target is in form y, x
TARGET = (int(x[1]), int(x[2]))[::-1]
GRID_SIZE = (TARGET[0]+100, TARGET[1]+100)

import numpy as np
geologic_index = np.zeros(GRID_SIZE, dtype=np.uint64)
erosion_level = np.zeros(GRID_SIZE, dtype=np.uint64)
risk_level = np.zeros(GRID_SIZE, dtype=np.uint64)

# Initialize geologic index
geologic_index[0] = np.arange(GRID_SIZE[1]) * 16807
geologic_index[:,0] = np.arange(GRID_SIZE[0]) * 48271
# Initialize erosion level
erosion_level[0] = (geologic_index[0] + DEPTH) % 20183
erosion_level[:,0] = (geologic_index[:,0] + DEPTH) % 20183

# Iteratively calculating erosion level and geologic index
for y in range(1,GRID_SIZE[0]):
  for x in range(1,GRID_SIZE[1]):
    # Assertion to check if we're using uninitialised erosion level values
    # assert(erosion_level[y][x-1] != 0)
    # assert(erosion_level[y-1][x] != 0)
    
    if (y,x) != TARGET:
      geologic_index[y][x] = erosion_level[y][x-1] * erosion_level[y-1][x]
    erosion_level[y][x] = (geologic_index[y][x] + DEPTH) % 20183

risk_level = erosion_level%3

from dijkstar import Graph, find_path
graph = Graph()

# For every region in the map, we add 3 nodes
# 1: Where you equip torch
# 2: Where you equip climbing gear
# 3: Where you equip neither
valid_equip = {ROCK: ["C","T"], WET: ["C","N"], NARROW: ["T","N"]}
for y in range(GRID_SIZE[0]):
  for x in range(GRID_SIZE[1]):
    RL = risk_level[y][x]
    for equipment in valid_equip[RL]:
      graph.add_node(f'Y={y};X={x};{equipment}')
    # Add transitions between equipment
    e1, e2 = valid_equip[RL]
    graph.add_edge(f'Y={y};X={x};{e1}', f'Y={y};X={x};{e2}', 7)
    graph.add_edge(f'Y={y};X={x};{e2}', f'Y={y};X={x};{e1}', 7)

def generate_adjacents(coordinate):
  coordinate = np.array(coordinate)
  adjacents = []
  for x in np.array([[1,0],[0,1],[-1,0],[0,-1]]):
    adjacents.append(coordinate + x)
  # Remove coordinates that are out of grid
  adjacents = list(filter(lambda x: x[0]>=0 and x[0]<GRID_SIZE[0] and x[1]>=0 and x[1]<GRID_SIZE[1], adjacents))
  return adjacents

# Add transitions between adjacent regions
for y in range(GRID_SIZE[0]):
  for x in range(GRID_SIZE[1]):
    for adjacent in generate_adjacents((y,x)):
      y2, x2 = adjacent
      for equipment in ["T", "C", "N"]:
        name1 = f'Y={y};X={x};{equipment}'
        name2 = f'Y={y2};X={x2};{equipment}'
        if name1 in graph and name2 in graph:
          graph.add_edge(name1, name2, 1)
          graph.add_edge(name2, name1, 1)

start = 'Y=0;X=0;T'
end = f'Y={TARGET[0]};X={TARGET[1]};T'
print(find_path(graph, start, end))

def num_to_char(num):
  if num == ROCK:
    return "."
  elif num == WET:
    return "="
  elif num == NARROW:
    return "|"
  assert(False)

def print_risk_level(grid):
  for line in grid:
    print("".join(map(num_to_char, line)))


