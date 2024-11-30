f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

total = 0
for line in content.splitlines():
  line = list(filter(lambda x: x.isdigit(), line))
  print(line)
  total += int(line[0] + line[-1])

print(total)
