content = open("input2.txt").read().splitlines()

import re
import numpy as np

def dist(p1, p2):
  return np.abs(p1- p2).sum()

# Returns true if the cubes that the bots form intersect
def do_signals_intersect(bot1, bot2):
  # One of the bots contains the others
  if dist(bot2.loc, bot1.loc) <= max((bot1.r, bot2.r)):
    return True
  
  # Otherwise we check that both bots contain the corners of the signal of the other bot
  bot1_contains_bot2_signal_cube = False
  for corner in bot1.corners:
    if dist(bot2.loc, corner) <= bot2.r:
      bot1_contains_bot2_signal_cube = True
      break
  bot2_contains_bot1_signal_cube = False
  for corner in bot2.corners:
    if dist(bot1.loc, corner) <= bot1.r:
      bot2_contains_bot1_signal_cube = True
      break
  return bot2_contains_bot1_signal_cube and bot1_contains_bot2_signal_cube

class Bot:
  bots = []
  
  def __init__(self, x, y, z, r):
    self.loc = np.array([x,y,z])
    self.r = r
    self.corners = self.get_corners()
    Bot.bots.append(self)
  
  # Get the corners of the cube formed by the bot
  def get_corners(self):
    corners = []
    for x in (1, -1):
      for y in (1, -1):
        for z in (1, -1):
          xyz = np.array([x,y,z])
          corners.append(self.loc + (xyz*self.r))
    return corners
  
  def get_num_bots_reachable_to_point(point):
    return sum([(dist(bot.loc, point) <= bot.r) for bot in Bot.bots])
  
  def get_within_radius_bot_count(self):
    return sum([(dist(bot.loc, self.loc) <= self.r) for bot in Bot.bots])
  
  # Get's the bot with the biggest radius
  def get_strongest_bot():
    return max(Bot.bots, key=lambda x: x.r)

for line in content:
  result = re.findall('(-?\d+),(-?\d+),(-?\d+)', line)
  assert(len(result[0])==3)
  x,y,z = list(map(int, result[0]))
  r = int(re.search('r=(-?\d+)', line)[1])
  Bot(x,y,z,r)

# Biggest coordinate is
coords = []
for bot in Bot.bots:
  coords.extend(np.abs(bot.loc).tolist())
print(max(coords))
# We don't search outside of this
biggest = max(coords)

from random import randint
# Get's a random point within "biggest"
def get_random_point():
  return np.random.randint(-biggest, high=biggest, size=3)

# Start with a random point
start_step_size = 10
max_iterations = 200

# Randomly move from curr with range of step_size_min and step_size_max
def move_by_step(curr, curr_reachable, step_size_min, step_size_max):
  next = curr + np.random.randint(step_size_min, high=step_size_max, size=3)
  next_reachable = Bot.get_num_bots_reachable_to_point(next)
  return next, next_reachable

curr = np.array([17188356, 40491771, 33773220])
# This function needs to be called multiple times
# Not guaranteed to find the best solution
# It starts at curr and randomly moves by using move_by_step
# If it doesn't find a better point, it increases the step size
def find_point_with_most(curr):
  curr_step_size = start_step_size
  if len(curr)==0:
    curr = get_random_point()
  curr_reachable = Bot.get_num_bots_reachable_to_point(curr)

  while curr_step_size < biggest:
    i = 0
    while i < max_iterations:
      next, next_reachable = move_by_step(curr, curr_reachable, -curr_step_size, curr_step_size)
      if next_reachable > curr_reachable:
        print(next, next_reachable)
        curr, curr_reachable = next, next_reachable
        i = 0
        curr_step_size = start_step_size
      else:
        i += 1
    print(curr_step_size)
    curr_step_size *= 10

  return curr, curr_reachable

# Best so far
# (array([  813315, 40440359, 15891961]), 784)
# (array([17188356, 40491771, 33773220]), 906)

# Other Best
# (array([16886662, 40058656, 32335334]), 863)

# Given a point that has the most intersections, this function moves randomly
# until it finds the point that has the most intersections and is also closest to origin
# This should work since the region that has the most intersections should be continguous
# Although this doesn't account for if there are multiple distinct regions
# that all have the most intersections.
def find_point_closest_to_origin(curr):
  curr_step_size = start_step_size
  curr_reachable = Bot.get_num_bots_reachable_to_point(curr)

  while curr_step_size < biggest:
    i = 0
    while i < max_iterations:
      next, next_reachable = move_by_step(curr, curr_reachable, -curr_step_size, 0)
      if next_reachable >= curr_reachable and np.abs(next_reachable).sum() < np.abs(curr_reachable).sum():
        print(next, next_reachable)
        curr, curr_reachable = next, next_reachable
        i = 0
        curr_step_size = start_step_size
      else:
        i += 1
    print(curr_step_size)
    curr_step_size *= 10

  return curr, curr_reachable

# Create graph of intersections
# Each node is a cube
# 2 nodes are connected in the graph if the cubes intersect
from collections import defaultdict
def create_graph(bots):
  graph = defaultdict(list)
  for i, bot1 in enumerate(bots):
    print(i)
    for j in range(i+1, len(bots)):
      bot2 = bots[j]
      if do_signals_intersect(bot1, bot2):
        graph[bot1].append(bot2)
        graph[bot2].append(bot1)
  return graph

graph = create_graph(Bot.bots)
print(graph[Bot.bots[0]])
