#Started 16/02/2021 14:43
#Ended 16/02/2021 15:22

myfile = open("input.txt")
content = myfile.read()

import re
def generate_coordinates(claim):
	nums = [int(num) for num in list(re.findall("\d+", claim))]
	inches_from_left_edge = nums[1]
	inches_from_top_edge = nums[2]
	width = nums[3]
	height = nums[4]
	
	output = set()
	for i in range(inches_from_left_edge, inches_from_left_edge+width):
		for j in range(inches_from_top_edge, inches_from_top_edge+height):
			output.add(f"x:{i}, y:{j}")
			
	return output

#This is a list of coordinates that are claimed by each claim
claim_coordinates = [generate_coordinates(line) for line in content.splitlines()]

#These are all the coordinates that are claimed at least one
claimed_coordinates = set()	
#These are all the coordinates claimed more than once
multi_claimed_coordinates = set()

#Determining the above sets
for coordinates in claim_coordinates:
	multi_claimed_coordinates.update(coordinates.intersection(claimed_coordinates))
	claimed_coordinates.update(coordinates)
	
print(len(multi_claimed_coordinates))
