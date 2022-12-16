import re, numpy as np
from collections import defaultdict
myfile = open("input.txt")
content = myfile.read().splitlines()

# 1 indicates corrext, -1 indicated wrong, 0 indicates check next input
def compare(a1, a2):
  i = -1
  while i+1 < len(a1) and i+1 < len(a2):
    i += 1
    x, y = a1[i], a2[i]
    if type(x) is int and type(y) is int:
      if x == y:
        continue
      if x < y:
        return 1
      else:
        return -1
    elif type(x) is list and type(y) is list:
      val = compare(x, y)
      if val == 0:
        continue
      return val
    else:
      assert(type(x)!=type(y))
      assert(type(x) in [list, int] and type(y) in [list, int])
      if type(x) is int:
        x = [x]
      if type(y) is int:
        y = [y]
      val = compare(x, y)
      if val == 0:
        continue
      return val
  if len(a1) == len(a2):
    return 0
  elif len(a1) < len(a2):
    return 1
  else:
    return -1

correct_indices = []
i = 0
index = 1
while i < len(content):
  p1 = eval(content[i])
  p2 = eval(content[i+1])
  
  if compare(p1, p2)==1:
    correct_indices.append(index)
  i += 3
  index += 1

print(sum(correct_indices))
