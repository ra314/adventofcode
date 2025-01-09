import reader
content = reader.read()

class Robot:
  def __init__(self, pos: tuple[int, int], vel: tuple[int, int], grid_size: tuple[int, int]):
    self.pos = pos
    self.vel = vel
    self.grid_size = grid_size
  
  def move(self):
    dx, dy = self.vel
    x, y = self.pos
    maxx, maxy = self.grid_size
    nx = (x+dx)%maxx
    ny = (y+dy)%maxy
    self.pos = (nx, ny)
  
  def quadrant(self) -> int:
    x, y = self.pos
    maxx, maxy = self.grid_size
    if x == maxx//2 or y == maxy//2:
      return 0
    if x < maxx//2 and y < maxy//2:
      return 1
    if x < maxx//2 and y > maxy//2:
      return 2
    if x > maxx//2 and y > maxy//2:
      return 3
    if x > maxx//2 and y < maxy//2:
      return 4
    assert False
  
  def __str__(self):
    return f'({self.pos[0]}, {self.pos[1]})'

from collections import defaultdict
import numpy as np
def safety_factor(robots: list[Robot]) -> int:
  robots_by_quadrant: dict[int, int] = defaultdict(int)
  for robot in robots:
    robots_by_quadrant[robot.quadrant()] += 1
  robots_by_quadrant[0] = 1
  return np.prod(list(robots_by_quadrant.values()))

def print_grid(robots: list[Robot], grid_size: tuple[int, int]):
  maxx, maxy = grid_size
  grid = np.zeros((maxy, maxx)).astype(int)
  for robot in robots:
    x, y = robot.pos
    grid[y][x] = 1
  for row in grid:
    print(''.join(["#" if cell==1 else "." for cell in row]))

def score_tightness(robots: list[Robot]) -> int:
  score = 0
  for r1 in robots:
    for r2 in robots:
      r1x, r1y = r1.pos
      r2x, r2y = r2.pos
      score += abs(r1x - r2x) + abs(r1y - r2y)
  return score

import re
robots = []
grid_size = (11, 7)
if len(content.splitlines()) > 20:
  grid_size = (101, 103)
for line in content.splitlines():
  nums = list(map(int, re.findall(r'-?\d+', line)))
  pos = nums[0], nums[1]
  vel = nums[2], nums[3]
  robot = Robot(pos, vel, grid_size)
  robots.append(robot)

from math import inf
min_score = inf
i = 0
while True:
  i += 1
  for robot in robots:
    robot.move()
  tightness_score = score_tightness(robots)
  if tightness_score < min_score:
    min_score = tightness_score
    print_grid(robots, grid_size)
    print(i)
    print()
print(safety_factor(robots))
