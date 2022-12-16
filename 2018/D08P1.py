#Started 22/02/2021 16:34
#Ended 22/02/2021 16:57

myfile = open("input.txt")
content = myfile.read()
content = [int(num) for num in content.split()]

metadata_sum = 0

#The function returns the number of nums to skip to get to the metadata
def extract_metadata(data):
	global metadata_sum
	num_children = data[0]
	num_metadata = data[1]
	num_to_skip = 0
	
	children_processed = 0
	while children_processed != num_children:
		num_to_skip += extract_metadata(data[2+num_to_skip:])
		children_processed += 1
		
	#print(num_children, num_metadata, data[2+num_to_skip:2+num_to_skip+num_metadata])
	metadata_sum += sum(data[2+num_to_skip:2+num_to_skip+num_metadata])
	return num_metadata + 2 + num_to_skip
	
extract_metadata(content)
print(metadata_sum)
