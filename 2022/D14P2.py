import re, numpy as np
from collections import defaultdict
myfile = open("input.txt")
content = myfile.read().splitlines()

# 0,0 is at the top left of the grid
grid = np.zeros((1000, 1000))
floor = 0
for line in content:
  coords = line.split(" -> ")
  coords = [[int(x) for x in re.search(r'(\d+),(\d+)', coord).groups()] for coord in coords]
  for coord1, coord2 in zip(coords, coords[1:]):
    coord1, coord2 = sorted([coord1,coord2])
    x1, y1 = coord1
    x2, y2 = coord2
    floor = max(floor, y1)
    floor = max(floor, y2)
    assert(x1 == x2 or y1 == y2)
    grid[y1:y2+1, x1:x2+1] = 1

sand_source = [0, 500]
floor += 2
grid[floor] = 1

def drop_sand():
  i = 0
  cy, cx = sand_source
  if grid[cy,cx] == 2:
    print("Sand already found at source")
    assert(False)
  grid[cy,cx] = 2
  while i < 1000:
    i += 1
    dy, dx = np.array([cy,cx]) + np.array([1,0])
    dly, dlx = np.array([cy,cx]) + np.array([1,-1])
    dry, drx = np.array([cy,cx]) + np.array([1,1])
    if grid[dy, dx] == 0:
      grid[cy, cx] = 0
      grid[dy, dx] = 2
      cy, cx = dy, dx
    elif grid[dly, dlx] == 0:
      grid[cy, cx] = 0
      grid[dly, dlx] = 2
      cy, cx = dly, dlx
    elif grid[dry, drx] == 0:
      grid[cy, cx] = 0
      grid[dry, drx] = 2
      cy, cx = dry, drx
    else:
      return
  print("Sand particle dropped down for too long")
  assert(False)

def print_grid(grid):
  retval = []
  for row in grid:
    row_str = []
    for col in row:
      if col == 0:
        row_str.append(".")
      elif col == 1:
        row_str.append("#")
      elif col == 2:
        row_str.append("+")
      else:
        assert(False)
    retval.append("".join(row_str))
  return "\n".join(retval)

count = 0
while True:
  count += 1
  drop_sand()
  if count % 100 == 0:
    print(count)

print(count-1)
