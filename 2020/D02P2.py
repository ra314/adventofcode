myfile = open("input.txt")
content = myfile.read()

num_valid_passwords = 0

for line in content.splitlines():
	index_1 = int(line.split()[0].split('-')[0])
	index_2 = int(line.split()[0].split('-')[1])
	char = line.split()[1][0]
	password = line.split()[-1]
	if (password[index_1-1] == char) ^ (password[index_2-1] == char):
		num_valid_passwords += 1

print(num_valid_passwords)
