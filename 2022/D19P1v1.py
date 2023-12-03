# num, frm, to = list(map(int, re.search(r'move (?\-\d+) from (\d+) to (\d+)', line).groups()))
# from dijkstar import Graph, find_path
# graph = Graph()
# graph.add_edge(node1, node2, weight)
# path = find_path(graph, create_node_name((0,0)), create_node_name(np.array(array.shape)-1))

import re
import random
import numpy as np
from copy import copy
myfile = open("input2.txt")
content = myfile.read().splitlines()

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

class Blueprint:
  def __init__(self, blueprint_id, ore_rc, clay_rc, obsidian_rc, geode_rc):
    self.blueprint_id = blueprint_id
    # Costs for each time of robot
    self.costs = np.array([ore_rc, clay_rc, obsidian_rc, geode_rc])
    # Resource counts
    self.resources = np.zeros(4)
    # Robot counts
    self.robots = np.zeros(4)
    self.robots[0] = 1
  def __str__(self):
    return f"{self.costs}\n{self.resources}\n{self.robots}"

blueprints = []
for line in content:
  nums = [int(x) for x in re.findall(r'\d+', line)]
  blueprint_id, oc1, oc2, oc3, clay_cost, oc4, obsidian_cost = nums
  blueprints.append(Blueprint(blueprint_id, np.array((oc1,0,0,0)), np.array((oc2,0,0,0)), np.array((oc3,clay_cost,0,0)), np.array((oc4,0,obsidian_cost,0))))
  break

j = 0
c_max = 0
cache = {}
cache_hits = 0
def get_max_geodes(blueprint, time_left, progress):
  global j, c_max, cache, cache_hits
  # Check in the cache
  state = (tuple(blueprint.robots), tuple(blueprint.resources), time_left)
  if state in cache:
    cache_hits += 1
    return cache[state]
  # Skip this state if the number of geodes produces can not possible be greater than the max
  max_possible_geodes = blueprint.resources[GEODE] + ((time_left*(time_left+1))//2)
  if max_possible_geodes < c_max:
    return 0
  # Debug for progress
  j += 1
  if j % 10000 == 0:
    print(progress)
    print(cache_hits, j)
  # Returning the number of geodes
  if time_left <= 0:
    #print(blueprint.robots, blueprint.resources)
    return max(c_max, blueprint.resources[GEODE])
  
  # Selecting actions
  possible_actions = [ORE,CLAY,OBSIDIAN]
  random.shuffle(possible_actions)
  for i in [GEODE]+possible_actions:
    cost = blueprint.costs[i]
    # Never have more robots than the max possible consumption rate for that resource
    # Geodes are not consumed, so adding a special condition
    if max(blueprint.costs[:, i]) <= blueprint.robots[i] and i!=GEODE:
      continue
    # SKETCHY hard cap on number of clay bots
    if i == CLAY and blueprint.robots[CLAY] >= 5:
      continue
     # SKETCHY hard cap on number of obsidian bots
    if i == OBSIDIAN and blueprint.robots[OBSIDIAN] >= 5:
      continue
    # Mask to add a robot
    x = np.zeros(4)
    x[i] = 1
    if np.all(blueprint.resources >= cost):
      # Gain resources from mining
      blueprint.resources += blueprint.robots
      # Build robot
      blueprint.resources -= cost
      blueprint.robots += x
      c_max = max(c_max, get_max_geodes(blueprint, time_left-1, progress + [f"{i+1}/4"]))
      # Reversion
      blueprint.robots -= x
      blueprint.resources += cost
      blueprint.resources -= blueprint.robots
      # Always build a geode bot if you can. And consider nothing else
      if i == GEODE:
        break
  # Gain resources from mining
  blueprint.resources += blueprint.robots
  # Going to the next round without building
  c_max = max(c_max, get_max_geodes(blueprint, time_left-1, progress + [f"{i+1}/4"]))
  # Reversion
  blueprint.resources -= blueprint.robots
  # Storing in the cache
  cache[state] = c_max
  return c_max

blueprint = blueprints[0]
print(get_max_geodes(blueprints[0], 24, []))
