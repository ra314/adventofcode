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
		
print(content[i])
