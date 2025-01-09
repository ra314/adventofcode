import reader
import networkx as nx
from multiprocessing import Pool
import tqdm
content = reader.read()
content = [list(line) for line in content.splitlines()]

def construct_graph(content: list[list[str]]) -> nx.Graph:
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
  return graph, start, end

graph, start, end = construct_graph(content)

def solve(s: tuple[int, int], e: tuple[int, int]) -> int:
 return nx.shortest_path_length(graph, s, e)

def manhattan(a: tuple[int, int], b: tuple[int, int]) -> int:
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

no_cheat_dist = solve(start, end)
cheats = []
non_walls = []
for y in range(len(content)):
  for x in range(len(content[y])):
    if content[y][x] != '#':
      non_walls.append((x, y))
for i in range(len(non_walls)):
  # Progress print
  if i % 100 == 0:
    print(i)
  for j in range(i+1, len(non_walls)):
    if manhattan(non_walls[i], non_walls[j]) <= (20+20):
      cheats.append((non_walls[i], non_walls[j]))
to_end_cache = {}
from_start_cache = {}
print(len(non_walls))
for i in range(len(non_walls)):
  if i % 100 == 0:
    print(i)
  non_wall = non_walls[i]
  to_end_cache[non_wall] = solve(non_wall, end)
  from_start_cache[non_wall] = solve(start, non_wall)

# Use multiprocessing to speed up the search.
def solve_with_cheat(cheat: tuple[tuple[int, int], tuple[int, int]]) -> int:
  return from_start_cache[cheat[0]] + manhattan(cheat[0], cheat[1]) + to_end_cache[cheat[1]]

# Use tqdm to show progress.
# pool = Pool(processes=64)
# dists = list(tqdm.tqdm(pool.imap_unordered(solve_with_cheat, cheats), total=len(cheats)))

def count_cheats(dists: list[int], required_savings: int) -> int:
  return sum(1 for dist in dists if (no_cheat_dist-dist) >= (required_savings))

dists = []
print(len(cheats))
for i in range(len(cheats)):
  if i % 10000 == 0:
    print(i)
  dists.append(solve_with_cheat(cheats[i]))
print(dists)

print(count_cheats(dists, 50))
