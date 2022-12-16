myfile = open("input.txt")
content = myfile.read()

import numpy as np
base_pattern = [0, 1, 0, -1]
input_pattern = np.array([int(char) for char in content.strip()])
input_pattern = np.tile(input_pattern, 10000)
message_offset = int(content.strip()[:7])

def get_base_patterns_matrix_rows():
  for i in range(1,len(input_pattern)+1):
    repeated_base_pattern = np.repeat(base_pattern, i)[:len(input_pattern)]
    num_tilings = (len(input_pattern)//len(repeated_base_pattern))+1
    tiled_base_pattern = np.tile(repeated_base_pattern, num_tilings)
    base_patterns_matrix_row = tiled_base_pattern[1:][:len(input_pattern)]
    yield base_patterns_matrix_row

#base_patterns_matrix = np.array(base_patterns_matrix)
#print(base_patterns_matrix)

def fft(input_pattern):
  retval = []
  i = 0
  for row in get_base_patterns_matrix_rows():
    retval.append(int(str((input_pattern * row).sum())[-1]))
    i += 1
    if i%100 == 0:
      print(i)
  return retval

print(input_pattern)
for i in range(100):
  print(i)
  input_pattern = fft(input_pattern)
  #print(input_pattern)

print("".join([str(num) for num in input_pattern])[message_offset:8+message_offset])
