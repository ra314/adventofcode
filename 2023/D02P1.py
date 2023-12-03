f1 = open("sample.txt")
f2 = open("real.txt")
import re
content = f1.read()

counts = {'red': 12, 'green':13, 'blue':14}

def is_game_possible(line):
  for round in line.split(';'):
    for colornum in round.split(','):
      num, color = colornum.split()
      num = int(num)
      if counts[color] < num:
        return False
  return True

ids = []
for line in content.splitlines():
  id, line = re.findall(r'Game (\d+):(.*)', line)[0]
  if is_game_possible(line):
    ids.append(int(id))

print(sum(ids))
