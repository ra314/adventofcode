myfile = open("input.txt")
content = myfile.read()
content = content.split()
content = [int(string) for string in content]
preamble_length = 25

def can_sum(nums, target):
	for x in nums:
		for y in nums:
			if x+y == target:
				return True
	return False
	
i = preamble_length
while i < len(content):
	if not can_sum(content[i-preamble_length:i], content[i]):
		break
	i+=1
		
invalid_num = content[i]
found = False
for i in range(len(content)):
	for j in range(i,len(content)):
		if sum(content[i:j]) == invalid_num:
			found = True
			break
	if found: break
		
print(i,j)
print(min(content[i:j]) + max(content[i:j]))
