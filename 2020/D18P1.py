myfile = open("input.txt")
content = myfile.read()
content = content.replace(' ','')
content = content.splitlines()

def operate(num1, operator, num2):
	if operator == '+': return num1 + num2
	elif operator == '*': return num1 * num2

def solve(equation, i):
	num1_found = False
	operator = ''
	while True:
		char = equation[i]
		if equation[i] == '(':
			if not num1_found:
				num1, i = solve(equation, i+1)
				num1_found = True
			else:
				num2, i = solve(equation, i+1)
				num1 = operate(num1, operator, num2)
		elif equation[i].isdigit():
			if not num1_found:
				num1 = int(equation[i])
				num1_found = True
			else:
				num2 = int(equation[i])
				num1 = operate(num1, operator, num2)
		elif equation[i] in "*+":
			operator = equation[i]
		elif equation[i] == ")":
			return num1, i
		i+=1
		if i>=len(equation): return num1, i

answers = []
for equation in content:
	answers.append(solve(equation, 0)[0])

print(sum(answers))
