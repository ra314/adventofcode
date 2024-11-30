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

heshs = []
for line in content.strip().split(","):
  heshs.append(hesh(line))

print(sum(heshs))
