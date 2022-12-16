myfile = open("input.txt")
content = myfile.read()
import numpy as np

def generate_path(string):
  coord_to_num_steps = {}
  curr_coord = np.array([0,0])
  num_steps = 0
  
  dir_to_coord = {"R": (0,1), "L": (0,-1), "U": (1,0), "D": (-1,0)}
  for key, value in dir_to_coord.items():
    dir_to_coord[key] = np.array(value)
  
  for direction in string.split(','):
    distance = int(direction[1:])
    for _ in range(distance):
      num_steps += 1
      curr_coord += dir_to_coord[direction[0]]
      if tuple(curr_coord) not in coord_to_num_steps:
        coord_to_num_steps[tuple(curr_coord)] = num_steps
  
  return coord_to_num_steps

path1 = generate_path(content.splitlines()[0])
path2 = generate_path(content.splitlines()[1])

intersections = path1.keys() & path2.keys()
closest_point = min(intersections, key=lambda x: path1[x] + path2[x])
print(path1[closest_point] + path2[closest_point])
