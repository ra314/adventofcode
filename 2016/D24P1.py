myfile = open("input3.txt")
content = myfile.read()

matrix = []
targets = {}

for i, line in enumerate(content.splitlines()):
  grid_line = []
  for j, char in enumerate(line):
    if char == "#":
      grid_line.append(0)
    elif char == ".":
      grid_line.append(1)
    elif char.isdigit():
      grid_line.append(1)
      targets[int(char)] = [i,j]
  matrix.append(grid_line)

# "#" = 0, "." = 1

from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

grid = Grid(matrix=matrix)
finder = DijkstraFinder()

start = grid.node(9, 1)
end = grid.node(9, 3)
path, runs = finder.find_path(start, end, grid)
print(len(path))

distance_matrix = []
for target1 in targets.keys():
  line = []
  for target2 in targets.keys():
    start = grid.node(*targets[target1][::-1])
    end = grid.node(*targets[target2][::-1])
    path, runs = finder.find_path(start, end, grid)
    line.append(len(path))
  distance_matrix.append(line)
