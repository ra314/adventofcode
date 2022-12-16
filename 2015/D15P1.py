import numpy as np
import regex as re

content = open("input2.txt").read()
ingredient_values = []
for line in content.splitlines():
  nums = list(map(int, re.findall(r'-?\d+', line)))[:-1]
  ingredient_values.append(np.array(nums))
ingredient_values = np.array(ingredient_values)
num_ingredients = len(ingredient_values)

def calculate_calories(distribution):
  if not (distribution>=0).all():
    return 0
  return int(np.matmul(distribution.reshape(1,num_ingredients),ingredient_values).prod())

distribution = np.array([100//num_ingredients]*num_ingredients)

def pick_max_distribution(distributions):
  calories = np.array(list(map(calculate_calories, distributions)))
  return distributions[np.argmax(calories)]

while True:
  # Greedy optimization
  # At each step we add 1 ingredient and then remove 1 ingredient
  prev_distribution = distribution
  distribution = pick_max_distribution(np.eye(num_ingredients) + distribution)
  distribution = pick_max_distribution(-np.eye(num_ingredients) + distribution)
  if (calculate_calories(prev_distribution)>=calculate_calories(distribution)):
    break

print(calculate_calories(distribution))
