myfile = open("input2.txt")
content = myfile.read()

from collections import defaultdict
registers = defaultdict(int)
max_val = 0

for line in content.splitlines():
  line = line.split()
  line[0] = f"registers[\'{line[0]}\']"
  if line[1] == "inc":
    line[1] = "+="
  if line[1] == "dec":
    line[1] = "-="
  line[4] = f"registers[\'{line[4]}\']"
  output = " ".join(line[3:])
  output += ":"
  output += " ".join(line[0:3])
  exec(output)
  max_val = max(max(registers.values()), max_val)

print(max_val)
