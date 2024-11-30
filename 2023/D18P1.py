import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
from skimage.morphology import flood_fill


f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

L = (0,-1)
R = (0,1)
U = (-1,0)
D = (1,0)
dir_map = {"L": L, "R": R, "U": U, "D": D}

def show(grid):
  return "\n".join(["".join([str(int(x)) for x in line]) for line in grid])

boundary = set()
curr = (0,0)
boundary.add(curr)
for line in content.splitlines():
  dirc, dist, _ = line.split()
  dist = int(dist)
  dirc = dir_map[dirc]
  for i in range(dist):
    curr = tuple(np.array(curr) + np.array(dirc))
    boundary.add(curr)

ys = [yx[0] for yx in boundary]
xs = [yx[1] for yx in boundary]
x = max(xs)-min(xs)+5
y = max(ys)-min(ys)+5
ymin = min(ys)
xmin = min(xs)
minn = np.array([ymin, xmin])

grid = np.zeros((y,x))
for cell in boundary:
  grid[tuple(np.array(cell)-minn)] = 1
grid = np.pad(grid, 1)
print(show(grid))

new_grid = flood_fill(grid, (0, 0), 2)
print(show(new_grid))
print(np.sum(new_grid==1)+np.sum(new_grid==0))
