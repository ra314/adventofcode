myfile = open("input.txt")
content = myfile.read()

content = [list(line) for line in content.splitlines()]
grid_size = [len(content), len(content[0])]

import numpy as np
def generate_adjacents(coordinate, grid_size):
  coordinate = np.array(coordinate)
  adjacents = []
  for diff in np.array([[0,1],[1,0],[0,-1],[-1,0]]):
    adjacents.append(coordinate + diff)
  # Remove coordinates that are out of grid
  adjacents = list(filter(lambda x: x[0]>=0 and x[0]<grid_size[0] and x[1]>=0 and x[1]<grid_size[1], adjacents)) 
  return list(map(tuple, adjacents))

def get_adjacent_count(coordinate):
  global grid_size, content
  count = 0
  for coordinate in generate_adjacents(coordinate, grid_size):
    count += content[coordinate[0]][coordinate[1]] == '#'
  return count

def get_new_state(coordinate):
  global content
  curr_char = content[coordinate[0]][coordinate[1]]
  count = get_adjacent_count(coordinate)
  if curr_char == "#":
    if count == 1:
      return "#"
    else:
      return "."
  else:
    if count == 1 or count == 2:
      return "#"
    else:
      return "."

def simulate():
  global content
  new_content = [['' for _ in range(5)] for _ in range(5)]
  for i in range(5):
    for j in range(5):
      new_content[i][j] = get_new_state((i,j))
  return new_content

def draw(content):
  return ("\n".join(list(map(lambda x: "".join(x), content))))

def evaluate(content):
  retval = 0
  for i, char in enumerate(draw(content).replace("\n","")):
    if char == "#":
      retval += 2**i
  return retval

prev_states = set()

hash_rep = draw(content).replace("\n","")
while hash_rep not in prev_states:
  prev_states.add(hash_rep)
  content = simulate()
  hash_rep = draw(content).replace("\n","")

print(draw(content))
print(evaluate(content))
