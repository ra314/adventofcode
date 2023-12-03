# num, frm, to = list(map(int, re.search(r'move (?\-\d+) from (\d+) to (\d+)', line).groups()))
# from dijkstar import Graph, find_path
# graph = Graph()
# graph.add_edge(node1, node2, weight)
# path = find_path(graph, create_node_name((0,0)), create_node_name(np.array(array.shape)-1))

import re
myfile = open("input.txt")
content = myfile.read().splitlines()


'''
Due to conservation of blizzard energy, as a blizzard reaches the wall of the valley, a new blizzard forms on the opposite side of the valley moving in the same direction
'''

'''
Because blizzards are made of tiny snowflakes, they pass right through each other.
'''

blizzards = []
walls = set()
collision_set = set()
HEIGHT = len(content)
WIDTH = len(content[0])
for y, line in enumerate(content):
  for x, char in enumerate(line):
    if char == "#":
      walls.add((y,x))
    elif char == ">":
      blizzards.append((y,x,0,1))
    elif char == "<":
      blizzards.append((y,x,0,-1))
    elif char == "^":
      blizzards.append((y,x,-1,0))
    elif char == "v":
      blizzards.append((y,x,1,0))
    elif char == ".":
      pass
    else:
      assert(False)

for y,x,dy,dx in blizzards:
  collision_set.add((y,x))

start = (0,1)
end = (5,6)
end = (26,120)
time = 0

from collections import deque
queue = deque()
queue.append((start, time))
states = set()

while queue:
  curr, c_time = queue.popleft()
  if c_time > time:
    print(time, len(queue))
    assert(c_time-time==1)
    # Simulate the blizzard
    collision_set.clear()
    new_blizzards = []
    for y,x,dy,dx in blizzards:
      assert((y,x) not in walls)
      y, x = y+dy, x+dx
      # Wall teleportation
      if (y,x) in walls:
        y, x = y+dy, x+dx
        y, x = y+dy, x+dx
        y, x = y%HEIGHT, x%WIDTH
      assert((y,x) not in walls)
      collision_set.add((y,x))
      new_blizzards.append((y,x,dy,dx))
    blizzards = new_blizzards
    time += 1
    assert(time<1000000)
  if curr in walls: continue
  if curr in collision_set: continue
  y, x = curr
  if not (0<=x<WIDTH and 0<=y<HEIGHT): continue
  if curr == end: break
  for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
    next = ((y+dy,x+dx),c_time+1)
    if next in states: continue
    queue.append(next)
    states.add(next)
    
  # Staying still
  next = ((y,x),c_time+1)
  if next not in states:
    queue.append(next)
    states.add(next)

print(c_time)
queue = deque()
queue.append((end, time))
states = set()

while queue:
  curr, c_time = queue.popleft()
  if c_time > time:
    print(time, len(queue))
    assert(c_time-time==1)
    # Simulate the blizzard
    collision_set.clear()
    new_blizzards = []
    for y,x,dy,dx in blizzards:
      assert((y,x) not in walls)
      y, x = y+dy, x+dx
      # Wall teleportation
      if (y,x) in walls:
        y, x = y+dy, x+dx
        y, x = y+dy, x+dx
        y, x = y%HEIGHT, x%WIDTH
      assert((y,x) not in walls)
      collision_set.add((y,x))
      new_blizzards.append((y,x,dy,dx))
    blizzards = new_blizzards
    time += 1
    assert(time<1000000)
  if curr in walls: continue
  if curr in collision_set: continue
  y, x = curr
  if not (0<=x<WIDTH and 0<=y<HEIGHT): continue
  if curr == start: break
  for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
    next = ((y+dy,x+dx),c_time+1)
    if next in states: continue
    queue.append(next)
    states.add(next)
    
  # Staying still
  next = ((y,x),c_time+1)
  if next not in states:
    queue.append(next)
    states.add(next)

print(c_time)
queue = deque()
queue.append((start, time))
states = set()

while queue:
  curr, c_time = queue.popleft()
  if c_time > time:
    print(time, len(queue))
    assert(c_time-time==1)
    # Simulate the blizzard
    collision_set.clear()
    new_blizzards = []
    for y,x,dy,dx in blizzards:
      assert((y,x) not in walls)
      y, x = y+dy, x+dx
      # Wall teleportation
      if (y,x) in walls:
        y, x = y+dy, x+dx
        y, x = y+dy, x+dx
        y, x = y%HEIGHT, x%WIDTH
      assert((y,x) not in walls)
      collision_set.add((y,x))
      new_blizzards.append((y,x,dy,dx))
    blizzards = new_blizzards
    time += 1
    assert(time<1000000)
  if curr in walls: continue
  if curr in collision_set: continue
  y, x = curr
  if not (0<=x<WIDTH and 0<=y<HEIGHT): continue
  if curr == end: break
  for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
    next = ((y+dy,x+dx),c_time+1)
    if next in states: continue
    queue.append(next)
    states.add(next)
    
  # Staying still
  next = ((y,x),c_time+1)
  if next not in states:
    queue.append(next)
    states.add(next)

print(c_time)
