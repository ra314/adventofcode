myfile = open("input.txt")
content = myfile.read()
content = content.split()[0].split(",")
content = [int(x) for x in content]

#The key is the number
#The value is the turn it was said
nums = {}

i = 0
while i < 30000000:
	i += 1
	if i <= len(content):
		nums[content[i-1]] = [i]
		curr_num = content[i-1]
	else:
		new_num = (len(nums[curr_num]) == 1)
		if new_num:
			curr_num = 0
			nums[curr_num].append(i)
		else:
			curr_num = nums[curr_num][-1] - nums[curr_num][-2]
			if curr_num in nums:
				nums[curr_num].append(i)
			else:
				nums[curr_num] = [i]

	#print(curr_num)
	print(i)
