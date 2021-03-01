myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()




line_to_change = 0
while line_to_change < len(content):
	i=0
	accumulator=0
	lines_executed = [0] * len(content)
	
	while True:
		code = content[i][:3]
		num = int(content[i].split()[1])
		
		if lines_executed[i]:
			break
		else:
			lines_executed[i] = 1
		
		if line_to_change == i and code in "jmpnop": 
			if code == "jmp": code = "nop"
			elif code == "nop": code = "jmp"
				
		if code == "nop":
			i+=1
		elif code == "acc":
			i+=1
			accumulator+=num
		elif code == "jmp":
			i+=num
			
		if i==len(content): break
			
	line_to_change += 1
	if i==len(content): break
		
print(accumulator)
