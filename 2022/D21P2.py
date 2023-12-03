import re
from scipy.optimize import minimize
myfile = open("input.txt")
content = myfile.read().splitlines()

def f(x):
  known = {}
  unknown = {}
  for line in content:
    key, value = re.search(r'(....): (.*)', line).groups()
    if value.isdigit():
      known[key] = value
    else:
      unknown[key] = value

  # Insertion
  known["humn"] = x

  while len(unknown)>1:
    #print(len(known),len(unknown))
    for key in list(unknown.keys()):
      if key == "root": continue
      value = unknown[key]
      first, second = value[:4], value[-4:]
      if first in known and second in known:
        f, s = known[first], known[second]
        ans = eval(f'{f} {value[5]} {s}')
        known[key] = ans
        del unknown[key]

  value = (unknown['root'])
  first, second = value[:4], value[-4:]
  f, s = known[first], known[second]
  f, s = int(f), int(s)
  return f-s

curr = 1000000000000
step = 1000000000000
while f(curr) != 0:
  print(curr, step, f(curr))
  if f(curr+step)<0:
    step = step//2
  else:
    curr += step
