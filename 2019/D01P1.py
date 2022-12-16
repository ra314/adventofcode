myfile = open("input.txt")
content = myfile.read()

###Parsing
masses = [int(line) for line in content.splitlines()]

###Calculating fuel requirement
print(sum([int(mass/3)-2 for mass in masses]))
