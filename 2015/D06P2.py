myfile = open("input2.txt")
content = myfile.read()

import numpy as np
grid = np.zeros((1000, 1000))

for line in content.splitlines():
  line = line.split()
  xs = line[-3].split(',')
  x1, x2 = list(map(int, xs))
  ys = line[-1].split(',')
  y1, y2 = list(map(int, ys))
  y1 += 1
  y2 += 1
  if line[0] == "toggle":
    grid[x1:y1, x2:y2] += 2
  elif line[0] == "turn" and line[1] == "on":
    grid[x1:y1, x2:y2] += 1
  elif line[0] == "turn" and line[1] == "off":
    grid[x1:y1, x2:y2] -= 1
    grid[grid<0] = 0
  else:
    print("exceptino")
print(int(np.sum(grid)))
