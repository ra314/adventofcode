import reader
content = reader.read()

from collections import defaultdict
from functools import cmp_to_key

rules, page_updates = content.split("\n\n")
rules = [list(map(int, line.split("|"))) for line in rules.splitlines()]
page_updates = [list(map(int, line.split(","))) for line in page_updates.splitlines()]

rules_dict = defaultdict(list)
for rule in rules:
  rules_dict[rule[0]].append(rule[1])

def is_valid_page(page_update):
  for i in range(len(page_update)):
    num = page_update[i]
    for after in rules_dict[num]:
      if after in page_update[:i]:
        return False
  return True

def cmp(x, y):
  if y in rules_dict[x]:
    return 1
  elif x in rules_dict[y]:
    return -1
  else:
    return 0

def sort_page(page_update):
  return sorted(page_update, key=cmp_to_key(cmp))

total = 0
for page_update in page_updates:
  if not is_valid_page(page_update):
    print(page_update)
    new = sort_page(page_update)
    total += new[len(page_update)//2]

print(total)
