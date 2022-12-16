#Started 16/02/2021 13:29
#Ended 16/02/2021 13:44

myfile = open("input.txt")
content = myfile.read()

reached_frequencies = set()
current_frequency = 0
repeat_not_found = True

i = 0
while repeat_not_found:
	for line in content.splitlines():
		current_frequency += int(line)
		if current_frequency in reached_frequencies:
			repeat_not_found = False
			break
		else:
			reached_frequencies.add(current_frequency)
			
	if not repeat_not_found: 
		break
	
	i += 1
	print(i)
		
print(current_frequency)

#Holy shit, a set is a shit ton faster than lists for appending and searching
