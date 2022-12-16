#Started 16/02/2021 15:22
#Ended 16/02/2021 15:26

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
			
	return (nums[0], output)

#This is a list of coordinates that are claimed by each claim
claim_coordinates = [generate_coordinates(line) for line in content.splitlines()]

#These are all the coordinates that are claimed at least one
claimed_coordinates = set()	
#These are all the coordinates claimed more than once
multi_claimed_coordinates = set()

#Determining the above sets
for coordinates in claim_coordinates:
	multi_claimed_coordinates.update(coordinates[1].intersection(claimed_coordinates))
	claimed_coordinates.update(coordinates[1])
	
#Finding the claim with no intersection
for coordinates in claim_coordinates:
	if len(coordinates[1].intersection(multi_claimed_coordinates)) == 0:
		break
		
print(coordinates[0])

