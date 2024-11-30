import numpy as np
from collections import defaultdict
from collections import Counter
from collections import deque
import re
import itertools
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

content = np.array(list(map(list, content.splitlines())))
print(content)
print()

y = 0
while y < content.shape[0]:
  row = content[y]
  if np.all(row == "."):
    content = np.concatenate((content[:y],np.zeros((1,content.shape[1]), dtype='<U11', ), content[y:]), axis=0)
    y += 2
  else:
    y += 1

content[content==""] = "."
print(content)
print()

x = 0
while x < content.shape[1]:
  col = content[:,x]
  if np.all(col == "."):
    content = np.concatenate((content[:,:x],np.zeros((content.shape[0],1), dtype='<U11', ), content[:,x:]), axis=1)
    x += 2
  else:
    x += 1

content[content==""] = "."
print(content)

galaxies = list(zip(*np.where(content == "#")))
total = []
for i in range(len(galaxies)):
  for j in range(len(galaxies)):
    if i==j: continue
    start, end = galaxies[i], galaxies[j]
    manhat = np.sum(np.abs(np.array(start)-np.array(end)))
    total.append(manhat)
    print(start, end, manhat)

print(len(total), sum(total)//2)
