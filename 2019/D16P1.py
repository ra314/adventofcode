myfile = open("input2.txt")
content = myfile.read()

import numpy as np
base_pattern = [0, 1, 0, -1]
input_pattern = np.array([int(char) for char in content.strip()])

base_patterns_matrix = []
for i in range(1,len(input_pattern)+1):
  repeated_base_pattern = np.repeat(base_pattern, i)
  num_tilings = (len(input_pattern)//len(repeated_base_pattern))+1
  tiled_base_pattern = np.tile(repeated_base_pattern, num_tilings)
  base_patterns_matrix.append(tiled_base_pattern[1:][:len(input_pattern)])

base_patterns_matrix = np.array(base_patterns_matrix)
print(base_patterns_matrix)

def fft(input_pattern):
  double_digit_values = (input_pattern*base_patterns_matrix).sum(axis=1)
  return np.array([int(str(value)[-1]) for value in double_digit_values])

print(input_pattern)
for i in range(100):
  input_pattern = fft(input_pattern)
  print(input_pattern)

print("".join([str(num) for num in input_pattern])[:8])
