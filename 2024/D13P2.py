import reader
content = reader.read()

import re
import numpy as np
def nums(line: str) -> list[int]:
  return list(map(int, re.findall(r'-?\d+', line)))

from fractions import Fraction

a_cost = 3
b_cost = 1
def calc_game_cost(game: str) -> int:
  sol = solve_game(game)
  if sol is None:
    return 0
  print("SOL: ", sol)
  return a_cost*sol[0] + b_cost*sol[1]

def solve_game(game: str):
  a, b, prize = parse_game(game)
  a1, a2 = a
  b1, b2 = b
  
  A = np.array([[a1, b1], [a2, b2]])
  B = np.array(prize)
  x = np.linalg.solve(A, B)
  print(x[0], x[1])
  
  fractions = [Fraction(val).limit_denominator(1000) for val in x]
  denominators = [frac.denominator for frac in fractions]
  lcm = np.lcm.reduce(denominators)

  # Scale the solution to integers
  integer_solution = [frac.numerator * (lcm // frac.denominator) for frac in fractions]
  print("Integer solution:", integer_solution)

  # Verify the integer solution
  scaled_A = A * lcm
  scaled_B = B * lcm
  is_valid = np.allclose(np.dot(scaled_A, integer_solution), scaled_B)
  if is_valid:
    return integer_solution
  else:
    return None

def parse_game(game: str):
  game = game.splitlines()
  a = nums(game[0])
  b = nums(game[1])
  prize = nums(game[2])
  prize = [prize[0] + 10000000000000, prize[1] + 10000000000000]
  return a, b, prize

total_cost = 0
for game in content.split("\n\n"):
  cost = calc_game_cost(game)
  total_cost += cost

print(int(total_cost))

