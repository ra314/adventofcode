content = 361527

import numpy as np
grid = np.zeros((11,11)).astype('int')
curr_coordinate = (5,5)
grid[curr_coordinate] = 1

def generate_adjacents(coordinate):
    adjacents = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            adjacents.append(coordinate + np.array([i,j]))
    # Remove coordiantes that are out of grid
    adjacents = list(filter(lambda x: x[0]>=0 and x[0]<grid.shape[0] and x[1]>=0 and x[1]<grid.shape[1], adjacents)) 
    return adjacents

print(generate_adjacents(curr_coordinate))

curr_coordinate = (6,6)
spiral_length = 2
while np.max(grid) < content:
  for i in range(4):
    for j in range(spiral_length):
      if i == 0:
        curr_coordinate = (curr_coordinate[0]-1, curr_coordinate[1])
      elif i == 1:
        curr_coordinate = (curr_coordinate[0], curr_coordinate[1]-1)
      if i == 2:
        curr_coordinate = (curr_coordinate[0]+1, curr_coordinate[1])
      if i == 3:
        curr_coordinate = (curr_coordinate[0], curr_coordinate[1]+1)
        
      next_num = 0
      for adjacent in generate_adjacents(curr_coordinate):
        next_num += grid[tuple(adjacent)]
      grid[curr_coordinate] = next_num
  curr_coordinate = (curr_coordinate[0]+1, curr_coordinate[1]+1)
  spiral_length += 2

print(np.min(grid[grid>content].flatten()))
