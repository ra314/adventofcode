myfile = open("input.txt")
content = myfile.read()

num_valid_passwords = 0

for line in content.splitlines():
	min = int(line.split()[0].split('-')[0])
	max = int(line.split()[0].split('-')[1])
	char = line.split()[1][0]
	password = line.split()[-1]
	if min <= password.count(char) <= max:
		num_valid_passwords += 1
	
	print(line)
	print(min, max, char)

print(num_valid_passwords)
