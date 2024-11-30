import numpy as np
import re
from collections import defaultdict
import networkx as nx

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

G = nx.Graph()
for line in content.splitlines():
  a = line.split(": ")[0]
  zs = line.split(": ")[1].split()
  for z in zs:
    G.add_edge(a, z)

print(G)
print(nx.number_connected_components(G))
cuts = nx.minimum_edge_cut(G)
print(cuts)

for cut in cuts:
  G.remove_edge(*cut)

print(G)
components = list(nx.connected_components(G))
print(len(components))
print(len(components[0])*len(components[1]))
