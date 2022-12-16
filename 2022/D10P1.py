import re
myfile = open("input.txt")
content = myfile.read()

x = 1
cycle = 1
values = []

def log_x(cycle):
  if (cycle-20)%40 == 0:
    values.append(x*cycle)

for line in content.splitlines():
  match line.split()[0]:
    case "noop":
      cycle += 1
      log_x(cycle)
    case "addx":
      cycle += 1
      log_x(cycle)
      cycle += 1
      x += int(line.split()[-1])
      log_x(cycle)

print(sum(values))
