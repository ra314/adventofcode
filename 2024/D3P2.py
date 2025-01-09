import reader
content = reader.read()

import re
from math import inf

dos = [m.start() for m in re.finditer(r'do\(\)', content)]
donts = [m.start() for m in re.finditer(r'don\'t\(\)', content)]
dos = [(pos, "do") for pos in dos]
donts = [(pos, "dont") for pos in donts]
combined = sorted(dos + donts)

total = 0
curr_op = "do"
index = -1
next_op_pos = combined[0][0]
for match in re.finditer(r'mul\((\d+),(\d+)\)', content):
  start = match.span()[0]
  x, y = int(match[1]), int(match[2])
  if start > next_op_pos:
    index += 1
    curr_op = combined[index][1]
    if index+1 < len(combined):
      next_op_pos = combined[index+1][0]
    else:
      next_op_pos = inf
  if curr_op == "do":
    total += x * y
print(total)

# Cleaned up solution.
matches = re.findall(r'(mul\((\d+),(\d+)\)|do\(\)|don\'t\(\))', content)
curr_op = "do"
total = 0
for match in matches:
  match: str
  if match[0].startswith("mul") and curr_op == "do":
    x, y = int(match[1]), int(match[2])
    total += x * y
  elif match[0].startswith("don't"):
    curr_op = "dont"
  elif match[0].startswith("do"):
    curr_op = "do"
print(total)
