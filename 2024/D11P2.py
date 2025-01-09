import reader
content = reader.read()

from collections import Counter
from functools import lru_cache

stones = list(map(int, content.strip().split()))
stones = Counter(stones)

@lru_cache(maxsize=1000)
def process(stone: int) -> list[int]:
  if stone == 0:
    return [1]
  str_stone = str(stone)
  if len(str_stone)%2 == 0:
    return [int(str_stone[:len(str_stone)//2]), int(str_stone[len(str_stone)//2:])]
  return [2024*stone]

def blink(stones: dict[int, int]) -> dict[int, int]:
  retval = {}
  for stone, count in stones.items():
    new_stones = process(stone)
    for new_stone in new_stones:
      retval[new_stone] = retval.get(new_stone, 0) + count
  return retval

num_blinks = 75
for i in range(num_blinks):
  stones = blink(stones)
  print(i, sum(stones.values()))

print(sum(stones.values()))
