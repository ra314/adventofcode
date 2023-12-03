import re
myfile = open("input.txt")
content = myfile.read()

path = content.split("\n\n")[1].strip()
field = content.split("\n\n")[0].splitlines()
biggest_row = max([len(row) for row in field])
for i, row in enumerate(field):
  if len(row) < biggest_row:
    field[i] = row + (" "*(biggest_row-len(field[i])))

s = (0,0)
while True:
  y, x = s
  if field[y][x] == ".":
    break
  s = (y,x+1)

i = 0
direc = (0, 1)
direcs = [(0,1),(1,0),(0,-1),(-1,0)]
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
    assert(field[y][x] == ".")
    for _ in range(num):
      dy, dx = direc
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
