import re
import numpy as np
from copy import copy
myfile = open("input.txt")
content = myfile.read().splitlines()

cubes = set()

for line in content:
  cubes.add(eval("("+line+")"))
assert(len(content)==len(cubes))
open_faces = len(cubes)*6

# Find any touching faces
for cube in cubes:
  x,y,z = cube
  if (x-1,y,z) in cubes:
    open_faces -= 1
  if (x+1,y,z) in cubes:
    open_faces -= 1
  if (x,y-1,z) in cubes:
    open_faces -= 1
  if (x,y+1,z) in cubes:
    open_faces -= 1
  if (x,y,z-1) in cubes:
    open_faces -= 1
  if (x,y,z+1) in cubes:
    open_faces -= 1

print(open_faces)
