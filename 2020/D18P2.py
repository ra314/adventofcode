myfile = open("input.txt")
content = myfile.read()
content = content.replace(' ','')
content = content.splitlines()

def clean_equation(equation):
	for i in range(len(equation)):
		if equation[i].isdigit():
			equation[i] = int(equation[i])
			
	return equation

def solve(start):
	global equation
	end = len(equation)
	
	#This it the first pass to get rid of brackets
	i=start
	while True:
		if equation[i] == '(':
			solve(i+1)
			del equation[i+2]
			del equation[i]
		elif equation[i] == ')':
			end = i
			break
		i+=1
		if i>=len(equation): break
		
	#This is the second pass to get rid of the sums
	i=start
	while True:
		if equation[i] == '+':
			equation[i] = equation[i-1]+equation[i+1]
			del equation[i+1]
			del equation[i-1]
			end-=2
			i-=1
		i+=1
		if i>=min(len(equation),end): break

	#This is the third pass to get rid of the products	
	i=start
	while True:
		if equation[i] == '*':
			equation[i] = equation[i-1]*equation[i+1]
			del equation[i + 1]
			del equation[i - 1]
			i-=1
			end-=2
		i+=1
		if i>=min(len(equation),end): break
		
	return

answers = []
for equation in content:
	equation = clean_equation(list(equation))
	solve(0)
	answers.append(equation[0])

print(answers)
print(sum(answers))