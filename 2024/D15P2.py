import reader
content = reader.read()
import os
import time

class Moveable:
  all = {}
  grid_size: tuple[int, int]
  walls = set()
  robot = None
  
  def initialize(_grid):
    maxx, maxy = (len(_grid[0]), len(_grid))
    for y in range(maxy):
      for x in range(maxx):
        char = _grid[y][x]
        pos = (x*2, y)
        adj_pos = ((x*2)+1, y)
        if char == "@":
          mover = Moveable(pos, char)
          Moveable.robot = mover
          Moveable.all[pos] = mover
        elif char == "O":
          Moveable.all[pos] = Moveable(pos, "[")
          Moveable.all[adj_pos] = Moveable(adj_pos, "]")
        elif char == "#":
          Moveable.walls.add(pos)
          Moveable.walls.add(adj_pos)
    Moveable.grid_size = (maxx*2, maxy)
  
  def __init__(self, position: tuple[int, int], char: str):
    self.position = position
    self.char = char
  
  def new_position(self, dir:str) -> tuple[int, int]:
    x,y = self.position
    if dir == "^":
      return (x, y-1)
    elif dir == "v":
      return (x, y+1)
    elif dir == "<":
      return (x-1, y)
    elif dir == ">":
      return (x+1, y)
    assert(False)
  
  def get_pair(self):
    assert(self.char == "[" or self.char == "]")
    x, y = self.position
    if self.char == "[":
      return (self, Moveable.all[(x+1, y)])
    return (Moveable.all[(x-1, y)], self)

  def can_move_alone(self, dir: str) -> bool:
    npos = self.new_position(dir)
    if npos in Moveable.walls:
      return False
    if npos in Moveable.all:
      return Moveable.all[npos].can_move(dir)
    return True

  def can_move(self, dir: str) -> bool:
    if self.char == "@":
      return self.can_move_alone(dir)
    elif self.char == "[" or self.char == "]":
      if dir == "<" or dir == ">":
        return self.can_move_alone(dir)
      p1, p2 = self.get_pair()
      return p1.can_move_alone(dir) and p2.can_move_alone(dir)
    assert(False)
  
  def move(self, dir: str):
    npos = self.new_position(dir)
    if npos in Moveable.all:
     pair = Moveable.all[npos].get_pair()
     if dir == "<":
       pair[0].move(dir)
       pair[1].move(dir)
     else:
       pair[1].move(dir)
       pair[0].move(dir)
    del Moveable.all[self.position]
    self.position = npos
    Moveable.all[self.position] = self
    return True

  def move_robot(dir: str):
    if Moveable.robot.can_move(dir):
      Moveable.robot.move(dir)
  
  def __str__(self):
    return f"{self.char}({self.position})"
  
  def print_grid() -> str:
    string = ""
    maxx, maxy = Moveable.grid_size
    for y in range(maxy):
      for x in range(maxx):
        position = (x, y)
        if position in Moveable.all:
          char = Moveable.all[position].char
        elif position in Moveable.walls:
          char = "#"
        else:
          char = "."
        string += char
      string += "\n"
    return string
  
  def score(self) -> int:
    if self.char == "@":
      return 0
    if self.char == "]":
      return 0
    x, y = self.position
    return (y*100)+x
  
  def total_score() -> int:
    return sum(map(lambda x: x.score(), Moveable.all.values()))

grid, moves = content.split("\n\n")
grid = grid.splitlines()
Moveable.initialize(grid)

print(Moveable.print_grid())
for i, move in enumerate(moves.replace("\n", "")):
  Moveable.move_robot(move)
  os.system('cls' if os.name == 'nt' else 'clear')
  print(move, i)
  print(Moveable.print_grid())
  time.sleep(1/60)

print(Moveable.total_score())
