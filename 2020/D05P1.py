myfile = open("input.txt")
content = myfile.read()

def code_to_binary(code):
	binary = ""
	for char in code:
		if char in "BR":
			binary += "1"
		else:
			binary += "0"
	return binary

seat_ids = []
for line in content.splitlines():
	bin_line = code_to_binary(line)
	row = int(bin_line[:7],2)
	column = int(bin_line[7:],2)
	seat_ids.append((row*8)+column)
	
print(max(seat_ids))
