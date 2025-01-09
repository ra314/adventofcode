import reader
content = reader.read()

class Moveable:
  all = {}
  grid: list[str]
  walls = set()
  robot = None
  
  def initialize(_grid):
    Moveable.grid = _grid
    for y in range(len(Moveable.grid)):
      for x in range(len(Moveable.grid[0])):
        char = Moveable.grid[y][x]
        pos = (x, y)
        if char == "@" or char == "O":
          mover = Moveable(pos, char)
          Moveable.all[pos] = mover
          if char == "@":
            Moveable.robot = mover
        elif char == "#":
          Moveable.walls.add(pos)
  
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

  def move_robot(dir: str) -> bool:
    return Moveable.robot.move(dir)

  def move(self, dir: str) -> bool:
    npos = self.new_position(dir)
    if npos in Moveable.walls:
      return False
    if npos in Moveable.all:
      if not Moveable.all[npos].move(dir):
        return False
    del Moveable.all[self.position]
    self.position = npos
    Moveable.all[self.position] = self
    return True
  
  def __str__(self):
    return f"{self.char}({self.position})"
  
  def print_grid() -> str:
    string = ""
    for y in range(len(Moveable.grid)):
      for x in range(len(Moveable.grid[0])):
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
    x, y = self.position
    return (y*100)+x
  
  def total_score() -> int:
    return sum(map(lambda x: x.score(), Moveable.all.values()))

grid, moves = content.split("\n\n")
grid = grid.splitlines()
Moveable.initialize(grid)

print(Moveable.print_grid())
for move in moves.replace("\n", ""):
  Moveable.move_robot(move)
  print(move)
  print(Moveable.print_grid())

print(Moveable.total_score())
