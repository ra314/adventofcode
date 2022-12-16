import numpy as np
myfile = open("input.txt")
content = myfile.read()

nums = np.array(list(map(int, content.split(','))))

costs = []
for i in range(max(nums)+1):
    costs.append(np.array(list(map(triangular, abs(nums-i)))).sum())

def triangular(n):
    return n*(n+1)/2

print(min(costs))
