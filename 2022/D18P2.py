# num, frm, to = list(map(int, re.search(r'move (?\-\d+) from (\d+) to (\d+)', line).groups()))
# from dijkstar import Graph, find_path
# graph = Graph()
# graph.add_edge(node1, node2, weight)
# path = find_path(graph, create_node_name((0,0)), create_node_name(np.array(array.shape)-1))

import re
import numpy as np
from copy import copy
myfile = open("input.txt")
content = myfile.read().splitlines()

cubes = set()

for line in content:
  cubes.add(eval("("+line+")"))
assert(len(content)==len(cubes))
open_faces = 0

min_val = min(min(cubes, key=lambda x: min(x)))-1
max_val = max(max(cubes, key=lambda x: max(x)))+1
start = (min_val,min_val,min_val)
processed = set()
to_process = [start]
# Do a 3d flood fill to find the faces that can be touched externally.
while to_process:
  curr = to_process.pop()
  if min(curr)<min_val:
    continue
  if max(curr)>max_val:
    continue
  x,y,z = curr
  for new in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
    if new in processed:
      continue
    if new in cubes:
      print(curr, new)
      open_faces += 1
      continue
    processed.add(new)
    to_process.append(new)

print(open_faces)
