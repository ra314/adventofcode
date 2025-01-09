import reader
content = reader.read()
import os

class Computer:
  def __init__(self, program: str, reg_a: int, reg_b: int, reg_c: int):
    self.program = program
    self.instruction_pointer = 0
    self.reg_a = reg_a
    self.reg_b = reg_b
    self.reg_c = reg_c
    self.output = []
  
  @staticmethod
  def parse_config(config: str):
    lines = config.splitlines()
    A = int(lines[0].split()[-1])
    B = int(lines[1].split()[-1])
    C = int(lines[2].split()[-1])
    program = list(map(int, lines[4].split(": ")[1].split(",")))
    return Computer(program, A, B, C)
  
  def get_output(self) -> str:
    return ",".join([str(x) for x in self.output])

  def __str__(self):
    return f"Program: {self.program}\nRegister A: {self.reg_a}\nRegister B: {self.reg_b}\nRegister C: {self.reg_c}\nOutput: {self.output}\nInstruction pointer: {self.instruction_pointer}"
  
  def combo_op(self, lit_op: int) -> int:
    if lit_op >= 0 and lit_op <= 3:
      return lit_op
    if lit_op == 4:
      return self.reg_a
    elif lit_op == 5:
      return self.reg_b
    elif lit_op == 6:
      return self.reg_c
    raise ValueError("Invalid literal operation: ", lit_op)
  
  def dv(self, lit_op: int) -> int:
    numerator = self.reg_a
    denominator = 2**self.combo_op(lit_op)
    return numerator // denominator
  
  def execute(self) -> bool:
    if self.instruction_pointer >= len(self.program) or self.instruction_pointer < 0:
      return False
    instruction = self.program[self.instruction_pointer]
    lit_op = self.program[self.instruction_pointer + 1]
    match instruction:
      case 0: # adv
        self.reg_a = self.dv(lit_op)
      case 1: #bxl 
        # Calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
        self.reg_b = self.reg_b ^ lit_op
      case 2: #bst
        self.reg_b = self.combo_op(lit_op) % 8
      case 3: #jnz
        if self.reg_a != 0:
          self.instruction_pointer = lit_op
          # Prevent the instruction pointer from moving again.
          return True
      case 4: #bxc
        # Calculates the bitwise XOR of register B and register C, then stores the result in register B.
        self.reg_b = self.reg_b ^ self.reg_c
      case 5: #out
        result = self.combo_op(lit_op) % 8
        self.output.append(result)
      case 6: #bdv
        self.reg_b = self.dv(lit_op)
      case 7: #cdv
        self.reg_c = self.dv(lit_op)
    self.instruction_pointer += 2
    return True

computer = Computer.parse_config(content)
# Execute the computer continuously until the output is complete.
while computer.execute():
  # Clear the previously console and print the computer
  print(computer)
  pass

print(computer.get_output())
