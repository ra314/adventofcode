#Started 16/02/2021 13:25
#Ended 16/02/2021 13:28

myfile = open("input.txt")
content = myfile.read()

#91212129

content = content.splitlines()[0]
content = list(map(int, content))

total = 0
for i in range(len(content)-1):
    if content[i] == content[i+1]:
        total += content[i]

if content[0] == content[-1]:
    total += content[-1]

print(total)
