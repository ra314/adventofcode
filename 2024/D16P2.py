import reader
content = reader.read()

import networkx as nx
from math import inf

# Each cell on the grid is represented as pos + facing direction.
# The position infront of you is connected with a cost of 1.
# The position behind you is connected with a cost of 2000.
# Positions to the left and right are connected with a cost of 1000.

def is_wall(char: str) -> bool:
  return char == "#"

dirs = ["<", "^", ">", "v"]

def get_next(pos: tuple[int, int], dir: str) -> tuple[int, int]:
  x, y = pos
  if dir == "<":
    x -= 1
  elif dir == ">":
    x += 1
  elif dir == "^":
    y -= 1
  elif dir == "v":
    y += 1
  return (x, y)

content = content.splitlines()
graph = nx.Graph()
start = (0, 0)
end = (0, 0)
for y in range(len(content)):
  for x in range(len(content[0])):
    char = content[y][x]
    pos = (x, y)
    if is_wall(char):
      continue
    if char == "S":
      start = pos
    elif char == "E":
      end = pos
    # Add edges to adjacent cells.
    for dir in dirs:
      nxt = get_next(pos, dir)
      if is_wall(content[nxt[1]][nxt[0]]):
        continue
      graph.add_edge((pos, dir), (nxt, dir), cost=1)
    # Add edges for rotation.
    graph.add_edge((pos, "^"), (pos, ">"), cost=1000)
    graph.add_edge((pos, ">"), (pos, "v"), cost=1000)
    graph.add_edge((pos, "v"), (pos, "<"), cost=1000)
    graph.add_edge((pos, "<"), (pos, "^"), cost=1000)
    # And counter clocking edges.
    #graph.add_edge((pos, "^"), (pos, "<"), cost=1000)
    #graph.add_edge((pos, "<"), (pos, "v"), cost=1000)
    #graph.add_edge((pos, "v"), (pos, ">"), cost=1000)
    #graph.add_edge((pos, ">"), (pos, "^"), cost=1000)

def get_num_tiles_in_paths(paths) -> int:
  tiles = set()
  num_paths = 0
  for path in paths:
    num_paths += 1
    for pos, dir in path:
      tiles.add(pos)
  print(num_paths)
  return len(tiles)

def find_shortest_path_cost(graph: nx.DiGraph, start: tuple[int, int], end: tuple[int, int]):
  start_with_dir = (start, ">")
  min_cost = inf
  min_path = None
  for dir in dirs:
    end_with_dir = (end, dir)
    try:
      paths = nx.all_shortest_paths(graph, start_with_dir, end_with_dir, weight="cost")
      if paths is None:
        continue
      cost = nx.shortest_path_length(graph, start_with_dir, end_with_dir, weight="cost")
      if cost < min_cost:
        min_cost = cost
        min_path = paths
    except nx.NetworkXNoPath:
      continue
  return min_cost, min_path

# Solution.
shortest_paths = find_shortest_path_cost(graph, start, end)
print(get_num_tiles_in_paths(shortest_paths[1]))
