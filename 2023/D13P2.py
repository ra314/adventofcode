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

def find_reflection(pattern):
  for x in range(1,pattern.shape[0]):
    before_len, after_len = x, pattern.shape[0]-x
    size = min(before_len, after_len)
    if np.all(pattern[x-size:x]==np.flip(pattern[x:x+size], axis=0)):
      return x * 100, True
  for y in range(1,pattern.shape[1]):
    before_len, after_len = y, pattern.shape[1]-y
    size = min(before_len, after_len)
    if np.all(pattern[:,y-size:y]==np.flip(pattern[:,y:y+size], axis=1)):
      return y, False
  assert(False)
    
reflections = []
for pattern in content.split("\n\n"):
  pattern = np.array(list(map(list, pattern.splitlines())))
  reflections.append(find_reflection(pattern))

print(reflections)
print(sum([x[0] for x in reflections]))


def find_alt_reflection(pattern, line_num, is_x):
  if is_x: 
    line_num = line_num//100
  for x in range(1,pattern.shape[0]):
    if is_x and (x == line_num): continue
    before_len, after_len = x, pattern.shape[0]-x
    size = min(before_len, after_len)
    diff = np.sum(pattern[x-size:x]!=np.flip(pattern[x:x+size], axis=0))
    if diff == 1:
      return x * 100
  for y in range(1,pattern.shape[1]):
    if (not is_x) and (y == line_num): continue
    before_len, after_len = y, pattern.shape[1]-y
    size = min(before_len, after_len)
    diff = np.sum(pattern[:,y-size:y]!=np.flip(pattern[:,y:y+size], axis=1))
    if diff == 1:
      return y
  assert(False)

new_reflections = []
for i, pattern in enumerate(content.split("\n\n")):
  pattern = np.array(list(map(list, pattern.splitlines())))
  line_num, is_x = reflections[i]
  new_reflections.append(find_alt_reflection(pattern, line_num, is_x))

print(new_reflections)
print(sum(new_reflections))
