import re
from math import inf
from itertools import combinations, permutations
myfile = open("input.txt")
content = myfile.read().splitlines()

valves = {}
class Valve:
  def __init__(self, flow_rate, neighbours, name):
    self.flow_rate = flow_rate
    self.neighbours = neighbours
    self.name = name
    self.is_released = False
  
  def __hash__(self):
    return hash(self.name)
  
  def __str__(self):
    return f'{self.name}, {self.flow_rate}, {self.neighbours}'

for line in content:
  name, flow_rate, neighbours = re.search(r'Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line).groups()
  flow_rate = int(flow_rate)
  neighbours = neighbours.split(", ")
  valves[name] = Valve(flow_rate, neighbours, name)
  if valves[name].flow_rate == 0:
    valves[name].is_released = True

for valve in valves.values():
  valve.neighbours = [valves[n] for n in valve.neighbours]

print("#####")
for valve in valves.values():
  print(valve)
print("#####")

unopened_valves = set([v for v in valves.values() if not v.is_released])
opened_valves = set([v for v in valves.values() if v.is_released])
# DP TSP
def TSP(time, loc, el_loc, valves_opened):
  if loc.is_released and el_loc.is_released:
    for new_loc in loc.neighbours:
      for new_el_loc in el_loc.neighbours:
        TSP(time-1, new_loc, new_el_loc, opened_valves)
  new_score = 0
  if not loc.is_released and not el_loc.is_released:
    loc.is_released = True
    el_loc.is_released = True
    new_score += (me_curr.flow_rate*(me_time_left-1))
    loc.is_released = False
    el_loc.is_released = False

val = TSP(26, valves["AA"], valves["AA"], opened_valves)
print(val)    
