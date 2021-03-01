myfile = open("input2.txt")
content = myfile.read()
content = content.split()
content = [int(num) for num in content]
content.sort()

#This is the jump from the outlet that has 0 joltage
content = [0] + content
#This is the jump that the device provides
content.append(content[-1]+3)

diffs = [0,0,0]
for i in range(1,len(content)):
	diffs[content[i]-content[i-1]-1] += 1
	print(content[i], diffs)

print(diffs)
print(diffs[0]*diffs[2])
