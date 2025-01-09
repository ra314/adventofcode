import reader
from functools import lru_cache
content = reader.read()

towels, targets = content.split("\n\n");
towels = set(towels.split(", "))
targets = targets.splitlines()

@lru_cache(maxsize=None)
def count(target: str) -> int:
  if target == "":
    return 1
  total = 0
  for towel in towels:
    if target.startswith(towel):
      total += count(target[len(towel):])
  return total

total = 0
for target in targets:
  c = count(target)
  total += c
  print(target, c)
print(total)
