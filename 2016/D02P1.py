content = open("input.txt").read()

import numpy as np
class Numpad:
  def __init__(self):
    self.numpad = np.arange(1,10).reshape((3,3))
    self.curr = np.array((1,1))
  
  def move(self, direction):
    if direction == "L":
      self.curr += (0, -1)
    elif direction == "R":
      self.curr += (0, 1)
    elif direction == "D":
      self.curr += (1, 0)
    elif direction == "U":
      self.curr += (-1, 0)
    self.curr = np.clip(self.curr, 0, 2)
  
  def move_repeated(self, directions):
    for direction in directions:
      self.move(direction)
  
  def get_num(self):
    return self.numpad[self.curr[0], self.curr[1]]

numpad = Numpad()
passcode = ""
for line in content.splitlines():
  numpad.move_repeated(list(line))
  passcode += str(numpad.get_num())

print(passcode)
