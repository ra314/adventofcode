### OP codes
def addr(A, B, C, registers):
  registers[C] = registers[A] + registers[B]
def addi(A, B, C, registers):
  registers[C] = registers[A] + B

def mulr(A, B, C, registers):
  registers[C] = registers[A] * registers[B]
def muli(A, B, C, registers):
  registers[C] = registers[A] * B
  
def banr(A, B, C, registers):
  registers[C] = registers[A] & registers[B]
def bani(A, B, C, registers):
  registers[C] = registers[A] & B

def borr(A, B, C, registers):
  registers[C] = registers[A] | registers[B]
def bori(A, B, C, registers):
  registers[C] = registers[A] | B

def setr(A, B, C, registers):
  registers[C] = registers[A]
def seti(A, B, C, registers):
  registers[C] = A

def gtir(A, B, C, registers):
  registers[C] = A > registers[B]
def gtri(A, B, C, registers):
  registers[C] = registers[A] > B
def gtrr(A, B, C, registers):
  registers[C] = registers[A] > registers[B]

def eqir(A, B, C, registers):
  registers[C] = A == registers[B]
def eqri(A, B, C, registers):
  registers[C] = registers[A] == B
def eqrr(A, B, C, registers):
  registers[C] = registers[A] == registers[B]

###Parsing
class Sample:
  def __init__(self, before, instruction, after):
    self.before = before
    self.instruction = instruction
    self.after = after
  
  opcodes = (addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr)
  
  opcode_possibilities = [list() for i in range(len(opcodes))]
  
  opcode_index = [None for i in range(len(opcodes))] 
  
  def operate(self, opcode):
    registers = self.before.copy()
    opcode(*self.instruction[1:], registers)
    return registers
  
  def store_possible_opcodes(self):
    possibilities = set()
    for opcode in Sample.opcodes:
      if self.operate(opcode) == self.after:
        possibilities.add(opcode)
    Sample.opcode_possibilities[self.instruction[0]].append(possibilities)
  
  def get_num_possible_opcodes(self):
    return sum(map(lambda x: self.operate(x) == self.after, Sample.opcodes))
  
  def print_possibilities():
    for possiblity in Sample.opcode_possibilities:
      print(" ".join([x.__name__ for x in possiblity]))
  
  def solve_opcode_indices():
    OP = Sample.opcode_possibilities
    for i in range(len(OP)):
      OP[i] = set.intersection(*OP[i])
    
    pruned_indexes = set()
    all_pruned = False
    broken = False
    while not all_pruned:
      for i in range(len(OP)):
        if len(OP[i]) == 1 and (i not in pruned_indexes):
          pruned_indexes.add(i)
          OP_to_remove = list(OP[i])[0]
          for j in range(len(OP)):
            if i != j:
              OP[j].discard(OP_to_remove)
          broken = True
          break
      if broken:
        broken = False
        continue
      all_pruned = True 
    
    for i in range(len(OP)):
      Sample.opcode_index[i] = list(OP[i])[0]

def get_registers(line):
  return list(map(int, line.split(":")[1].strip()[1:-1].split(',')))

def get_space_separated_nums(line):
  return list(map(int, line.split()))

myfile = open("input.txt")
content = myfile.read().splitlines()
i = 0
samples = []
while i<len(content):
  line = content[i]
  if line and line[0] == "B":
    before = get_registers(content[i+0])
    instruction = get_space_separated_nums(content[i+1])
    after = get_registers(content[i+2])
    samples.append(Sample(before, instruction, after))
    i += 1
    continue
  i += 1

for sample in samples:
  sample.store_possible_opcodes()
Sample.solve_opcode_indices()
Sample.print_possibilities()


def operate(opcode, registers, instrcution):
  registers = registers.copy()
  opcode(*instruction[1:], registers)
  return registers

myfile = open("input3.txt")
content = myfile.read().splitlines()
registers = [0,0,0,0]
for line in content:
  instruction = get_space_separated_nums(line)
  opcode = Sample.opcode_index[instruction[0]]
  registers = operate(opcode, registers, instruction)
  print(registers)
