myfile = open("input.txt")
content = myfile.read()
import re

size = 9
towers = [[] for i in range(size)]
parsing_towers = True
for line in content.splitlines():
  if line == "":
    parsing_towers = False
    continue
  if parsing_towers:
    for i in range(size):
      idx = 1+(i*4)
      if line[idx] != " " and line[idx].isalpha():
        towers[i].append(line[idx])
  else:
    num, frm, to = list(map(int, re.search(r'move (\d+) from (\d+) to (\d+)', line).groups()))
    frm -= 1
    to -= 1
    for i in range(num):
      towers[to].insert(0, towers[frm].pop(0))
    print(towers)

crates = []
for tower in towers:
  crates.append(tower[0])

print("".join(crates))
