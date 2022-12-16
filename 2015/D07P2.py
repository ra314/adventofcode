myfile = open("input2.txt")
content = myfile.read()

from functools import lru_cache
value_to_rule = {}
for line in content.splitlines():
  line = line.split('->')
  value_to_rule[line[1].strip()] = line[0].strip().split()

@lru_cache
def calculate_value(wire_name):
  if wire_name.isdigit():
    return int(wire_name)
  rule = value_to_rule[wire_name]
  #print(rule)
  if len(rule) == 1:
    if rule[0].isdigit():
      return int(rule[0])
    else:
      return calculate_value(rule[0])
  elif len(rule) == 2:
    return ~calculate_value(rule[1]) & 0xffff
  elif len(rule) == 3:
    if rule[1] == "AND":
      return calculate_value(rule[0]) & calculate_value(rule[2])
    elif rule[1] == "OR":
      return calculate_value(rule[0]) | calculate_value(rule[2])
    elif rule[1] == "RSHIFT":
      return calculate_value(rule[0]) >> int(rule[2])
    elif rule[1] == "LSHIFT":
      return calculate_value(rule[0]) << int(rule[2])

print(calculate_value('a'))
