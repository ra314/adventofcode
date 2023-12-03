import re
from itertools import cycle
c = cycle
myfile = open("input2.txt")
content = myfile.read()

direcs = {"R":(0,1),"D":(1,0),"L":(0,-1),"U":(-1,0)}
path = content.split("\n\n")[1].strip()
field = content.split("\n\n")[0].splitlines()
# Whitespace padding
biggest_row = max([len(row) for row in field])
for i, row in enumerate(field):
  if len(row) < biggest_row:
    field[i] = row + (" "*(biggest_row-len(field[i])))
# Turning each point into a node
grid = []
for y, row in enumerate(field):
  new_row = []
  for x, char in enumerate(row):
    if char == " ":
      new_row.append(None)
    else:
      # Node consists of neighbour x, y and direction change
      node = {}
      for d_name, direc in direcs.items():
        dy, dx = direc
        ny, nx = dy+y, dx+x
        if ny<len(field) and nx<len(field[ny]) and field[ny][nx] != " ":
          node[d_name] = (ny,nx, d_name)
      new_row.append(node)
  grid.append(new_row)

# Go around the cube in all 3 loopable directions
for y1, x1, y2, x2 in zip(range(0,4),c(8),c(4),range(4,8)):
  grid[y1][x1]["L"] = (y2, x2, "D")
  grid[y2][x2]["U"] = (y1, x1, "R")
for y1, x1, y2, x2 in zip(range(8,12),c(8),c(7),range(4,8)):
  grid[y1][x1]["L"] = (y2, x2, "U")
  grid[y2][x2]["D"] = (y1, x1, "R")
for y1, x1, y2, x2 in zip(range(0,4),c(12),range(12,8),c(16)):
  grid[y1][x1]["R"] = (y2, x2, "L")
  grid[y2][x2]["R"] = (y1, x1, "L")

assert(False)

sections = [((1,9),(4,12)),((5,1),(8,4)),((5,5),(8,8)),((5,9),(8,12)),((9,13),(12,16))]
sections = [((x[0][0],x[0][1]-1),(x[1][0],x[1][1]-1)) for x in sections]
# Cube map indices start at one
cube_map = {1:{0:6,2:3},2:{1:5,3:1},3:{1:5,3:1}}

s = (0,0)
while True:
  y, x = s
  if field[y][x] == ".":
    break
  s = (y,x+1)

i = 0
direc = (0, 1)

print(s, direc)
while i < len(path):
  instr = path[i]
  i += 1
  if path[i-1].isdigit():
    while i < len(path) and path[i].isdigit():
      instr += path[i]
      i += 1
  if instr.isdigit():
    num = int(instr)
    y, x = s
    dy, dx = direc
    assert(field[y][x] == ".")
    for _ in range(num):
      ny, nx = ((dy+y)%len(field),(dx+x)%len(field[0]))
      if field[ny][nx] == " ":
        while field[ny][nx] == " ":
          ny += dy
          ny %= len(field)
          nx += dx
          nx %= len(field[0])
      if field[ny][nx] == "#":
        break
      y, x = ny, nx
    s = (y,x)
  else:
    direc_index = direcs.index(direc)
    if instr == "R":
      direc_index += 1
    elif instr == "L":
      direc_index -= 1
    else:
      assert(False)
    direc_index %= len(direcs)
    direc = direcs[direc_index]
  print(s, direc, instr)

y, x = s
print(((y+1)*1000)+((x+1)*4)+direcs.index(direc))
