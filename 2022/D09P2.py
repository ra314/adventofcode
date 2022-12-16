import re, numpy as np
myfile = open("input.txt")
content = myfile.read()

rope = np.zeros((10,2))
visited = set()
visited.add((0,0))

for line in content.splitlines():
  dirr = line.split()[0]
  steps = int(line.split()[1])
  for _ in range(steps):
    match dirr:
      case "R":
        rope[0] += np.array([1,0])
      case "L":
        rope[0] -= np.array([1,0])
      case "U":
        rope[0] += np.array([0,1])
      case "D":
        rope[0] -= np.array([0,1])
    for i in range(len(rope)-1):
      curr, next = rope[i], rope[i+1]
      dist = max(np.abs(curr-next))
      if dist > 2:
        assert(False)
      if dist == 2:
        delta = curr-next
        delta[delta==2]=1
        delta[delta==-2]=-1
        next += delta
    visited.add(tuple(rope[-1]))

print(len(visited))
