import numpy as np
myfile = open("input.txt")
content = myfile.read()

nums = np.array(list(map(int, content.split(','))))

costs = []
for i in range(max(nums)+1):
    costs.append(abs(nums-i).sum())

print(min(costs))
