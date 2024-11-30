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

content = list(map(list, content.splitlines()))

# Go through each col try and shift each round rock as far up as possible
for x in range(len(content[0])):
  lowest_open = -1
  for y in range(len(content)):
    char = content[y][x]
    match char:
      case "O":
        if lowest_open != -1:
          content[lowest_open][x] = "O"
          content[y][x] = "."
          lowest_open += 1
      case ".":
        if lowest_open == -1:
          lowest_open = y
      case "#":
        lowest_open = -1
      case _:
        assert(False)
  #print("\n".join(["".join(x) for x in content]))
  #print()

total = 0
for i, line in enumerate(content[::-1]):
  total += (line.count("O")*(i+1))

print(total)
