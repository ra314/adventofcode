#Started 16/02/2021 13:25
#Ended 16/02/2021 13:28

myfile = open("input.txt")
content = myfile.read()

resulting_frequency = sum([int(line) for line in content.splitlines()])
print(resulting_frequency)
