content = open("input.txt").read()

import numpy as np
class Numpad:
  def __init__(self):
    self.numpad = [[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0,0,'D',0,0]]
    self.curr = np.array((2,0))
  
  def is_in_grid(self, coord):
    return self.numpad[coord[0]][coord[1]] != 0
  
  def move(self, direction):
    if direction == "L":
      next_coord = self.curr + (0, -1)
    elif direction == "R":
      next_coord = self.curr + (0, 1)
    elif direction == "D":
      next_coord = self.curr + (1, 0)
    elif direction == "U":
      next_coord = self.curr + (-1, 0)
    next_coord = np.clip(next_coord, 0, 4)
    if self.is_in_grid(next_coord):
      self.curr = next_coord
  
  def move_repeated(self, directions):
    for direction in directions:
      self.move(direction)
  
  def get_num(self):
    return self.numpad[self.curr[0]][self.curr[1]]

numpad = Numpad()
passcode = ""
for line in content.splitlines():
  numpad.move_repeated(list(line))
  passcode += str(numpad.get_num())

print(passcode)
