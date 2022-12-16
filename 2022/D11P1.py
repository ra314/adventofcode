import re, numpy as np
from collections import defaultdict
myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()

class Monkey:
  monkeys = []

  def __init__(self, items, mod_num, operation, true_receiver, false_receiver):
    self.items = items
    self.mod_num = mod_num
    self.operation = lambda old: eval(operation)
    self.true_receiver = true_receiver
    self.false_receiver = false_receiver
    self.num_inspected = 0
    Monkey.monkeys.append(self)
  
  def inspect(self, item):
    item = self.operation(item)
    item //= 3
    if (item % self.mod_num) == 0:
      Monkey.monkeys[self.true_receiver].items.append(item)
    else:
      Monkey.monkeys[self.false_receiver].items.append(item)
    self.num_inspected += 1
  
  def print_all():
    for monkey in Monkey.monkeys:
      print(monkey)
    print()
  
  def __str__(self):
    return str(self.items)

i = 0
while i < len(content):
  monkey_num = int(re.match(r'Monkey (\d+):', content[i]).groups()[0])
  items = [int(x) for x in content[i+1].split(":")[-1].split(",")]
  operation = content[i+2].split("= ")[-1]
  mod_num = int(content[i+3].split()[-1])
  true_receiver = int(content[i+4].split()[-1])
  false_receiver = int(content[i+5].split()[-1])
  Monkey(items, mod_num, operation, true_receiver, false_receiver)
  i += 7

for i in range(20):
  for monkey in Monkey.monkeys:
    while monkey.items:
      item = monkey.items.pop(0)
      monkey.inspect(item)

levels = [monkey.num_inspected for monkey in Monkey.monkeys]
print(levels)
total = np.prod(sorted(levels)[-2:])
print(total)
