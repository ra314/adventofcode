import numpy as np
myfile = open("input.txt")
content = myfile.read()
nums = np.zeros(2021)
target = 2020

for line in content.splitlines():
	num = int(line)
	if num <= 2020:
		nums[num] = 1
		
for line in content.splitlines():
	num = int(line)
	if nums[target-num]:
		break
		
print(num*(target-num))
