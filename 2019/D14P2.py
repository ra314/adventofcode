myfile = open("input.txt")
content = myfile.read()
from math import ceil
from collections import defaultdict

# Key is the output chemical
# Value is a 2-tuple
# eg: {"C": ([(7, 'A'), (1, 'B')]
#           , (1, 'C'))}
rules = {}

for line in content.splitlines():
  line = line.split("=>")
  reactants = line[0].split(',')
  product = line[1].split()
  
  reactants_list = []
  for reactant in reactants:
    reactant = reactant.split()
    reactants_list.append((int(reactant[0]), reactant[1]))
  rules[product[1]] = (reactants_list, (int(product[0]), product[1]))

reactant_stockpile = defaultdict(int)
def get_ore_cost(product, amount_needed, initial_call: bool):
  global reactant_stockpile
  
  if initial_call:
    reactant_stockpile = defaultdict(int)
  
  #print(reactant_stockpile, product, amount_needed)
  
  if reactant_stockpile[product] > amount_needed:
    reactant_stockpile[product] -= amount_needed
    amount_needed = 0
  else:
    amount_needed -= reactant_stockpile[product]
    reactant_stockpile[product] = 0
  
  if amount_needed == 0:
    return 0
  
  if product == "ORE":
    return amount_needed
  
  # Suppose you have 1 ORE => 5 B, but you want 7 B
  # Then you need to perform the reaction twice and will have 3 B leftover
  times_reaction_performed = ceil(amount_needed/rules[product][1][0])
  product_produced = times_reaction_performed * rules[product][1][0]
  leftover_product = product_produced - amount_needed
  reactant_stockpile[product] += (leftover_product)
  
  #print(product, times_reaction_performed, product_produced, leftover_product)
  
  ore_cost = 0
  for reactant in rules[product][0]:
    ore_cost += (get_ore_cost(reactant[1], times_reaction_performed * reactant[0], False))
  
  return ore_cost

from math import inf
def binary_search_maximise():
  lower_bound = 0
  upper_bound = inf
  prev_num = 1
  num = 1
  while True:
    cost = get_ore_cost("FUEL", num, True)
    if cost < 1000000000000:
      lower_bound = num
    else:
      upper_bound = num
    
    if upper_bound != inf:
      num = int((upper_bound + lower_bound)/2)
    else:
      num *= 2
      
    print(num, lower_bound, upper_bound)
    
    if prev_num == num:
      return num
    prev_num = num

binary_search_maximise()
