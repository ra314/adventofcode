myfile = open("input2.txt")
content = myfile.read()

total_characters_in_code = 0
total_characters_in_memory = 0
for line in content.splitlines():
  # Iterate characters excluding the first and last
  i = 1
  num_characters_in_code = len(line)
  num_characters_in_memory = 0
  while i < len(line)-1:
    if line[i] == '\\':
      if line[i+1] == '\\' or line[i+1] == '\"':
        num_characters_in_memory += 1
        i += 2
        continue
      # \x27 ASCII code
      else:
        num_characters_in_memory += 1
        i += 4
        continue
    num_characters_in_memory += 1
    i += 1
  total_characters_in_code += num_characters_in_code
  total_characters_in_memory += num_characters_in_memory
print(total_characters_in_code - total_characters_in_memory)
