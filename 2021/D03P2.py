import numpy as np
myfile = open("input.txt")
content = myfile.read()

array = []
for line in content.splitlines():
    array.append((list(map(int, line))))

array = np.array(array)

curr = array
for i in range(len(array[0])):
    m_freq = np.argmax(np.bincount(curr[:,i]))
    # O2 generator
    if np.bincount(curr[:,i])[0] == np.bincount(curr[:,i])[1]:
        m_freq = 1
    curr = curr[curr[:,i] == m_freq]
    if len(curr) == 1:
        break

O2 = curr[0]


curr = array
for i in range(len(array[0])):
    m_freq = np.argmin(np.bincount(curr[:,i]))
    # CO2 generator
    if np.bincount(curr[:,i])[0] == np.bincount(curr[:,i])[1]:
        m_freq = 0
    curr = curr[curr[:,i] == m_freq]
    if len(curr) == 1:
        break

CO2 = curr[0]
    
O2 = int("".join(map(str, O2)), 2)
CO2 = int("".join(map(str, CO2)), 2)

print(O2*CO2)
