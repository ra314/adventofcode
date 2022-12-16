myfile = open("input.txt")
content = myfile.read()

###Parsing
program = [int(num) for num in content.split(',')]
program[1] = 12
program[2] = 2

###Calculating fuel requirement
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
        
    print(position)

print(program[0])
