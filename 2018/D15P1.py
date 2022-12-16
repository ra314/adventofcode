myfile = open("input2.txt")
content = myfile.read()

class Unit:
  def __init__(self, name, AP, HP, pos):
    self.name = name
    self.AP = AP
    self.HP = HP
    self.pos = pos
    self.processed = False

from collections import deque
import numpy as np

grid = []
for line in content.splitlines():
  grid.append(list(line))

rows = len(grid)
cols = len(grid[0])
units = {}

for i in range(rows):
  for j in range(cols):
    if grid[i][j] in "EG":
      pos = (i,j)
      units[pos] = Unit(grid[i][j], 3, 200, pos)

# Positions are in y,x form with the origin at the top left
deltas = np.array([[-1,0],[0,-1],[0,1],[1,0]])
def get_dir_to_enemy(pos):
  assert(len(pos)==2)
  pos = np.array(pos)
  my_name = grid[pos[0]][pos[1]]
  assert(my_name in "EG")
  enemy_name = "E" if my_name == "G" else "G"
  
  seen = set([tuple(pos)])
  # To process contains tuples
  # Each tuple contains the position to process, and the initial starting direction
  # along that path of the BFS
  to_process = deque()
  to_process.append([pos, None])
  while to_process:
    curr, original_dir = to_process.popleft()
    for delta in deltas:
      new_pos = curr+delta
      if tuple(new_pos) in seen:
        continue
      char = grid[new_pos[0]][new_pos[1]]
      if char == enemy_name:
        return [tuple(new_pos), original_dir]
      if char == my_name:
        continue
      if char == ".":
        to_process.append([new_pos, delta if original_dir is None else original_dir])
        seen.add(tuple(new_pos))
  return [tuple(pos), None]

def print_grid():
  print("\n".join(["".join(row) for row in grid]))

round_count = 0
while round_count < 500:
  for i in range(rows):
    for j in range(cols):
      char = grid[i][j]
      pos = tuple([i,j])
      if char == "G" or char == "E":
        enemy_pos, original_dir = get_dir_to_enemy([i,j])
        myself = units[pos]
        if myself.processed:
          continue
        myself.processed = True
        # Unable to move towards an enemy
        if enemy_pos == (i,j):
          continue
        # Move
        if sum(np.abs(np.array(enemy_pos) - np.array([i,j]))) > 1:
          new_pos = tuple(np.array(pos)+original_dir)
          assert(grid[new_pos[0]][new_pos[1]] == ".")
          grid[new_pos[0]][new_pos[1]] = myself.name
          grid[i][j] = "."
          del units[pos]
          units[new_pos] = myself
          myself.pos = new_pos
        # Attack if possible
        if sum(np.abs(np.array(enemy_pos) - np.array(myself.pos))) == 1:
          # Find the adjacent enemy with the least HP
          enemies = []
          for delta in deltas:
            new_pos = np.array(myself.pos) + delta
            new_pos = tuple(new_pos)
            if new_pos in units:
              if units[new_pos].name != myself.name and units[new_pos].HP>0:
                enemies.append(units[new_pos])
          enemy = min(enemies, key=lambda x:x.HP)
          # Attack the enemy
          enemy.HP -= myself.AP
          if enemy.HP <= 0:
            enemy.HP = 0
            grid[enemy.pos[0]][enemy.pos[1]] = "."
  for unit in units.values():
    unit.processed = False
  print_grid()
  print([(unit.HP, unit.pos) for unit in units.values()])
  print(round_count)
  round_count += 1
  if len(set([unit.name for unit in units.values() if unit.HP>0]))==1:
    break

print(round_count)
hp_remaining = sum([unit.HP for unit in units.values()])
print(hp_remaining)
print(round_count*hp_remaining)
