import numpy as np
myfile = open("input.txt")
content = myfile.read()

depths = np.array(list(map(int, content.splitlines())))
print(np.sum(np.diff(depths)>0))
