import itertools
import numpy as np
from math import ceil

myfile = open("input.txt")
content = myfile.read()

boss_stats = {'hp':100, 'damage':8, 'armor':2}
#boss_stats = {'hp':12, 'damage':7, 'armor':2}

shop = {}
curr_section = None
for line in content.splitlines():
  line = line.split()
  if not line:
    continue
  if line[0][:-1] in ['Armor', 'Rings', 'Weapons']:
    curr_section = []
    shop[line[0][:-1].lower()] = curr_section
    continue
  if '+' in line[1]:
    del line[1]
  curr_section.append(tuple(map(int, line[1:])))

shop['armor'].append((0,0,0))
shop['rings'].append((0,0,0))
shop['rings'].append((0,0,0))
print(shop)

rings = itertools.combinations(shop['rings'], 2)
all_combos = itertools.product(shop['weapons'], shop['armor'], rings)

# Returns true if the player wins
def simulate(player_stats, boss_stats):
  player_damage_dealt = max(player_stats['damage'] - boss_stats['armor'], 1)
  boss_damage_dealt = max(boss_stats['damage'] - player_stats['armor'], 1)
  num_player_hits = ceil(boss_stats['hp']/player_damage_dealt)
  num_boss_hits = ceil(player_stats['hp']/boss_damage_dealt)
  return num_player_hits <= num_boss_hits

max_cost = 0
best_player_stats = None
for combo in all_combos:
  info = np.array(combo[:2] + combo[2]).sum(axis=0)
  player_stats = {'hp':100, 'damage':info[1], 'armor':info[2]}
  cost = info[0]
  if not simulate(player_stats, boss_stats):
    if cost > max_cost:
      max_cost = cost
      best_player_stats = player_stats

print(max_cost, best_player_stats)
