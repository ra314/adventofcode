import reader
content = reader.read()

towels, targets = content.split("\n\n");
towels = set(towels.split(", "))
targets = targets.splitlines()

cache: dict[str, bool] = {}
def is_possible(target: str) -> bool:
  if target in cache:
    return cache[target]
  if target in towels:
    cache[target] = True
    return True
  if len(target) == 1:
    cache[target] = False
    return False
  for i in range(1, len(target)):
    x, y = target[:i], target[i:]
    if is_possible(x) and is_possible(y):
      cache[target] = True
      return True
  cache[target] = False
  return False

count = 0
for target in targets:
  pos = is_possible(target)
  count += pos
  print(target, pos)
print(count)
