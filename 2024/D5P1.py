import reader
content = reader.read()

from collections import defaultdict

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

total = 0
for page_update in page_updates:
  if is_valid_page(page_update):
    total += page_update[len(page_update)//2]

print(total)
