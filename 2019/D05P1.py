myfile = open("input2.txt")
content = myfile.read()
content = list(map(int, content.split(",")))
OPCODE_TO_NUM_PARAMS = {1:3, 2:3, 3:1, 4:1, 99:0}

def parse_opcode_and_parameter_modes(string):
  opcode = int(string[-2:])
  parameter_modes = string[:-2]
  parameter_modes = ('0'*(OPCODE_TO_NUM_PARAMS[opcode]-len(parameter_modes))) + parameter_modes
  parameter_modes = list(map(int, list(parameter_modes)))
  parameter_modes = parameter_modes[::-1]
  return opcode, parameter_modes

def read_parameter(instructions, parameter, parameter_mode):
  if parameter_mode:
    return parameter
  else:
    return instructions[parameter]

inputs = [1]
outputs = []
pos = 0
opcode, parameter_modes = parse_opcode_and_parameter_modes(str(content[pos]))
while opcode != 99:
  if opcode==1 or opcode==2:
    assert(len(parameter_modes) == 3)
    a = read_parameter(content, content[pos+1], parameter_modes[0])
    b = read_parameter(content, content[pos+2], parameter_modes[1])
    val = a+b if opcode==1 else a*b
    assert(parameter_modes[2]==0)
    content[content[pos+3]] = val
  elif opcode==3:
    assert(parameter_modes[0]==0)
    content[content[pos+1]] = inputs.pop()
  elif opcode==4:
    outputs.append(read_parameter(content, content[pos+1], parameter_modes[0]))
  elif opcode==99:
    break
  print(content)
  pos += len(parameter_modes)+1
  opcode, parameter_modes = parse_opcode_and_parameter_modes(str(content[pos]))
