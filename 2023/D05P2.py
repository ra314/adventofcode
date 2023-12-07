import numpy as np
from collections import defaultdict
import re
from math import inf
import portion as P

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f1.read()

content = content.split("\n\n")
seeds = list(map(int, content[0].split(":")[1].split()))
seed_range = P.empty()
for i in range(0, len(seeds), 2):
  seed_range = seed_range | (P.closed(seeds[i],seeds[i]+seeds[i+1]-1))

print(seed_range)
maps = content[1:]

def convert_map(almap):
  almap = almap.splitlines()
  name = almap[0].split()[0]
  almap = almap[1:]
  return [name, list(map(lambda x: list(map(int, x.split())), almap))]

maps = list(map(convert_map, maps))

#def convert(seed_range, almap):
for almap in maps:
  output_seed_range = P.empty()
  for rangex in almap[1]:  
    dest, source, length = rangex
    map_interval = P.closed(source, source+length-1)
    inter = seed_range & map_interval
    #print("X", map_interval, inter)
    if inter:
      seed_range = seed_range - inter
      inter = inter.apply(lambda x: (x.left, dest+x.lower-source, dest+x.upper-source, x.right))
      output_seed_range = output_seed_range | inter
      #print("Y", output_seed_range)
  seed_range = output_seed_range | seed_range
  #print("Z", seed_range)
print(seed_range)
