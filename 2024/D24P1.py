import dataclasses

import reader
content = reader.read()

c_values, c_gates = content.split("\n\n")

class Gate:
  all_gates = {}
  values = {}
  
  def __init__(self, write_address, op, read_1, read_2):
    self.write_address = write_address
    self.op = op
    self.read_1 = read_1
    self.read_2 = read_2
    Gate.all_gates[write_address] = self
  
  @staticmethod
  def static_evaluate(address: str) -> int:
    if address in Gate.values:
      return Gate.values[address]
    if address in Gate.all_gates:
      return Gate.all_gates[address].evaluate()
    assert(False)
    return 0
  
  def evaluate(self) -> int:
    r1 = Gate.static_evaluate(self.read_1)
    r2 = Gate.static_evaluate(self.read_2)
    if self.op == "AND":
      return r1 & r2
    elif self.op == "OR":
      return r1 | r2
    elif self.op == "XOR":
      return r1 ^ r2
    assert(False)
    return 0
  
  def __str__(self):
    return f"{self.read_1} {self.op} {self.read_2} -> {self.write_address}"

gates = []
for line in c_gates.splitlines():
  gate, write_address = line.split(" -> ")
  read_1, op, read_2 = gate.split()
  gates.append(Gate(write_address, op, read_1, read_2))

for line in c_values.splitlines():
  address, value = line.split(": ")
  Gate.values[address] = int(value)

z_gates = []
for gate in gates:
  if gate.write_address.startswith("z"):
    z_gates.append(gate)
z_gates = sorted(z_gates, key=lambda gate: gate.write_address, reverse=True)
result = "".join([str(gate.evaluate()) for gate in z_gates])
# Convert result from binary to decimal
print(int(result, 2))
