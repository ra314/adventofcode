myfile = open("input.txt")
content = myfile.read()

import re
ranges = re.findall("\d+-\d+", content)
other_tickets = content[content.index("nearby tickets"):]
nums = list(map(int, re.findall("\d+", other_tickets)))

valid_nums = []
for item in ranges:
	x, y = list(map(int, re.findall("\d+", item)))
	valid_nums.extend(list(range(x,y+1)))
	
invalid = []
for num in nums:
	if num not in valid_nums:
		invalid.append(num)
		
print(sum(invalid))
print(invalid)
