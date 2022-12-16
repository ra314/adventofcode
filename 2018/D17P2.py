import numpy as np
import re
from itertools import chain

myfile = open("input.txt")
content = myfile.read()

###Parsing
# Find the size of the grid
ys = []
xs = []
ys.extend(list(map(int, re.findall(r"y=(\d+)", content))))
xs.extend(list(map(int, re.findall(r"x=(\d+)", content))))
ys.extend(list(map(int, re.findall(r"y=\d+\.\.(\d+)", content))))
xs.extend(list(map(int, re.findall(r"x=\d+\.\.(\d+)", content))))

grid = np.zeros((max(ys)+2, max(xs)+2))

# Populating the grid
from enum import Enum
class TileType(Enum):
  SAND = 0
  CLAY = 1
  WATER = 2

def tile_num_to_char(num):
  if num == 0:
    return "."
  elif num == 1:
    return "#"
  else:
    return "+"

grid[0, 500] = TileType.WATER.value

def get_nums(line):
  nums = re.findall(r".*=(\d+).*=(\d+)..(\d+)", line)
  return list(map(int, nums[0]))

for line in content.splitlines():
  num1, num2, num3 = get_nums(line)
  if line[0] == 'x':
    grid[num2:num3+1, num1] = TileType.CLAY.value
  else:
    grid[num1, num2:num3+1] = TileType.CLAY.value

def print_grid(grid, to_file):
  f = open("grid.txt", "w")
  for row in grid:
    string = "".join([tile_num_to_char(num) for num in row])
    if to_file:
      f.write(string+'\n')
    else:
      print(string)
  f.close()

# Simulation
step = 0
active_points = set([(0,500)])

def is_layer_settled(point):
  global grid
  # First find the left most and right most water in this layer of settled water
  l = r = point[1]
  while grid[point[0], l] == TileType.WATER.value:
    l -= 1
    if not 0 <= l < grid.shape[1]:
      break
  l += 1
  while grid[point[0], r] == TileType.WATER.value:
    r += 1
    if not 0 <= r < grid.shape[1]:
      break
  r -= 1
  
  # Check the tiles to the left and right of the left most and right most water tile
  # Are both clay tiles
  if l-1 < 0 or r+1 >= grid.shape[1]:
    return None
  if (grid[point[0],l-1] == TileType.CLAY.value) and \
    (grid[point[0],r+1] == TileType.CLAY.value):
    return l, r
  return None

def process_point(point):
  global grid
  retval = set()
  
  # If the point is at the max y value, then return
  if point[0] == max(ys):
    return retval
  
  # If the tile below is sand
  if grid[point[0]+1,point[1]] == TileType.SAND.value:
    grid[point[0]+1,point[1]] = TileType.WATER.value
    retval.add((point[0]+1, point[1]))
    
  # If the tile below is clay
  elif grid[point[0]+1,point[1]] == TileType.CLAY.value:
    # If sand on right, add water
    if grid[point[0],point[1]+1] == TileType.SAND.value:
      grid[point[0],point[1]+1] = TileType.WATER.value
      retval.add((point[0],point[1]+1))
    # If sand on left, add water
    if grid[point[0],point[1]-1] == TileType.SAND.value:
      grid[point[0],point[1]-1] = TileType.WATER.value
      retval.add((point[0],point[1]-1))
  
  # If the tile below is water
  elif grid[point[0]+1,point[1]] == TileType.WATER.value:
    # Check if the layer below me is settled
    if is_layer_settled((point[0]+1, point[1])):
      # If sand on right, add water
      if grid[point[0],point[1]+1] == TileType.SAND.value:
        grid[point[0],point[1]+1] = TileType.WATER.value
        retval.add((point[0],point[1]+1))
      # If sand on left, add water
      if grid[point[0],point[1]-1] == TileType.SAND.value:
        grid[point[0],point[1]-1] = TileType.WATER.value
        retval.add((point[0],point[1]-1))
    
  # If there were no tiles added and the tile below is water or clay,
  # that means the water at this layer might have setteled
  if not retval:
    lr = is_layer_settled((point[0], point[1]))
    if lr:
      l, r = lr
      # Add all water tiles directly above this layer to the active set
      for x in range(l,r+1):
        if grid[point[0]-1, x] == TileType.WATER.value:
          retval.add((point[0]-1,x))
  
  return retval

from random import randrange
while active_points:
  #print_grid(grid[:,494:508], False)
  #print(active_points)
  #print()
  if randrange(1,1000) == 1:
    print(len(active_points))
  
  new_points = set()
  for point in active_points:
    new_points.update(process_point(point))
  active_points = new_points
  
  if step >= 100000:
    break
  step += 1

print(np.sum(grid[min(ys):max(ys)+1]==TileType.WATER.value))
print_grid(grid, True)

### Removing non stationary water
for point in np.argwhere(grid==TileType.WATER.value):
  lr = is_layer_settled(point)
  if not lr:
    grid[point[0], point[1]] = TileType.SAND.value

print(np.sum(grid==TileType.WATER.value))
