myfile = open("input.txt")
content = myfile.read()

forest = []
import os
from time import sleep

for line in content.splitlines():
  forest.append(list(line))

seen_set = set()
seen_list = []

def forest_to_str(forest):
  return "\n".join(["".join(row) for row in forest])

SIZE = 50
for c in range(1000000000):
  new_forest = []
  for i in range(SIZE):
    new_row = []
    for j in range(SIZE):
      adjs = []
      for x in range(-1, 2):
        for y in range(-1, 2):
          if 0 <= i+x < SIZE and 0 <= j+y < SIZE and (abs(x)+abs(y)!=0):
            adjs.append(forest[i+x][j+y])
      curr = forest[i][j]
      if curr == ".":
        if adjs.count("|") >= 3:
          new_row.append("|")
        else:
          new_row.append(curr)
      elif curr == "|":
        if adjs.count("#") >= 3:
          new_row.append("#")
        else:
          new_row.append(curr)
      elif curr == "#":
        if adjs.count("#") >= 1 and adjs.count("|") >= 1:
          new_row.append("#")
        else:
          new_row.append(".")
    new_forest.append(new_row)
  forest = new_forest
  os.system('clear')
  string = forest_to_str(forest)
  print(string)
  if string in seen_set:
    break
  seen_set.add(string)
  seen_list.append(string)
  

start_of_cycle = seen_list.index(string)
cycle_length = c-start_of_cycle
ending_cycle_index = (1000000000-c)%(cycle_length)
ending_forest = seen_list[start_of_cycle + ending_cycle_index]

from itertools import chain
resources = list(chain.from_iterable(ending_forest))
print(resources.count("#")*resources.count("|"))


