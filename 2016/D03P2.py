content = open("input.txt").read()

import numpy as np

def is_valid_triangle(nums):
  A = nums[0] + nums[1] > nums[2]
  B = nums[1] + nums[2] > nums[0]
  C = nums[2] + nums[0] > nums[1]
  return A and B and C

nums = []
for i in range(3):
  for line in content.splitlines():
    nums.append(int(line.strip().split()[i]))

num_valid = 0
i = 0
while i < len(nums):
  num_valid += is_valid_triangle(nums[i:i+3])
  i += 3

print(num_valid)
