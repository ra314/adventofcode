import reader
content = reader.read()

import numpy as np
grid = np.array([list(line) for line in content.splitlines()])
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
while next_loc[0] >= 0 and next_loc[1] >= 0 and next_loc[0] < grid.shape[0] and next_loc[1] < grid.shape[1]:
  if grid[next_loc[0]][next_loc[1]] == '#':
    curr_dir = get_next_dir()
  else:
    curr_loc = next_loc
    grid[curr_loc[0]][curr_loc[1]] = 'X'
  next_loc = get_next_loc(curr_loc, curr_dir)

print(len(grid[grid == 'X']))
