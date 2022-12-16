content = open("input2.txt").read().splitlines()

import re
import numpy as np
class Bot:
  bots = []
  
  def __init__(self, x, y, z, r):
    self.loc = np.array([x,y,z])
    self.r = r
    Bot.bots.append(self)
  
  def get_within_radius_bot_count(self):
    return sum([(np.abs(bot.loc - self.loc).sum() <= self.r) for bot in Bot.bots])
  
  def get_strongest_bot():
    return max(Bot.bots, key=lambda x: x.r)

for line in content:
  result = re.findall('(-?\d+),(-?\d+),(-?\d+)', line)
  assert(len(result[0])==3)
  x,y,z = list(map(int, result[0]))
  r = int(re.search('r=(-?\d+)', line)[1])
  Bot(x,y,z,r)

print(Bot.get_strongest_bot().get_within_radius_bot_count())
