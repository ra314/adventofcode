myfile = open("input.txt")
content = myfile.read()

total = 0
for line in content.splitlines():
  a, b = line.split(",")
  a1, a2 = list(map(int, a.split("-")))
  b1, b2 = list(map(int, b.split("-")))
  if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
    total += 1

print(total)
