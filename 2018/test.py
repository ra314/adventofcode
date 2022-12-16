from multiprocessing import Pool
a = list(range(10))
def f(x):
	a[x] = 1
    
input = list(range(10))

import time

start = time.time()
p = Pool(2)
output1 = p.map(f, input)
print(time.time()-start)

start = time.time()
output2 = []
for num in input:
	output2.append(f(num))
print(time.time()-start)
