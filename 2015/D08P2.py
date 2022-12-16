myfile = open("input2.txt")
content = myfile.read()

total_characters_in_code = 0
total_characters_in_new_encoding = 0
for line in content.splitlines():
  num_characters_in_code = len(line)
  num_characters_in_new_encoding = 0
  # Add 1 for each existing character
  num_characters_in_new_encoding += num_characters_in_code
  # Add 1 extra for each \
  num_characters_in_new_encoding += line.count("\\")
  # Add 1 extra for each "
  num_characters_in_new_encoding += line.count("\"")
  # Add 2 for the quote at start and end
  num_characters_in_new_encoding += 2
  
  total_characters_in_code += num_characters_in_code
  total_characters_in_new_encoding += num_characters_in_new_encoding
print(total_characters_in_new_encoding - total_characters_in_code)
