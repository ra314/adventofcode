import itertools
import numpy as np
from math import ceil, inf

myfile = open("input.txt")
content = myfile.read()

def missile(x):
  x['boss_hp'] -= 4
  x['mana'] -= 53
  x['mana_spent'] += 53
  return True
def drain(x):
  x['boss_hp'] -= 2
  x['player_hp'] += 2
  x['mana'] -= 73
  x['mana_spent'] += 73
  return True
def shield(x):
  #x['armor'] = 7
  if x['shield_timer']: return False
  x['shield_timer'] = 6
  x['mana'] -= 113
  x['mana_spent'] += 113
  return True
def poison(x):
  #x['boss_hp'] -= 3
  if x['poison_timer']: return False
  x['poison_timer'] = 6
  x['mana'] -= 173
  x['mana_spent'] += 173
  return True
def recharge(x):
  #x['mana'] += 101
  if x['recharge_timer']: return False
  x['recharge_timer'] = 5
  x['mana'] -= 229
  x['mana_spent'] += 229
  return True
actions = [missile, drain, shield, poison, recharge]

boss_stats = {'hp':55, 'damage':8}
#boss_stats = {'hp':13, 'damage':8}
player_stats = {'hp':50, 'mana':500}
#player_stats = {'hp':10, 'mana':250}

game_state_keys = ['mana', 'player_hp', 'boss_hp', 'shield_timer', 'poison_timer', 'armor', 'recharge_timer', 'mana_spent']
game_state = {key:0 for key in game_state_keys}
game_state['spells_cast'] = tuple()

new_state = game_state.copy()
new_state['player_hp'] = player_stats['hp']
new_state['mana'] = player_stats['mana']
new_state['boss_hp'] = boss_stats['hp']
bfs_queue = [new_state]

min_mana_cost = inf
min_mana_cost_state = None
boss_ded_counter = 0
player_ded_counter = 0
def is_game_over(state):
  global min_mana_cost, min_mana_cost_state, boss_ded_counter, player_ded_counter
  if state['mana'] <= 0:
    player_ded_counter += 1
    return True
  if state['boss_hp'] <= 0:
    boss_ded_counter += 1
    if state['mana_spent'] < min_mana_cost:
      print("Found a more optimal solution.")
      min_mana_cost = state['mana_spent']
      min_mana_cost_state = state
    return True
  if state['player_hp'] <= 0:
    player_ded_counter += 1
    return True
  return False

def process_timers(state):
  if state['poison_timer']:
    state['poison_timer'] -= 1
    state['boss_hp'] -= 3
  if state['recharge_timer']:
    state['recharge_timer'] -= 1
    state['mana'] += 101
  if state['shield_timer']:
    state['armor'] = 7
    state['shield_timer'] -= 1
    if state['shield_timer'] == 0:
      state['armor'] = 0

i = 0
while bfs_queue:
  #print("\n".join(map(str, bfs_queue)))
  #print()
  i += 1
  if i%10000 == 0:
    print(len(bfs_queue))
    print(f"Total: {boss_ded_counter+player_ded_counter} Win: {boss_ded_counter} Loss: {player_ded_counter}")
  curr_state = bfs_queue.pop(0)
  for action in actions:
    if curr_state['mana_spent'] >= min_mana_cost: continue
    new_state = curr_state.copy()
    new_state['player_hp'] -= 1
    if is_game_over(new_state): continue
    process_timers(new_state)
    if is_game_over(new_state): continue
    if not action(new_state):
      continue
    new_state['spells_cast'] += tuple([action.__name__])
    if is_game_over(new_state): continue
    process_timers(new_state)
    if is_game_over(new_state): continue
    new_state['player_hp'] -= max(boss_stats['damage'] - new_state['armor'], 1)
    if is_game_over(new_state): continue
    bfs_queue.append(new_state)
