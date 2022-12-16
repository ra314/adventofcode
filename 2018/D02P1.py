#Started 16/02/2021 14:20
#Ended 16/02/2021 14:26

myfile = open("input.txt")
content = myfile.read()

num2 = 0
num3 = 0
import collections
for line in content.splitlines():
	counter = collections.Counter(list(line))
	if 2 in counter.values():
		num2 +=1 
	if 3 in counter.values():
		num3 += 1

print(num2*num3)
