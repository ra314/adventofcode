import reader
content = reader.read()

import networkx as nx
import itertools
import math
graph = nx.Graph()
for line in content.splitlines():
  line = line.split("-")
  graph.add_edge(line[0], line[1])

triplets = set()
for node in graph.nodes():
  for n1 in graph.neighbors(node):
    for n2 in graph.neighbors(node):
      if n1 == n2:
        continue
      if graph.has_edge(n1, n2) or graph.has_edge(n2, n1):
        triplet = tuple(sorted([node, n1, n2]))
        if n1[0] == "t" or n2[0] == "t" or node[0] == "t":
          triplets.add(triplet)
print(triplets)
print(len(triplets))
