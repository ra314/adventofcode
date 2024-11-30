import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
import itertools
from math import inf
import itertools

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

def hesh(x):
  i = 0
  for char in x:
    i += ord(char)
    i *= 17
    i %= 256
  return i

heshmap = defaultdict(lambda: [[],[]])
for line in content.strip().split(","):
  op_is_add = line[-1].isdigit()
  if op_is_add:
    label = line[:-2]
  else:
    label = line[:-1]
  h = hesh(label)
  labels, lenses = heshmap[h]
  if op_is_add:
    try:
      index = labels.index(label)
      lenses[index] = int(line[-1])
    except:
      labels.append(label)
      lenses.append(int(line[-1]))
  else:
    try:
      index = labels.index(label)
      del lenses[index]
      del labels[index]
    except:
      pass
  print(heshmap)

total = 0
for key, values in heshmap.items():
  if len(values[0]) == 0: continue
  for i in range(len(values[0])):
    label, lense = values[0][i], values[1][i]
    total += ((key+1)*(i+1)*lense)

print(total)
