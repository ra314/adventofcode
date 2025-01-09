import reader
import networkx as nx
from multiprocessing import Pool
content = reader.read()

def solve(content: list[list[str]]) -> int:
  graph = nx.Graph()
  start = (0, 0)
  end = (0,0)
  for y in range(len(content)):
    for x in range(len(content[y])):
      if content[y][x] != '#':
        curr = (x,y)
        # Check adjacent positions and add edges
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
          fx, fy = x + dx, y + dy
          if 0 <= fy < len(content) and 0 <= fx < len(content[y]) and content[fy][fx] != '#':
            graph.add_edge(curr, (fx, fy))
      if content[y][x] == 'S':
        start = (x, y)
      if content[y][x] == 'E':
        end = (x, y)
  return nx.shortest_path_length(graph, start, end)

walls = []
cl = [list(line) for line in content.splitlines()]
for y in range(len(cl)):
  for x in range(len(cl[y])):
    if cl[y][x] == '#':
      walls.append((x, y))

no_cheat_dist = solve(cl)

# Use multiprocessing to speed up the search.
def shorter_than_target(wall: tuple[int, int]) -> bool:
  cl = [list(line) for line in content.splitlines()]
  wx, wy = wall
  cl[wy][wx] = '.'
  dist = solve(cl)
  return dist < (no_cheat_dist-99)

bools = []
with Pool(32) as pool:
  bools = list(pool.map(shorter_than_target, walls))

print(sum(bools))
