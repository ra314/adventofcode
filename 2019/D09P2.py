myfile = open("input.txt")
content = myfile.read()

###Parsing
program = [int(num) for num in content.split(',')]

###Calculating fuel requirement
def run_program(program):
    position = 0
    while True:
        match program[position]:
            case 1:
                program[program[position+3]] = program[program[position+1]]+program[program[position+2]]
                position += 4
            case 2:
                program[program[position+3]] = program[program[position+1]]*program[program[position+2]]
                position += 4
            case 99:
                break
            
    return program[0]

###Brute force
def find_input():
    for i in range(100):
        for j in range(100):
            program2 = program.copy()
            program2[1] = i
            program2[2] = j
            if run_program(program2) == 19690720:
                return((100*i)+j)

print(find_input())
