import numpy as np
myfile = open("input.txt")
content = "3113322113"

import re
def split_num(string):
  return [m.group(0) for m in re.finditer(r"(\d)\1*", string)]

def read_out_num(string):
  outputs = list(map(lambda x: str(len(x)) + x[0], split_num(string)))
  return "".join(outputs)

for i in range(50):
  content = read_out_num(content)
  print(i)
  print(len(content))
