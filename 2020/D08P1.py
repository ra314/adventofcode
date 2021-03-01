myfile = open("input.txt")
content = myfile.read()
content = content.splitlines()

lines_executed = [0] * len(content)

i=0
accumulator=0
while True:
	code = content[i][:3]
	num = int(content[i].split()[1])
	if lines_executed[i]:
		break
	else:
		lines_executed[i] = 1
	
	if code == "nop":
		i+=1
	elif code == "acc":
		i+=1
		accumulator+=num
	elif code == "jmp":
		i+=num
		
print(accumulator)
