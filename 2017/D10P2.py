#Started 16/02/2021 13:25
#Ended 16/02/2021 13:28

myfile = open("input.txt")
content = myfile.read()

import numpy as np
nums = np.array(list(map(int, content.split())))
cache = set()
num_cycles = 0

while True:
  # This works because numpy finds the first index of the max which is what we want anyway
  redistribution_index = np.argmax(nums)
  redistribution_amount = nums[redistribution_index]
  nums[redistribution_index] = 0
  nums += int(redistribution_amount/len(nums))
  redistribution_amount -= (int(redistribution_amount/len(nums))*len(nums))
  i = redistribution_index
  i += 1
  while redistribution_amount:
    if i >= len(nums):
      i = 0
    nums[i] += 1
    redistribution_amount -= 1
    i += 1
  num_cycles += 1
  string = ",".join(list(map(str, nums)))
  if string in cache:
    print(num_cycles)
    break
  else:
    cache.add(string)

target = string
num_cycles = 0
while True:
  # This works because numpy finds the first index of the max which is what we want anyway
  redistribution_index = np.argmax(nums)
  redistribution_amount = nums[redistribution_index]
  nums[redistribution_index] = 0
  nums += int(redistribution_amount/len(nums))
  redistribution_amount -= (int(redistribution_amount/len(nums))*len(nums))
  i = redistribution_index
  i += 1
  while redistribution_amount:
    if i >= len(nums):
      i = 0
    nums[i] += 1
    redistribution_amount -= 1
    i += 1
  num_cycles += 1
  string = ",".join(list(map(str, nums)))
  if string == target:
    print(num_cycles)
    break
