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

# Brute force the TSP
best_score = 0
best_path = []
el_curr = valves["AA"]
me_curr = valves["AA"]
valves["AA"].is_released = True
num_valves = len(valves.values())
valve_perms = list(permutations(valves.values(), 2))
x = 0
def TSP(el_curr, me_curr, curr_path, el_time_left, me_time_left, curr_score, progress, num_released):
  global best_score, best_path, x
  x += 1
  if x == 1000000:
    print(progress)
    x = 0
  if (el_time_left<=0 and me_time_left<=0) or num_released == num_valves:
    if curr_score > best_score:
      best_score, best_path = curr_score, curr_path
      print(best_score)
    return
  # Only time the elephant and I should be out of sync
  # Is when there's only 1 valve left
  # Or when one of us have run out of time
  # In either case the person standing on the released valve has nothing to do
  if el_curr.is_released != me_curr.is_released:
    if el_time_left>=0 and me_time_left>=0:
      if num_valves-num_released != 1:
        assert(False)
  was_valve_released = not el_curr.is_released or not me_curr.is_released
  new_score = curr_score
  new_path = curr_path 
  revert_el = False
  revert_me = False
  new_num_released = num_released
  new_el_time_left = el_time_left
  new_me_time_left = me_time_left
  # Possible actions are releasing current valve
  # Or moving through the tunnel to non released valve
  if not el_curr.is_released:
    el_curr.is_released = True
    revert_el = True
    new_score += (el_curr.flow_rate*(el_time_left-1))
    new_el_time_left = el_time_left-1
    new_num_released += 1
    new_path += [f"El rel {el_curr.name}, {new_score}, {new_el_time_left}, {new_me_time_left}"]
  if not me_curr.is_released:
    me_curr.is_released = True
    revert_me = True
    new_score += (me_curr.flow_rate*(me_time_left-1))
    new_me_time_left = me_time_left-1
    new_num_released += 1
    new_path += [f"me rel {me_curr.name}, {new_score}, {new_el_time_left}, {new_me_time_left}"]
  if was_valve_released:
    TSP(el_curr, me_curr, new_path, new_el_time_left, new_me_time_left, new_score, progress, new_num_released)
  if revert_el:
    el_curr.is_released = False
  if revert_me:
    me_curr.is_released = False
  if not was_valve_released:
    # Get list of all non released valves
    non_released = [v for v in valves.values() if not v.is_released]
    # If there's only one left the one closest to it should go there
    if len(non_released) == 1:
      non_valve = non_released[0]
      if me_curr.neighbours[non_valve.name] < el_curr.neighbours[non_valve.name]:
        new_path = curr_path + [f"Me move to {non_valve.name}"]
        new_me_time_left = me_time_left - me_curr.neighbours[non_valve.name]
        new_me_curr = non_valve
        TSP(el_curr, new_me_curr, new_path, el_time_left, new_me_time_left, curr_score, progress + ["1/1"], num_released)
      else:
        new_path = curr_path + [f"El move to {non_valve.name}"]
        new_el_time_left = el_time_left - el_curr.neighbours[non_valve.name]
        new_el_curr = non_valve
        TSP(new_el_curr, me_curr, new_path, new_el_time_left, me_time_left, curr_score, progress + ["1/1"], num_released)
    else:
      # Try all permutations for me and the elephant
      for i, perm in enumerate(valve_perms):
        new_me_curr, new_el_curr = perm
        if new_me_curr.is_released: continue
        if new_el_curr.is_released: continue
        new_path = curr_path + [f"Me move to {new_me_curr.name}"] + [f"El move to {new_el_curr.name}"]
        new_me_time_left = me_time_left - me_curr.neighbours[new_me_curr.name]
        new_el_time_left = el_time_left - el_curr.neighbours[new_el_curr.name]
        new_progress = progress + [f"{i}/{len(valve_perms)}"]
        TSP(new_el_curr, new_me_curr, new_path, new_el_time_left, new_me_time_left, curr_score, new_progress, num_released)

TSP(el_curr, me_curr, [], 26, 26, 0, [], 1)
print("#####")
print(best_score, best_path)
    
