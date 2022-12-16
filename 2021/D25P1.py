myfile = open("input2.txt")
content = myfile.read()
from copy import deepcopy

grid = []
for line in content.splitlines():
  grid.append(list(line))

def create_empty_grid(rows, cols):
  new_grid = []
  for i in range(rows):
    new_grid.append(list("."*cols))
  return new_grid

cols = len(grid[0])
rows = len(grid)

has_moved = True
iters = 0
while has_moved:
  has_moved = False
  new_grid = deepcopy(grid)
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == ">":
        if grid[i][(j+1)%cols] == ".":
          has_moved = True
          new_grid[i][(j+1)%cols] = ">"
          new_grid[i][j] = "."
  grid = new_grid
  new_grid = deepcopy(grid)
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == "v":
        if grid[(i+1)%rows][j] == ".":
          has_moved = True
          new_grid[(i+1)%rows][j] = "v"
          new_grid[i][j] = "."
  grid = new_grid
  iters += 1
  # print(iters)
  # print("\n".join(["".join(row) for row in grid]))

print(iters)
