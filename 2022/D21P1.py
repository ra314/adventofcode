import re
import numpy as np
from copy import copy
myfile = open("input2.txt")
content = myfile.read().splitlines()

known = {}
unknown = {}
for line in content:
  key, value = re.search(r'(....): (.*)', line).groups()
  if value.isdigit():
    known[key] = value
  else:
    unknown[key] = value

while unknown:
  print(len(known),len(unknown))
  for key in list(unknown.keys()):
    value = unknown[key]
    first, second = value[:4], value[-4:]
    if first in known and second in known:
      f, s = known[first], known[second]
      ans = eval(f'{f} {value[5]} {s}')
      known[key] = ans
      del unknown[key]

print(known['root'])
# 70674280581468.0

