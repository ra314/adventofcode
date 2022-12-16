import re

with open("input.txt") as f:
    input = f.read().splitlines()

nodes = []

for line in input:
    match = re.match("/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T", line)
    if not match or len(match.groups()) != 5: continue
    x, y, size, used, avail = match.groups()
    nodes.append((int(x), int(y), int(used), int(avail)+int(used)))

grid = [ [0]*38 for i in range(28)]

for node in nodes:
  x, y, used, total = node
  grid[y][x] = f"{used}/{total}"

"\n".join([" ".join(line) for line in grid])


'''
25 and 39
move 8 rows up to get around the wall
move 24 columns to the left to get to the first column
move 31 columns down to hit goal
5*37
'''
