myfile = open("input.txt")
content = myfile.read()
import numpy as np

def generate_path(string):
  path = set()
  curr_coord = np.array([0,0])
  
  dir_to_coord = {"R": (0,1), "L": (0,-1), "U": (1,0), "D": (-1,0)}
  for key, value in dir_to_coord.items():
    dir_to_coord[key] = np.array(value)
  
  for direction in string.split(','):
    distance = int(direction[1:])
    for _ in range(distance):
      curr_coord += dir_to_coord[direction[0]]
      path.add(tuple(curr_coord))
  
  return path

path1 = generate_path(content.splitlines()[0])
path2 = generate_path(content.splitlines()[1])

intersections = path1.intersection(path2)
closest_point = min(intersections, key=lambda x: abs(np.array(x)).sum())
print(abs(np.array(closest_point)).sum())
