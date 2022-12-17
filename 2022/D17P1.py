import re
import numpy as np
from copy import copy
myfile = open("input.txt")
content = myfile.read().splitlines()[0]

highest_rock_y = 0
occupied = np.zeros((20000,7))
# Set the bottom row as rocks
occupied[0] = 1

class Rock:
  def __init__(self, coords):
    self.coords = np.array(coords) + [0,2]

num_to_chr = [".", "#", "@"]

def print_scrn():
  return "\n".join(["".join([num_to_chr[int(x)] for x in row]) for row in np.flip(occupied, (0))])

rocks = []
rocks.append(Rock([(0,x) for x in range(4)]))
rocks.append(Rock([(0,1),(1,0),(1,1),(1,2),(2,1)]))
rocks.append(Rock([(2,2),(1,2),(0,0),(0,1),(0,2)]))
rocks.append(Rock([(y,0) for y in range(4)]))
rocks.append(Rock([(0,0),(0,1),(1,0),(1,1)]))

rock_index = 0
curr_jet_index = 0
for i in range(2022):
  print(i)
  curr_rock = rocks[rock_index]
  curr_coords = copy(curr_rock.coords)
  # Shift rocks upwards when adding it in
  curr_coords += [highest_rock_y+4,0]
  while True:
    # Debug prints
    #occupied[curr_coords[:,0],curr_coords[:,1]] = 2
    #print(print_scrn())
    #occupied[curr_coords[:,0],curr_coords[:,1]] = 0
    
    # Move the rock according to the jet
    if content[curr_jet_index] == ">":
      curr_coords += [0,1]
      if max(curr_coords[:,1]) > 6 or sum(occupied[curr_coords[:,0],curr_coords[:,1]]) > 0:
        curr_coords -= [0,1]
        print("Reverted right shift")
      else:
        print("Right shift")
    elif content[curr_jet_index] == "<":
      curr_coords -= [0,1]
      if min(curr_coords[:,1]) < 0 or sum(occupied[curr_coords[:,0],curr_coords[:,1]]) > 0:
        curr_coords += [0,1]
        print("Reverted left shift")
      else:
        print("Left shift")
    else:
      assert(False)
    curr_jet_index = (curr_jet_index+1)%len(content)
    
    # Move downwards
    curr_coords -= [1,0]
    
    # Check if it's occupied
    if sum(occupied[curr_coords[:,0],curr_coords[:,1]]) > 0:
      curr_coords += [1,0]
      occupied[curr_coords[:,0],curr_coords[:,1]] = 1
      # Update the highest y
      highest_rock_y = max(np.argwhere(occupied==1)[:,0])
      rock_index = (rock_index+1)%len(rocks)
      break

# Debug prints
#occupied[curr_coords[:,0],curr_coords[:,1]] = 1
#print(print_scrn())
#occupied[curr_coords[:,0],curr_coords[:,1]] = 0
print(highest_rock_y)
