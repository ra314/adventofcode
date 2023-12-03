f1 = open("sample.txt")
f2 = open("real.txt")
content = f2.read()
from collections import defaultdict

def game_power(line):
  counts = defaultdict(int)
  line = line.split(":")[1]
  rounds = line.split(";")
  for round in rounds:
    colornums = round.split(',')
    for colornum in colornums:
      num, color = colornum.split()
      num = int(num)
      if counts[color] < num:
        counts[color] = num
  nums = list(counts.values())
  return nums[0]*nums[1]*nums[2]

ids = []
for line in content.splitlines():
  id = int(line.split()[1][:-1])
  ids.append(game_power(line))

print(sum(ids))
