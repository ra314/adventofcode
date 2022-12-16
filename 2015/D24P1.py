from math import inf
from random import randint
import numpy as np

myfile = open("input2.txt")
content = myfile.read()

nums = [int(line) for line in content.splitlines()]

min_group_size = 4
min_distribution = None
min_QE = inf

def is_balanced(x):
  return sum(x[0]) == sum(x[1]) == sum(x[2])

def QE(x):
  return np.array(x[np.argmin(get_sublist_lens(x))]).prod()

def get_sublist_lens(x):
  return list(map(len, x))

while True:
  new_nums = nums.copy()
  curr_distribution = [[],[],[]]
  # Populate the first group with min_group_size elements
  for i in range(min_group_size):
    curr_distribution[0].append(new_nums.pop(randint(0,len(new_nums)-1)))
  while new_nums:
    curr_distribution[randint(1,2)].append(new_nums.pop(randint(0,len(new_nums)-1)))
  
  curr_min_group_size = min(get_sublist_lens(curr_distribution))
  curr_min_QE = QE(curr_distribution)
  
  if is_balanced(curr_distribution):
    if not min_distribution or (curr_min_group_size <= min_group_size and curr_min_QE < min_QE):
      min_distribution = curr_distribution
      min_QE = curr_min_QE
      min_group_size = curr_min_group_size
      print(f"New min found. QE:{min_QE} smallest_group:{min_group_size} distribution:{min_distribution}")
