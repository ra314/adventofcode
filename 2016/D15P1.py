from typing import List
from typing import NamedTuple

class Disc(NamedTuple):
    num_pos: int
    curr_pos: int

content = open("input2.txt").read()

# Array of tuple of num positions and current position
discs: List[Disc] = []
for line in content.splitlines():
  line = line.split()
  discs.append(Disc(int(line[3]), int(line[-1][:-1])))

curr_lcm = 1
passed_seconds = 0
for i, disc in enumerate(discs):
  while (disc.curr_pos + passed_seconds + i + 1)%disc.num_pos != 0:
    passed_seconds += curr_lcm
  curr_lcm = lcm(*[disc.num_pos for disc in discs[:i+1]])
