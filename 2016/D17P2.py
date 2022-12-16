myfile = open("input2.txt")
content = myfile.read()[:-1]

import hashlib
pos = [0,0]

def get_possible_paths_and_positions(pos, path):
  hash_val = hashlib.md5((content+path).encode('utf-8')).hexdigest()
  directions = set("LRDU")
  if pos[0] == 0:
    directions.remove("L")
  if pos[1] == 0:
    directions.remove("U")
  if pos[0] == 3:
    directions.remove("R")
  if pos[1] == 3:
    directions.remove("D")
  allow_list = "bcdef"
  direction_order = "UDLR"
  for i in range(4):
    if hash_val[i] not in allow_list:
      directions.discard(direction_order[i])
  output = []
  for direction in directions:
    new_path = path + direction
    if direction == "L":
      new_pos = [pos[0]-1, pos[1]]
    if direction == "R":
      new_pos = [pos[0]+1, pos[1]]
    if direction == "U":
      new_pos = [pos[0], pos[1]-1]
    if direction == "D":
      new_pos = [pos[0], pos[1]+1]
    output.append((new_pos, new_path))
  return output

bfs_queue = []
bfs_queue.extend(get_possible_paths_and_positions(pos, ""))

longest_path = ""
while bfs_queue:
  pos, path = bfs_queue.pop(0)
  if pos == [3,3]:
    if len(path) > len(longest_path):
      longest_path = path
    continue
  bfs_queue.extend(get_possible_paths_and_positions(pos, path))
  print(len(bfs_queue))

print(len(longest_path))
