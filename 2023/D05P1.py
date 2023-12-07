import numpy as np
from collections import defaultdict
import re
from math import inf

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

content = content.split("\n\n")
seeds = list(map(int, content[0].split(":")[1].split()))
maps = content[1:]

def convert_map(almap):
  almap = almap.splitlines()
  name = almap[0].split()[0]
  almap = almap[1:]
  return [name, list(map(lambda x: list(map(int, x.split())), almap))]

maps = list(map(convert_map, maps))
print(maps)

def convert(xseed, xalmap):
  for rangex in xalmap[1]:
    dest, source, length = rangex
    if xseed in range(source, source+length):
      return dest+(xseed-source)
  return xseed

nseeds = []
for seed in seeds:
  nseed = seed
  for almap in maps:
    nseed = convert(nseed, almap)
  nseeds.append(nseed)

print(min(nseeds))
