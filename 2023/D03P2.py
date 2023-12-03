import numpy as np
from collections import defaultdict
import re
from math import inf

f1 = open("sample.txt")
f2 = open("real.txt")
content = f2.read()
line_size = len(content.splitlines()[0])+1
num_lines = len(content.splitlines())-1
array = np.array(list(map(list, content.splitlines())))
adjacencies = defaultdict(list)
for m in re.finditer(r'\d+', content):
  start, end, num = m.start(0), m.end(0), m[0]
  y = (start//line_size)
  x1, x2 = start%line_size, end%line_size
  x1, x2 = max(x1-1, 0), min(x2+1, line_size)
  y1, y2 = max(y-1, 0), min(y+2, num_lines+1)
  area = array[y1:y2, x1:x2]
  asterisk_locs = np.swapaxes(np.array(np.where(area=="*")), 0, 1)
  for asterisk_loc in asterisk_locs:
    asterisk_loc += np.array([y1, x1])
    adjacencies[tuple(asterisk_loc)].append(num)

gear_ratios = []
for key, value in adjacencies.items():
  if len(value) == 2:
    gear_ratios.append(int(value[0])*int(value[1]))

print(gear_ratios)
print(sum(gear_ratios))
