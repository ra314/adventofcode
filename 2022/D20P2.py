import re
import numpy as np
from copy import copy
myfile = open("input.txt")
content = myfile.read().splitlines()

decryption_key = 811589153
og_nums = [int(x)*decryption_key for x in content]
curr_nums = list(range(len(og_nums)))

assert(og_nums.count(0)==1)

for _ in range(10):
  for i, num in enumerate(og_nums):
    loc = curr_nums.index(i)
    del curr_nums[loc]
    insertion_index = (loc+num)%len(curr_nums)
    if insertion_index == 0:
      curr_nums.append(i)
    else:
      curr_nums.insert(insertion_index, i)
    #print(curr_nums)
    #print([og_nums[x] for x in curr_nums])
    print(i)

zero_index = curr_nums.index(og_nums.index(0))
a = og_nums[curr_nums[(zero_index+1000)%len(curr_nums)]]
b = og_nums[curr_nums[(zero_index+2000)%len(curr_nums)]]
c = og_nums[curr_nums[(zero_index+3000)%len(curr_nums)]]
print(a, b, c, a+b+c)
