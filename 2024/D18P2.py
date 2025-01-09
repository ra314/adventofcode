import reader
import networkx as nx


def run(num_bytes: int):
  content = reader.read()

  content = content.splitlines()
  is_real_input = len(content) > 50

  grid_size = (7,7)
  if is_real_input:
    grid_size = (71, 71)
  content = content[:num_bytes]

  corrupted_cells = set()
  for line in content:
    x, y = list(map(int, line.split(",")))
    corrupted_cells.add((x,y))

  def is_in_bounds(x, y):
    return x >= 0 and x < grid_size[0] and y >= 0 and y < grid_size[1]

  def add_edge(graph, p1, p2):
    if p1 in corrupted_cells or p2 in corrupted_cells:
      return
    if is_in_bounds(p1[0], p1[1]) and is_in_bounds(p2[0], p2[1]):
      graph.add_edge(p1, p2)

  maxx, maxy = grid_size
  graph = nx.Graph()
  for x in range(maxx):
    for y in range(maxy):
      # Add connections between adjacent grid cells 
      curr = (x,y)
      add_edge(graph, curr, (x+1,y))
      add_edge(graph, curr, (x-1,y))
      add_edge(graph, curr, (x,y+1))
      add_edge(graph, curr, (x,y-1))

  # Find a path from top left to bottom right
  path = nx.shortest_path(graph, (0,0), (maxx-1, maxy-1))
  return len(path)

i = 10
while True:
  i += 1
  print(i)
  print(run(i))
