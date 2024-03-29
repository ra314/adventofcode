import re
from math import inf
from itertools import combinations, permutations
myfile = open("input2.txt")
content = myfile.read().splitlines()

valves = {}
class Valve:
  def __init__(self, flow_rate, neighbours, name):
    self.flow_rate = flow_rate
    self.neighbours = {n:1 for n in neighbours}
    self.name = name
    self.is_released = False
  
  def __str__(self):
    return f'{self.name}, {self.flow_rate}, {self.neighbours}'

for line in content:
  name, flow_rate, neighbours = re.search(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line).groups()
  flow_rate = int(flow_rate)
  neighbours = neighbours.split(", ")
  valves[name] = Valve(flow_rate, neighbours, name)

print("#####")
for valve in valves.values():
  print(valve)
print("#####")

# Transitive Closure
for _ in range(len(valves.values())):
  for v1 in valves.values():
    for v2 in valves.values():
      if v1 == v2: continue
      new_dist = v1.neighbours.get(v2.name, inf)
      for v1n, v1d in v1.neighbours.items():
        if v1n in v2.neighbours:
          new_dist = min(v1d + v2.neighbours[v1n], new_dist)
      v1.neighbours[v2.name] = new_dist
      v2.neighbours[v1.name] = new_dist

print("#####")
for valve in valves.values():
  print(valve)

# Remove all 0 flow valves
for no_flow_valve in list(valves.values()):
  if no_flow_valve.flow_rate != 0: continue
  if no_flow_valve.name == "AA": continue
  for valve in list(valves.values()):
    if no_flow_valve.name in valve.neighbours:
      del valve.neighbours[no_flow_valve.name]
  del valves[no_flow_valve.name]

print("#####")
for valve in valves.values():
  print(valve)

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

partition_pairs = []
for p1 in powerset(valves.values()):
  p2 = set(valves.values()).difference(p1)
  partition_pairs.append((p1,p2))


