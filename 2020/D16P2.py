myfile = open("input.txt")
content = myfile.read()

import re
#This is a dictionary that stores the valid_nums for each field
valid_nums_per_field = {}
for line in content.splitlines()[:content.splitlines().index("your ticket:")-1]:
	key = line[:line.find(':')]
	nums = list(map(int, re.findall("\d+", line)))
	values = list(range(nums[0], nums[1]+1)) + list(range(nums[2], nums[3]+1))
	valid_nums_per_field[key] = values

#This is a 2d list that contains all the nearby tickets
nearby_tickets = []
for ticket in content.splitlines()[content.splitlines().index("nearby tickets:")+1:]:
	nearby_tickets.append(list(map(int, re.findall("\d+", ticket))))
	
#These are all possible valid numbers for any ticket
ranges = re.findall("\d+-\d+", content)
valid_nums = []
for item in ranges:
	x, y = list(map(int, re.findall("\d+", item)))
	valid_nums.extend(list(range(x,y+1)))
	
#This is removing the invalid tickets
#By checking if they have a number that is not in the valid_nums list
def is_valid(ticket):
	for num in ticket:
		if num not in valid_nums:
			return False
	return True
valid_nearby_tickets = [ticket for ticket in nearby_tickets if is_valid(ticket)]

#Now we need to determine which field is which
import itertools
possible_fields = list(itertools.repeat(list(valid_nums_per_field.keys()),len(valid_nums_per_field)))

#This function checks if the num is allowed for a certain field
def is_valid_field(field):
	return curr_num in valid_nums_per_field[field]

#This goes through all the nums in each ticket
#And changes which fields are allowed for each position in the ticket
#By checking which fields are invalid for each number
for ticket in valid_nearby_tickets:
	for i in range(len(ticket)):
		curr_num = ticket[i]
		possible_fields[i] = list(filter(is_valid_field, possible_fields[i]))
		
#Find the size of a 2d array
def size(array):
	length = 0
	for item in array:
		length += len(item)
	return length

#Now go through possible fields
#If there is only one field left in a position,
#remove it from the possible fields for other positions
#Repeat doing this until there are no changes
prev_length = size(possible_fields)
while True:
	for i in range(len(possible_fields)):
		if len(possible_fields[i])==1:
			unique_field = possible_fields[i][0]
			for j in range(len(possible_fields)):
				if j!=i:
					if unique_field in possible_fields[j]:
						possible_fields[j].remove(unique_field)
	curr_length = size(possible_fields)
	if prev_length == curr_length: break
	prev_length = curr_length
	
possible_fields = [i[0] for i in possible_fields]

#Now we just get the answer
your_ticket = content.splitlines()[content.splitlines().index("your ticket:")+1]
your_ticket = list(map(int, re.findall("\d+", your_ticket)))

product = 1
for i in range(len(possible_fields)):
	if 'departure' in possible_fields[i]:
		product *= your_ticket[i]
		
print(product)
