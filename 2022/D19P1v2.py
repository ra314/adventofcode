import re
import numpy as np
from copy import copy
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

def decide_bot(blueprint):
  # Decide on which robot to build
  if blueprint.resources[ORE] < blueprint.costs[GEODE][ORE]:
    return ORE
  if blueprint.resources[OBSIDIAN] < blueprint.costs[GEODE][OBSIDIAN]:
    if blueprint.resources[CLAY] < blueprint.costs[OBSIDIAN][CLAY]:
      if blueprint.resources[ORE] < blueprint.costs[CLAY][ORE]:
        return ORE
      return CLAY
    if blueprint.resources[ORE] < blueprint.costs[OBSIDIAN][ORE]:
      return ORE
    return OBSIDIAN
  return GEODE

def get_max_geodes(blueprint):
  time = 1
  while time <= 24:
    bot = decide_bot(blueprint)
    print(time, bot)
    if np.all(blueprint.resources >= blueprint.costs[bot]):
      blueprint.resources -= blueprint.costs[bot]
      x = np.zeros(4)
      x[bot] = 1
      blueprint.resources += blueprint.robots
      blueprint.robots += x
    else:
      blueprint.resources += blueprint.robots
    print(blueprint.resources, blueprint.robots)
    time += 1

for blueprint in blueprints:
  print(get_max_geodes(blueprint))
  print("####")
