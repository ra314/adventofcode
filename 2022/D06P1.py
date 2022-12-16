# num, frm, to = list(map(int, re.search(r'move (\d+) from (\d+) to (\d+)', line).groups()))

import re
myfile = open("input.txt")
content = myfile.read()
content = content.strip()

for i in range(len(content)):
  if len(set(content[i:i+4])) == 4:
    break

print(i+1)

