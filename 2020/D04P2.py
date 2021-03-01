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
	
def fields_valid(fields):
	for field in fields:
		field_code = field[:3]
		field_value = field[4:]
		
		if field_code == "byr":
			if not (1920 <= int(field_value) <= 2002):
				return False
		elif field_code == "iyr":
			if not (2010 <= int(field_value) <= 2020):
				return False
		elif field_code == "eyr":
			if not (2020 <= int(field_value) <= 2030):
				return False
		elif field_code == "hgt":
			if field_value[-2:] == "cm":
				if not (150 <= int(field_value[:-2]) <= 193):
					return False
			elif field_value[-2:] == "in":
				if not (59 <= int(field_value[:-2]) <= 76):
					return False
			else:
				return False
		elif field_code == "hcl":
			if field_value[0] != "#":
				return False
			if len(field_value) != 7:
				return False
			for char in field_value[1:]:
				if char not in "1234567890abcdef":
					return False
		elif field_code == "ecl":
			if field_value not in ["amb","blu","brn","gry","grn","hzl","oth"]:
				return False
		elif field_code == "pid":
			if len(field_value) != 9:
				return False
			if not field_value.isdigit():
				return False
				
	return True
			

for passport in content:
	fields = []
	for field in passport.split():
		fields.append(field[:3])

	if not fields_present(fields):
		continue
	
	if fields_valid(passport.split()):
		num_valid += 1
		
print(num_valid)
			
