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

def print_scrn(grid):
  return "\n".join(["".join([num_to_chr[int(x)] for x in row]) for row in np.flip(grid, (0))])

rocks = []
rocks.append(Rock([(0,x) for x in range(4)]))
rocks.append(Rock([(0,1),(1,0),(1,1),(1,2),(2,1)]))
rocks.append(Rock([(2,2),(1,2),(0,0),(0,1),(0,2)]))
rocks.append(Rock([(y,0) for y in range(4)]))
rocks.append(Rock([(0,0),(0,1),(1,0),(1,1)]))

history_to_highest_rock = {}
highest_rocks = []

rock_index = 0
jet_index = 0
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
    if content[jet_index] == ">":
      curr_coords += [0,1]
      if max(curr_coords[:,1]) > 6 or sum(occupied[curr_coords[:,0],curr_coords[:,1]]) > 0:
        curr_coords -= [0,1]
        #print("Reverted right shift")
      else:
        pass
        #print("Right shift")
    elif content[jet_index] == "<":
      curr_coords -= [0,1]
      if min(curr_coords[:,1]) < 0 or sum(occupied[curr_coords[:,0],curr_coords[:,1]]) > 0:
        curr_coords += [0,1]
        #print("Reverted left shift")
      else:
        pass
        #print("Left shift")
    else:
      assert(False)
    jet_index = (jet_index+1)%len(content)
    
    # Move downwards
    curr_coords -= [1,0]
    
    # Check if it's occupied
    if sum(occupied[curr_coords[:,0],curr_coords[:,1]]) > 0:
      curr_coords += [1,0]
      occupied[curr_coords[:,0],curr_coords[:,1]] = 1
      # Update the highest y
      highest_rock_y = max(np.argwhere(occupied==1)[:,0])
      rock_index = (rock_index+1)%len(rocks)
      
      if i > 100:
        new_hist = ((rock_index, jet_index, print_scrn(occupied[highest_rock_y-100:highest_rock_y])))
        if new_hist in history_to_highest_rock:
          assert(False)
        history_to_highest_rock[new_hist] = (highest_rock_y, i)
        highest_rocks.append(highest_rock_y)
      else:
        highest_rocks.append(0)
      break

prev_highest, prev_i = history_to_highest_rock[new_hist]
cycle_time = i-prev_i
height_per_cycle = highest_rock_y - prev_highest
print(highest_rock_y, height_per_cycle, cycle_time)

num_whole_number_cycles = (1000000000000-i)//cycle_time
new_y = highest_rock_y + (height_per_cycle*num_whole_number_cycles)
cycles_left = 1000000000000-(i+(num_whole_number_cycles*cycle_time))
# Off by 1 fix
cycles_left -= 1
new_y += (highest_rocks[prev_i+cycles_left] - prev_highest)

print(new_y)
