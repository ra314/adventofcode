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
      return x * 100
  for y in range(1,pattern.shape[1]):
    before_len, after_len = y, pattern.shape[1]-y
    size = min(before_len, after_len)
    if np.all(pattern[:,y-size:y]==np.flip(pattern[:,y:y+size], axis=1)):
      return y
  assert(False)
    
reflections = []
for pattern in content.split("\n\n"):
  pattern = np.array(list(map(list, pattern.splitlines())))
  reflections.append(find_reflection(pattern))

print(reflections)
print(sum(reflections))
