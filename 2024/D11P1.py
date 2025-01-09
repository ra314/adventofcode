import reader
content = reader.read()

stones = list(map(int, content.strip().split()))

def process(stone: int) -> list[int]:
  if stone == 0:
    return [1]
  str_stone = str(stone)
  if len(str_stone)%2 == 0:
    return [int(str_stone[:len(str_stone)//2]), int(str_stone[len(str_stone)//2:])]
  return [2024*stone]

def blink(stones: list[int]) -> list[int]:
  retval = []
  for stone in stones:
    retval.extend(process(stone))
  return retval

num_blinks = 25
for _ in range(num_blinks):
  stones = blink(stones)

print(len(stones))
