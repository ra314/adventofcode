import numpy as np
import re
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Rule:
  value: str
  op: str
  literal: int
  exit: str

f1 = open("1in.txt", "r")
f2 = open("2in.txt", "r")
content = f1.read()

workflows = content.split("\n\n")[0].splitlines()

def workflow_str_to_workflow(workflow):
  name = workflow.split("{")[0]
  rules = workflow[:-1].split("{")[1].split(',')
  new_rules = []
  for rule in rules:
    if ":" in rule:
      value, op, literal, exit = re.findall(r'(.)(<|>)(\d+):(.*)', rule)[0]
      new_rules.append(Rule(value, op, int(literal), exit))
    else:
      new_rules.append(Rule(None, None, 0, rule))
  return name, new_rules

graph = defaultdict(list)
for workflow in workflows:
  name, rules = workflow_str_to_workflow(workflow)
  prev = name
  for i, rule in enumerate(rules):
    if rule.op == None:
      graph[prev].append(rule)
    elif "@" in prev:
      graph[prev].append(rule)
      graph[prev].append(rules[i-1].exit)
    else:
      graph[prev].append(rule)
    if i+1 != len(rules):
      prev = name+"@"+rule.value

for key, value in graph.items():
  print(key, value)

part = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}

def combos(part):
  return np.prod([x[1]-x[0]+1 for x in part.values()])

def dfs(part, curr, x):
  total = 0
  edges = None
  if curr is Rule:
    edges = graph[curr]
  else:
    edges = graph[curr]
  for edge in edges:
    #print(part, edge, type(edge) is Rule, x)
    if type(edge) is Rule:
      new_part = part.copy()
      mn, mx = new_part[edge.value]
      
      if edge.op == ">":
        new_part[edge.value] = (max(mn, min(edge.literal+1,4000)), mx)
        total += dfs(new_part, rule.exit, x+1)
        new_part[edge.value] = (mn, min(mx, edge.literal))
        total += dfs(new_part, rule.exit, x+1)
      elif edge.op == "<":
        new_part[edge.value] = (mn, min(mx, max(edge.literal-1,0)))
        total += dfs(new_part, rule.exit, x+1)
        new_part[edge.value] = (max(mn, edge.literal), mx)
        total += dfs(new_part, rule.exit, x+1)
      else:
        assert(False)
    else:
      if edge == "A":
        total += combos(part)
      elif edge == "R":
        total += 0
      else:
        total += dfs(part, edge, x+1)
  return total
    

print(dfs(part, "in", 0))





