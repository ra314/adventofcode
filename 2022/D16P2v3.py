import re
from math import inf
from itertools import combinations, permutations
myfile = open("input.txt")
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

# Remove all 0 flow valves
for no_flow_valve in list(valves.values()):
  if no_flow_valve.flow_rate != 0: continue
  if no_flow_valve.name == "AA": continue
  for valve in list(valves.values()):
    if no_flow_valve.name in valve.neighbours:
      del valve.neighbours[no_flow_valve.name]
  del valves[no_flow_valve.name]

# Add 1 to all distances to account for releasing the valve
for valve in valves.values():
  for key in valve.neighbours:
    valve.neighbours[key] += 1


# Minizinc input
print("#####")
print("Minizinc parameters")
# Adding a null valve
# And adding visiting self as 0 cost
null_valve = Valve(0, {}, "XXX")
for key in valves.keys():
  valves[key].neighbours["XXX"] = 0
  null_valve.neighbours[key] = 100
  valves[key].neighbours[key] = 0
valves["XXX"] = null_valve
null_valve.neighbours["XXX"] = 0

valve_names = sorted(list(valves.keys()))
valve_enums = str(valve_names)[1:-1].replace('\'','')
print(f"enum VALVE = {{{valve_enums}}};")
print(f"int: n = {len(valves)};")

matrix = [[valves[y].neighbours[x] for x in valve_names] for y in valve_names]
matrix_str = "|\n  ".join([str(x)[1:-1] for x in matrix])
print(f"time = \n[|{matrix_str}|];")
print(f"valve_flow_rate = {str([valves[n].flow_rate for n in valve_names])};")
for key in valve_names:
  if key == "XXX": continue
  print(f"constraint count_leq(visited, {key}, 1);")

print("#####")
for valve in valves.values():
  print(valve)
