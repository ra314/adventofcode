import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
from skimage.morphology import flood_fill


f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f1.read()

L = (0,-1)
R = (0,1)
U = (-1,0)
D = (1,0)
dir_map = [R,D,L,U]
dir_map_og = {"L": L, "R": R, "U": U, "D": D}

hor_slices = defaultdict(list)
vert_slices = defaultdict(list)
curr = (0,0)
for line in content.splitlines():
  nline = line.split()[-1][1:-1]
  dirc = dir_map[int(nline[-1])]
  dist = int(nline[1:-1], 16)
  
  dirc = dir_map_og[line.split()[0]]
  dist = int(line.split()[1])
  
  end = tuple(np.array(curr)+(dist*np.array(dirc)))
  if dirc == R or dirc == L:
    hor_slices[curr[0]].append((curr[1], curr[1]+(dist*dirc[1])))
  else:
    vert_slices[curr[1]].append((curr[0], curr[0]+(dist*dirc[0])))
  curr = end

print(hor_slices)
print(vert_slices)
boundary_size = 0
for dic in [hor_slices, vert_slices]:
  for value in dic.values():
    for slicee in value:
      boundary_size += max(slicee)-min(slicee)


