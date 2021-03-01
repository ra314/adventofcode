import numpy as np
myfile = open("input.txt")
content = myfile.read()
nums = []
target = 2020

for line in content.splitlines():
	nums.append(int(line))
	
def find_triplet(nums, target):
	for x in nums:
		for y in nums:
			for z in nums:
				if x+y+z == target:
					return x,y,z

triplet = find_triplet(nums, target)
print(triplet)			
print(np.prod(triplet))
