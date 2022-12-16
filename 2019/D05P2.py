myfile = open("input2.txt")
content = myfile.read()
content = list(map(int, content.split(",")))
OPCODE_TO_NUM_PARAMS = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}

def parse_opcode_and_parameter_modes(string):
  opcode = int(string[-2:])
  parameter_modes = string[:-2]
  parameter_modes = ('0'*(OPCODE_TO_NUM_PARAMS[opcode]-len(parameter_modes))) + parameter_modes
  parameter_modes = list(map(int, list(parameter_modes)))
  parameter_modes = parameter_modes[::-1]
  return opcode, parameter_modes

def read_parameter(instructions, parameter, parameter_mode):
  return parameter if parameter_mode else instructions[parameter]

inputs = [5]
outputs = []
pos = 0
opcode, parameter_modes = parse_opcode_and_parameter_modes(str(content[pos]))
while opcode != 99:
  if opcode==1 or opcode==2:
    assert(len(parameter_modes) == 3)
    assert(parameter_modes[2]==0)
    a = read_parameter(content, content[pos+1], parameter_modes[0])
    b = read_parameter(content, content[pos+2], parameter_modes[1])
    val = a+b if opcode==1 else a*b
    content[content[pos+3]] = val
    pos += len(parameter_modes)+1
  elif opcode==3:
    assert(len(parameter_modes) == 1)
    assert(parameter_modes[0]==0)
    content[content[pos+1]] = inputs.pop()
    pos += len(parameter_modes)+1
  elif opcode==4:
    assert(len(parameter_modes) == 1)
    outputs.append(read_parameter(content, content[pos+1], parameter_modes[0]))
    pos += len(parameter_modes)+1
  elif opcode==5 or opcode==6:
    assert(len(parameter_modes) == 2)
    a = read_parameter(content, content[pos+1], parameter_modes[0])
    b = read_parameter(content, content[pos+2], parameter_modes[1])
    jump_bool = a!=0 if opcode==5 else a==0
    if jump_bool:
      pos = b
    else:
      pos += len(parameter_modes)+1
  elif opcode==7 or opcode==8:
    assert(len(parameter_modes) == 3)
    assert(parameter_modes[2]==0)
    a = read_parameter(content, content[pos+1], parameter_modes[0])
    b = read_parameter(content, content[pos+2], parameter_modes[1])
    op_bool = a<b if opcode==7 else a==b
    content[content[pos+3]] = int(op_bool)
    pos += len(parameter_modes)+1
  elif opcode==99:
    break
  print(content)
  opcode, parameter_modes = parse_opcode_and_parameter_modes(str(content[pos]))

print(outputs)
