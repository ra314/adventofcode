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



myfile = open("input.txt")
content = myfile.read()

###Parsing
class Sample:
  def __init__(self, before, instruction, after):
    self.before = before
    self.instruction = instruction
    self.after = after
  
  opcodes = (addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr)
  
  def operate(self, opcode):
    registers = self.before.copy()
    opcode(*self.instruction[1:], registers)
    return registers
  
  def get_num_possible_opcodes(self):
    return sum(map(lambda x: self.operate(x) == self.after, Sample.opcodes))

def get_registers(line):
  return list(map(int, line.split(":")[1].strip()[1:-1].split(',')))

def get_space_separated_nums(line):
  return list(map(int, content[i+1].split()))

samples = []
content = content.splitlines()
i = 0
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

print(sum(map(lambda x: x.get_num_possible_opcodes() >= 3, samples)))
