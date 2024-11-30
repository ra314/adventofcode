import numpy as np
import re

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

world = np.array([])
bricks = []

for line in content.splitlines():
  x1, y1, z1, x2, y2, z2 = list(map(int, re.findall(r'(\d+),(\d+),(\d+)~(\d+),(\d+),(\d+)', line)[0]))
  bricks.append((x1, y1, z1, x2, y2, z2))

bricks = np.array(bricks)
maxx = np.max(bricks[:,(0,3)])
maxy = np.max(bricks[:,(1,4)])
maxz = np.max(bricks[:,(2,5)])
world = np.zeros((maxx+1, maxy+1, maxz+1))

def color_in_world(wrld, brick, color):
  x1, y1, z1, x2, y2, z2 = brick
  wrld[x1:x2+1,y1:y2+1,z1:z2+1] = color

for brick in bricks:
  color_in_world(world, brick, 1)

print(world)

def import_gravity():
  falling = True
  iter_count = 0 
  falling_bricks = set()
  while falling:
    iter_count += 1
    falling = False
    for i in range(len(bricks)):
      x1, y1, z1, x2, y2, z2 = bricks[i]
      # If on ground, stop
      if z1 == 1 or z2 == 1: continue
      # Remove yourself from the world
      color_in_world(world, bricks[i], 0)
      z1 -= 1
      z2 -= 1
      # Check if the points underneath are occupied
      if np.sum(world[x1:x2+1,y1:y2+1,z1:z2+1]) != 0: 
        # Add yourself back into the world in the same position
        color_in_world(world, bricks[i], 1)
        continue
      falling = True
      # Add yourself back into the world in the new position
      bricks[i] -= np.array([0,0,1,0,0,1])
      falling_bricks.add(i)
      color_in_world(world, bricks[i], 1)
  return iter_count, len(falling_bricks)

import_gravity()

count = 0
fellers = []
for i in range(len(bricks)):
  backup_world = np.copy(world)
  backup_bricks = np.copy(bricks)
  color_in_world(world, bricks[i], 0) 
  bricks = np.delete(bricks, i, 0)
  iter_count, num_fell = import_gravity()
  fellers.append(num_fell)
  print(iter_count, i, num_fell)
  if iter_count == 1:
    count += 1
  world = backup_world
  bricks = backup_bricks
  color_in_world(world, bricks[i], 1)

print(sum(fellers))


