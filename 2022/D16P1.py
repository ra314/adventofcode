# num, frm, to = list(map(int, re.search(r'move (?\-\d+) from (\d+) to (\d+)', line).groups()))
# from dijkstar import Graph, find_path
# graph = Graph()
# graph.add_edge(node1, node2, weight)
# path = find_path(graph, create_node_name((0,0)), create_node_name(np.array(array.shape)-1))

import re
from math import inf
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
curr = valves["AA"]
num_valves = len(valves.values())
curr.is_released = True
x = 0
def TSP(curr, curr_path, time_left, curr_score, progress, num_released):
  global best_score, best_path, x
  x += 1
  if x == 100:
    print(progress)
    x = 0
  if time_left <= 0 or num_released == num_valves:
    if curr_score > best_score:
      best_score, best_path = curr_score, curr_path
      print(best_score)
    return
  # Possible actions are releasing current valve
  if not curr.is_released:
    curr.is_released = True
    new_score = curr_score + (curr.flow_rate*(time_left-1))
    new_path = curr_path + [f"Release {curr.name}: {new_score}, {time_left}"]
    TSP(curr, new_path, time_left-1, new_score, progress, num_released+1)
    curr.is_released = False
  else:
    # Or moving through the tunnel to non released valve
    i = 0
    for valve in valves.values():
      i += 1
      if valve.is_released: continue
      if valve.name == curr.name: continue
      new_path = curr_path + [f"Move to {valve.name}"]
      new_time_left = time_left - curr.neighbours[valve.name]
      new_curr = valve
      TSP(new_curr, new_path, new_time_left, curr_score, progress + [f"{i}/{num_valves}"], num_released)


TSP(curr, [], 30, 0, [], 1)
print("#####")
print(best_score, best_path)
    
