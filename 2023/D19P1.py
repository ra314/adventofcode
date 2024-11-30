import numpy as np
import re

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f2.read()

workflows = content.split("\n\n")[0].splitlines()
parts = content.split("\n\n")[1].splitlines()

def part_str_to_part(part):
  part = part.replace("=","':")
  part = part.replace("{","{'")
  part = part.replace(",",",'")
  return eval(part)

parts = [part_str_to_part(part) for part in parts]



def workflow_str_to_workflow(workflow):
  name = workflow.split("{")[0]
  rules = workflow[:-1].split("{")[1].split(',')
  return name, rules

workflows_new = {}
for workflow in workflows:
  name, rules = workflow_str_to_workflow(workflow)
  workflows_new[name] = rules
workflows = workflows_new

good_parts = []
for part in parts:
  name, index = "in", 0
  #print()
  while True:
    if name == "R" or name == "A":
      break
    rule = workflows[name][index]
    #print(name, rule)
    if rule == "R" or rule == "A":
      break
    if ":" not in rule:
      name = rule
      index = 0
      continue
    
    passed = False
    value = part[rule[0]]
    #print(value)
    if rule[1] == ">":
      passed = value>int(rule[2:].split(":")[0])
    elif rule[1] == "<":
      passed = value<int(rule[2:].split(":")[0])
    else:
      assert(False)
    
    if passed:
      name = rule.split(":")[1]
      index = 0
    else:
      index += 1
    
  if rule == "A" or name == "A":
    good_parts.append(part)

print(good_parts)
print(sum([sum(x.values()) for x in good_parts]))




