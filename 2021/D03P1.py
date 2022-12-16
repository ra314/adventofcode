import numpy as np
myfile = open("input.txt")
content = myfile.read()

array = []
for line in content.splitlines():
    array.append((list(map(int, line))))

array = np.array(array)

gamma = []
epsilon = []

for column in array.transpose():
    gamma.append(np.argmax(np.bincount(column)))
    epsilon.append(1 - gamma[-1])

gamma = int("".join(map(str, gamma)), 2)
epsilon = int("".join(map(str, epsilon)), 2)

print(gamma*epsilon)
