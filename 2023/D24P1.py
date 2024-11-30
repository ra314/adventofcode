import sympy
from sympy import Point3D
from sympy.geometry import Ray3D, intersection
import re

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

rays = []
for line in content.splitlines():
  x1, y1, z1, x2, y2, z2 = re.findall(r'-?\d+', line)
  rays.append(Ray3D(Point3D(x1, y1, z1), Point3D(x2, y2, z2)))

count = 0
for i, r1 in enumerate(rays):
  for j, r2 in enumerate(rays):
    if i == j: continue
    if intersection(r1, r2):
      count += 1

print(count)
