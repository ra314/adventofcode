import reader
import networkx as nx
content = reader.read()

codes = content.splitlines()

class Keypad:
  dir_to_char = {(0,1): "v", (0,-1): "^", (1,0): ">", (-1,0): "<"}
  char_to_dir = {"v": (0,1), "^": (0,-1), ">": (1,0), "<": (-1,0)}
  directional_keys = [[".", "^", "A"], ["<", "v", ">"]]
  numeric_keys = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], [".", "0", "A"]]
  directional_ordering = "v><^"
  numeric_ordering = ">^<v"
  
  def __init__(self, _is_numeric: bool):
    rows = Keypad.numeric_keys if _is_numeric else Keypad.directional_keys
    self.is_numeric = _is_numeric
    self.char_to_pos = Keypad.map_pad(rows)
    self.pos_to_char = {v: k for k, v in self.char_to_pos.items()}
    self.graph = Keypad.to_graph(self.char_to_pos)
    
  @staticmethod
  def to_graph(mapping: dict[str, tuple[int, int]]) -> nx.Graph:
    g = nx.Graph()
    for c1, p1 in mapping.items():
      for c2, p2 in mapping.items():
        if c1 == c2:
          continue
        if c1 == "." or c2 == ".":
          continue
        if Keypad.manhattan_distance(p1, p2) == 1:
          g.add_edge(p1, p2)
    return g
  
  @staticmethod
  def map_pad(pad: list[list[str]]) -> dict[str, tuple[int, int]]:
    char_to_pos = {}
    for y, row in enumerate(pad):
      for x, char in enumerate(row):
        char_to_pos[char] =  (x, y)
    return char_to_pos
  
  @staticmethod
  def manhattan_distance(start: tuple[int, int], end: tuple[int, int]) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])
  
  def sort_path(self, path: list[str]) -> list[str]:
    ordering = Keypad.numeric_ordering if self.is_numeric else Keypad.directional_ordering
    return sorted(path, key=lambda x: ordering.index(x))
  
  @staticmethod
  def add_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return (t1[0] + t2[0], t1[1] + t2[1])
  
  @staticmethod
  def subtract_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
    return (t1[0] - t2[0], t1[1] - t2[1])
  
  def calc_path(self, start: str, end: str) -> list[str]:
    spos = self.char_to_pos[start]
    epos = self.char_to_pos[end]
    path = nx.shortest_path(self.graph, spos, epos)
    retval = []
    for i in range(len(path)-1):
      retval.append(Keypad.dir_to_char[Keypad.subtract_tuple(path[i+1], path[i])])
    return self.sort_path(retval)
  
  def calc_full_path(self, seq: str) -> list[str]:
    retval = []
    for i in range(len(seq)-1):
      prev, curr = seq[i], seq[i+1]
      retval.extend(self.calc_path(prev, curr))
      retval.append("A")
    return "".join(retval)
  
  def decode(self, seq: str) -> list[str]:
    retval = []
    curr = self.char_to_pos["A"]
    for c in seq:
      if c == "A":
        retval.append(self.pos_to_char[curr])
        continue
      curr = Keypad.add_tuple(curr, self.char_to_dir[c])
    return "".join(retval)

numpad = Keypad(True)
dirpad = Keypad(False)

# Returns the sequence needed to enter a code
def solve_code(code: str) -> str:
  numpath = numpad.calc_full_path("A"+code)
  dirpath1 = dirpad.calc_full_path("A"+numpath)
  dirpath2 = dirpad.calc_full_path("A"+dirpath1)
  print(code)
  print(numpath)
  print(dirpath1)
  print(dirpath2)
  return dirpath2

def score_code(code: str) -> int:
  seq = solve_code(code)
  print(len(seq))
  return len(seq) * int(code[:-1])

scores = [score_code(code) for code in codes]
print(scores)
print(sum(scores))
