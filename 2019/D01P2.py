myfile = open("input.txt")
content = myfile.read()

###Parsing
masses = [int(line) for line in content.splitlines()]

###Calculating fuel requirement
def calculate_fuel(mass):
	total_fuel = 0
	fuel = mass
	while fuel>0:
		fuel = max(int(fuel/3)-2, 0)
		total_fuel += fuel
	return total_fuel
	
print(sum([calculate_fuel(mass) for mass in masses]))
