myfile = open("input2.txt")
content = myfile.read()

import numpy as np
pos = np.array([0,0])
direction = np.array([1,0])

def rotate_dir(direction):
  if (direction == [1,0]).all():
    return np.array([0,1])
  if (direction == [0,1]).all():
    return np.array([-1,0])
  if (direction == [-1,0]).all():
    return np.array([0,-1])
  if (direction == [0,-1]).all():
    return np.array([1,0])

for step in content[:-1].split(", "):
  if "R" in step:
    direction = rotate_dir(direction)
  else:
    for i in range(3):
      direction = rotate_dir(direction)
  pos += (direction * int(step[1:]))
  
print(abs(pos).sum())
