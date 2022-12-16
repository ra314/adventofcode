import numpy as np
myfile = open("input.txt")
content = myfile.read()

depths = np.array(list(map(int, content.splitlines())))
aggregated_depths = np.convolve(depths,np.ones(3,dtype=int),'valid')
print(np.sum(np.diff(aggregated_depths)>0))
