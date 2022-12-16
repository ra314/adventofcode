content = open("input2.txt").read().splitlines()

import re
DEPTH = int(content[0].split()[-1])
x = re.search(r'(\d+),(\d+)', content[1])
# Target is in form y, x
TARGET = (int(x[1]), int(x[2]))[::-1]
GRID_SIZE = (TARGET[0]+1, TARGET[1]+1)

import numpy as np
geologic_index = np.zeros(GRID_SIZE, dtype=np.uint64)
erosion_level = np.zeros(GRID_SIZE, dtype=np.uint64)
risk_level = np.zeros(GRID_SIZE, dtype=np.uint64)

# Initialize geologic index
geologic_index[0] = np.arange(TARGET[1]+1) * 16807
geologic_index[:,0] = np.arange(TARGET[0]+1) * 48271
# Initialize erosion level
erosion_level[0] = (geologic_index[0] + DEPTH) % 20183
erosion_level[:,0] = (geologic_index[:,0] + DEPTH) % 20183

# Iteratively calculating erosion level and geologic index
for y in range(1,TARGET[0]+1):
  for x in range(1,TARGET[1]+1):
    # Assertion to check if we're using uninitialised erosion level values
    assert(erosion_level[y][x-1] != 0)
    assert(erosion_level[y-1][x] != 0)
    
    if (y,x) != TARGET:  
      geologic_index[y][x] = erosion_level[y][x-1] * erosion_level[y-1][x]
    erosion_level[y][x] = (geologic_index[y][x] + DEPTH) % 20183

risk_level = erosion_level%3

print(np.sum(risk_level))
