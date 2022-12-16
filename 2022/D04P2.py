myfile = open("input2.txt")
content = myfile.read()

total = 0
for line in content.splitlines():
  a, b = line.split(",")
  a1, a2 = list(map(int, a.split("-")))
  b1, b2 = list(map(int, b.split("-")))
  if (b1 <= a1 <= b2) or (b1 <= a2 <= b2) or (a1 <= b1 <= a2) or (a1 <= b2 <= a2):
    total += 1

print(total)

### POST HOC
import re

total = 0
for line in content.splitlines():
  a1, a2, b1, b2 = list(map(int, re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line).groups()))
  if (b1 <= a1 <= b2) or (b1 <= a2 <= b2) or (a1 <= b1 <= a2) or (a1 <= b2 <= a2):
    total += 1

print(total)
