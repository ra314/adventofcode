import numpy as np

myfile = open("input.txt")
content = myfile.read()
content = content.split('\n\n')
required_fields = ['ecl','pid','eyr','hcl','byr','iyr','hgt']
num_valid = 0

def fields_present(fields):
	for field in required_fields:
		if field not in fields:
			return False
	return True			

for passport in content:
	fields = []
	for field in passport.split():
		fields.append(field[:3])

	if fields_present(fields):
		num_valid += 1
		
print(num_valid)
			
