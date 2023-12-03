import re
import numpy as np
from copy import copy
import os
myfile = open("input2.txt")
content = myfile.read().splitlines()

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
NA = 4

class Blueprint:
  def __init__(self, blueprint_id, ore_rc, clay_rc, obsidian_rc, geode_rc):
    self.blueprint_id = blueprint_id
    # Costs for each time of robot
    self.costs = np.array([ore_rc, clay_rc, obsidian_rc, geode_rc, np.zeros(5)])
    # Resource counts
    self.resources = np.zeros(4)
    # Robot counts
    self.robots = np.zeros(4)
    self.robots[0] = 1
  def __str__(self):
    return "|".join([str(list(cost))[1:-1] for cost in self.costs.astype('int')])

blueprints = []
for line in content:
  nums = [int(x) for x in re.findall(r'\d+', line)]
  blueprint_id, oc1, oc2, oc3, clay_cost, oc4, obsidian_cost = nums
  blueprints.append(Blueprint(blueprint_id, np.array((oc1,0,0,0,0)), np.array((oc2,0,0,0,0)), np.array((oc3,clay_cost,0,0,0)), np.array((oc4,0,obsidian_cost,0,0))))

for blueprint in blueprints:
  blueprint_str = f"blueprint = [|{blueprint}|];"
  f = open("D19P1_data.mzn", "w")
  f.write(blueprint_str)
  f.close()
  os.system("/home/ra314/All/Programming/MiniZincIDE-2.6.4-bundle-linux-x86_64/bin/minizinc D19P1.mzn D19P1_data.mzn")
