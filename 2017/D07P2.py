myfile = open("input.txt")
content = myfile.read()
import itertools
from collections import Counter

dic = {}
weights = {}
for line in content.splitlines():
  if "->" in line:
    children = line.split('->')[1].split()
    children[-1] = children[-1] + ','
    for i in range(len(children)):
      children[i] = children[i][:-1]
    dic[line.split()[0]] = children
  else:
    dic[line.split()[0]] = []
  weights[line.split()[0]] = int(line.split()[1][1:-1])

def get_weight(name):
  if dic[name] == []:
    return weights[name]
  else:
    retval = weights[name]
    for child_name in dic[name]:
      retval += get_weight(child_name)
    return retval

def get_parent(name):
  for key, value in dic.items():
    if name in value:
      return key

root = list(set(dic.keys()) - set(itertools.chain.from_iterable(dic.values())))[0]
curr = root
while dic[curr]:
  ws = [get_weight(x) for x in dic[curr]]
  odd_one = dic[curr][ws.index(Counter(ws).most_common()[-1][0])]
  curr = odd_one
  if len(set(ws))==1:
    break
