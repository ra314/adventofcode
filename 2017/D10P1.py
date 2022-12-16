#Started 16/02/2021 13:25
#Ended 16/02/2021 13:28

myfile = open("input.txt")
content = myfile.read()

skip_size = 0
nums = np.arange(256)
lengths = list(map(int, content.split()[0].split(',')))
curr_index = 0

import numpy as np
for length in lengths:
  indices = np.arange(curr_index,curr_index+length)
  indices %= 256
  nums[indices] = nums[indices[::-1]]
  curr_index += (length+skip_size)
  skip_size += 1
  print(nums)

print(nums[0]*nums[1])
