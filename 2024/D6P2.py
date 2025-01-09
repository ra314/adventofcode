import reader
content = reader.read()
import numpy as np

def does_loop(grid) -> bool:
  curr = np.where(grid == '^')
  curr_loc = (int(curr[0][0]), int(curr[1][0]))
  grid[curr_loc[0]][curr_loc[1]] = '.'
  curr_dir = (-1, 0)
  dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
  def get_next_dir():
    return dirs[(dirs.index(curr_dir)+1)%len(dirs)]

  def get_next_loc(loc, dir):
    return (loc[0] + dir[0], loc[1] + dir[1])

  next_loc = get_next_loc(curr_loc, curr_dir)
  visited = set()
  while next_loc[0] >= 0 and next_loc[1] >= 0 and next_loc[0] < grid.shape[0] and next_loc[1] < grid.shape[1]:
    key = (curr_loc, curr_dir)
    if key in visited:
      return True
    visited.add(key)
    
    if grid[next_loc[0]][next_loc[1]] == '#':
      curr_dir = get_next_dir()
    else:
      curr_loc = next_loc
      grid[curr_loc[0]][curr_loc[1]] = 'X'
    next_loc = get_next_loc(curr_loc, curr_dir)

  return False

og_grid = np.array([list(line) for line in content.splitlines()])
x, y = og_grid.shape

loop_count = 0
for i in range(x):
  for j in range(y):
    if og_grid[i][j] == '.':
      grid = og_grid.copy()
      grid[i][j] = '#'
      if does_loop(grid):
        loop_count += 1
        print((i, j))

print(loop_count)
