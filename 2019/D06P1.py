myfile = open("input2.txt")
content = myfile.read()
from collections import defaultdict

graph = defaultdict(list)

for line in content.splitlines():
  line = line.split(")")
  assert(len(line)==2)
  graph[line[0]].append(line[1])

root = "COM"

def count(node):
  total = 0
  for child in graph[node]:
    total += (1 + count(child))
  return total

counts = [count(node) for node in list(graph.keys())]
print(sum(counts))
