myfile = open("input2.txt")
content = myfile.read()
from dijkstar import Graph, find_path

graph = Graph()
for line in content.splitlines():
  line = line.split(")")
  assert(len(line)==2)
  graph.add_edge(line[0], line[1], 1)
  graph.add_edge(line[1], line[0], 1)

print(find_path(graph, "YOU", "SAN"))
