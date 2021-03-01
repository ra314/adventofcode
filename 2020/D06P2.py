myfile = open("input2.txt")
content = myfile.read()
content = content.split('\n\n')

counts = 0
for group in content:
	questions = [0]*26
	
	for person in group.split():
		for char in person:
			questions[ord(char)-97] += 1
	
	for question in questions:
		if question == len(group.split()):
			counts += 1
	
print(counts)
