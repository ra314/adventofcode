import reader
content = reader.read()

import numpy as np
content = content.replace(".", "0")
grid = np.array([list(map(int, line)) for line in content.splitlines()])

def score_trailhead(position: tuple[int, int], grid: np.ndarray) -> int:
  assert(grid[position[1]][position[0]] == 0)
  curr = [position]
  found_9 = False
  while True:
    frontier = set()
    for x, y in curr:
      value = grid[y, x]
      # Find adjacent positions, if they are in the grid
      for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < grid.shape[1] and 0 <= ny < grid.shape[0]:
          new_value = grid[ny, nx]
          if new_value == value+1:
            if new_value == 9:
              found_9 = True
            frontier.add((nx, ny))
    curr = frontier
    if found_9:
      return len(curr)
    if not frontier:
      break
  assert(False)

def find_total_score(grid: np.ndarray) -> int:
  total = 0
  maxy, maxx = grid.shape
  for y in range(maxy):
    for x in range(maxx):
      if grid[y, x] == 0:
        score = score_trailhead((x, y), grid)
        print(f"Score for {x, y}: {score}")
        total += score
  return total

#print(score_trailhead((4, 0), grid))
print(find_total_score(grid))
