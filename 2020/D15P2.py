myfile = open("input.txt")
content = myfile.read()
content = content.split()[0].split(",")
content = [int(x) for x in content]

#The key is the number
#The value is the turn it was said
nums = {}

for i in range(len(content)):
	nums[content[i]] = i+1
	

curr_num = 0
i += 2

while i < 30000000:
	if nums.get(curr_num):
		next_num = i-nums[curr_num]
		nums[curr_num] = i
		curr_num = next_num
	else:
		nums[curr_num] = i
		curr_num = 0
	i += 1
	if (i%1000000) == 0: print(i, curr_num)
