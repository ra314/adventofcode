import re, numpy as np
myfile = open("input.txt")
content = myfile.read()

tail = np.array((0,0))
head = np.array((0,0))
visited = set()
visited.add(tuple(tail))

for line in content.splitlines():
  dirr = line.split()[0]
  steps = int(line.split()[1])
  for _ in range(steps):
    match dirr:
      case "R":
        head += np.array([1,0])
      case "L":
        head -= np.array([1,0])
      case "U":
        head += np.array([0,1])
      case "D":
        head -= np.array([0,1])
    dist = max(np.abs(head-tail))
    print(head, tail, dist)
    if dist > 2:
      assert(False)
    if dist == 2:
      delta = head-tail
      delta[delta==2]=1
      delta[delta==-2]=-1
      tail += delta
      visited.add(tuple(tail))

print(len(visited))
