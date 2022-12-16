myfile = open("input2.txt")
content = myfile.read()

import numpy as np

grid = content.splitlines()
grid = np.array(list(map(lambda x: [0 if char == '.' else 1 for char in x], grid)))

def generate_adjacents(coordinate):
    adjacents = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            adjacents.append(coordinate + np.array([i,j]))
    # Remove coordiantes that are out of grid
    adjacents = list(filter(lambda x: x[0]>=0 and x[0]<grid.shape[0] and x[1]>=0 and x[1]<grid.shape[1], adjacents)) 
    return adjacents

def process_tile(coordinate):
  adjacent_coordinates = generate_adjacents(coordinate)
  num_adjacent_on = 0
  for adjacent in adjacent_coordinates:
    num_adjacent_on += grid[adjacent[0], adjacent[1]]
  if grid[coordinate]:
    return 1 if num_adjacent_on in [2,3] else 0
  else:
    return 1 if num_adjacent_on == 3 else 0

for i in range(100):
  print(i)
  new_grid = np.zeros(grid.shape)
  for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
      coordinate = (x,y)
      new_grid[coordinate[0], coordinate[1]] = process_tile(coordinate)
  grid = new_grid
  grid[0,0] = 1
  grid[0,grid.shape[1]-1] = 1
  grid[grid.shape[0]-1,0] = 1
  grid[grid.shape[0]-1,grid.shape[1]-1] = 1

print(int(np.sum(grid)))
