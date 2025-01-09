import reader
content = reader.read()

import networkx as nx
import itertools
import math
graph = nx.Graph()
for line in content.splitlines():
  line = line.split("-")
  graph.add_edge(line[0], line[1])

def has_t(x):
  return sum([n[0]=="t" for n in x]) > 0

cliques = nx.enumerate_all_cliques(graph)
cliques_with_t = filter(has_t, cliques)
max_clique = max(cliques_with_t, key=lambda x: len(x))
print(",".join(sorted(max_clique)))
