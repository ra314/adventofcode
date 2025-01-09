import reader
content = reader.read()

import numpy as np
content = np.array(list(map(list, content.splitlines())))

def get_diags(arr):
  n_diags = len(arr[0])
  retval = []
  for offset in range(-n_diags, n_diags, 1):
    retval.append(np.diag(arr, offset))
  return retval

def find_target(words, target):
  forwards = sum([word.count(target) for word in words])
  reverse_target = target[::-1]
  reverse = sum([word.count(reverse_target) for word in words])
  return forwards + reverse

rows = ["".join(row) for row in content]
cols = ["".join(col) for col in np.rot90(content)]
diags = ["".join(diags) for diags in get_diags(content)]
other_diags = ["".join(diags) for diags in get_diags(np.flip(content, axis=1))]
print(find_target(rows, "XMAS"))
print(find_target(cols, "XMAS"))
print(find_target(diags, "XMAS"))
print(find_target(other_diags, "XMAS"))
print(find_target(rows+cols+diags+other_diags, "XMAS"))
