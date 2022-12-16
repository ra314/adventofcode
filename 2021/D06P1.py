import numpy as np
myfile = open("input.txt")
content = myfile.read()

nums = list(map(int, content.split(',')))

def simulate_day(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 6
            nums.append(8)
        else:
            nums[i] -= 1
    return nums

for i in range(80):
    print(i)
    nums = simulate_day(nums)

print(len(nums))
