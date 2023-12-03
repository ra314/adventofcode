import re
myfile = open("input.txt")
content = myfile.read().splitlines()

elves = set()
for y, line in enumerate(content):
  for x, char in enumerate(line):
    if char == "#":
      elves.add((y,x))

deltas = [((-1,-1),(-1,0),(-1,1)),((1,-1),(1,0),(1,1)),((-1,-1),(0,-1),(1,-1)),((-1,1),(0,1),(1,1))]

from collections import defaultdict

def print_elves(elves):
  ys = [elf[0] for elf in elves]
  xs = [elf[1] for elf in elves]
  if min(ys)<0:
    elves = [(y+abs(min(ys)),x) for y,x in elves]
  if min(xs)<0:
    elves = [(y,x+abs(min(xs))) for y,x in elves]
  ys = [elf[0] for elf in elves]
  xs = [elf[1] for elf in elves]
  grid = ""
  for y in range(max(ys)+1):
    row = ""
    for x in range(max(xs)+1):
      if (y,x) in elves:
        row += "#"
      else:
        row += "."
    grid += row + "\n"
  return grid

def is_open(delta, elf):
  y, x = elf
  for dy, dx in delta:
    if (y+dy,x+dx) in elves:
      return False
  return True

def is_near_elf(elf, elves):
  y, x = elf
  for dy in (-1,0,1):
    for dx in (-1,0,1):
      if dy==0 and dx==0: continue
      if (y+dy,x+dx) in elves:
        return True
  return False

print(print_elves(elves))
for _ in range(10):
  wanted_tiles = defaultdict(int)
  curr_tile_next_tile = []
  for elf in elves:
    if not is_near_elf(elf, elves):
      continue
    y, x = elf
    for delta in deltas:
      if is_open(delta, elf):
        dy, dx = delta[1]
        destination = (y+dy,x+dx)
        wanted_tiles[destination] += 1
        curr_tile_next_tile.append((elf, destination))
        break
  for curr, next in curr_tile_next_tile:
    assert(wanted_tiles[next]!=0)
    if wanted_tiles[next]==1:
      elves.remove(curr)
      elves.add(next)
  print(print_elves(elves))
  deltas.append(deltas.pop(0))

# Bounding box
ys = [elf[0] for elf in elves]
xs = [elf[1] for elf in elves]
num_elves = len(elves)
height = (max(ys)-min(ys))+1
width = (max(xs)-min(xs))+1
box_size = width*height
print(box_size, num_elves, box_size-num_elves)
