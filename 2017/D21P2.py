import numpy as np
from math import sqrt

myfile = open("input.txt")
content = myfile.read()
seed = np.array([[0,1,0],[0,0,1],[1,1,1]])

def pattern_to_num(pattern):
  return pattern.replace('/', '').replace('.', '0').replace('#', '1')

rules = {}
for line in content.splitlines():
  input_pattern = line.split('=>')[0].split()[0]
  output_pattern = line.split('=>')[1].split()[0]
  rules[pattern_to_num(input_pattern)] = pattern_to_num(output_pattern)

def array_to_str(array):
  return "".join(list(map(str, array.flatten().astype('int'))))

def find_pattern(array):
  for i in range(4):
    curr_array = np.rot90(array, i)
    if array_to_str(curr_array) in rules:
      return rules[array_to_str(curr_array)]
    if array_to_str(np.flip(curr_array, 1)) in rules:
      return rules[array_to_str(np.flip(curr_array, 1))]
    if array_to_str(np.flip(curr_array, 0)) in rules:
      return rules[array_to_str(np.flip(curr_array, 0))]

def str_to_array(string):
  size = int(sqrt(len(string)))
  return np.array(list(map(int, string))).reshape((size, size))

def enhance(seed):
  if len(seed)%2 == 0:
    new_grid = np.zeros((len(seed)+len(seed)//2, len(seed)+len(seed)//2))
    for i in range((len(seed)//2)):
      for j in range((len(seed)//2)):
        new_grid[i*3:(i+1)*3, j*3:(j+1)*3] = str_to_array(find_pattern(seed[i*2:(i+1)*2, j*2:(j+1)*2]))
    return new_grid
  else:
    new_grid = np.zeros((len(seed)+len(seed)//3, len(seed)+len(seed)//3))
    for i in range((len(seed)//3)):
      for j in range((len(seed)//3)):
        new_grid[i*4:(i+1)*4, j*4:(j+1)*4] = str_to_array(find_pattern(seed[i*3:(i+1)*3, j*3:(j+1)*3]))
    return new_grid

def print_pretty(array):
  string = ""
  for row in array:
    string += "".join(list(map(lambda x: "." if x == 0 else "#", row)))
    string += "\n"
  return string

for i in range(18):
  seed = enhance(seed)
  print(i)
  print(print_pretty(seed))
