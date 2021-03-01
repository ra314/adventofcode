myfile = open("input.txt")
content = myfile.read()
content = content.split()
content = [int(num) for num in content]
content.sort()

#The first bit is the jump from the outlet that has 0 joltage
#The second bit is the joltage of the device which is always 3 more than max
content = [0] + content + [content[-1]+3]

#We start at the bottom and use DFS to find all paths to the top
#Dynamic programming is used to store the number of paths from any given adapter to the top
paths = [0] * len(content)
paths[len(content)-1] = 1
paths[len(content)-2] = 1
def find_paths_to_top(adapter_index):
	sum = 0
	
	if paths[adapter_index] != 0:
		return paths[adapter_index]
	
	i = adapter_index + 1	
	while True:
		if content[i] - content[adapter_index] <= 3:
			sum += find_paths_to_top(i)
			i += 1
		else:
			break
	
	paths[adapter_index] = sum
	return sum

print()
print(find_paths_to_top(0))
