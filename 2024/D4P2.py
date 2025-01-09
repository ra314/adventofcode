import reader
content = reader.read()

import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

content = np.array(list(map(list, content.splitlines())))
words = sliding_window_view(content, (3,3))
count = 0
valid = ("MAS", "SAM")
for dim1 in words:
  for word in dim1:
    d1 = np.diag(word)
    d2 = np.diag(np.flip(word, axis=1))
    d1, d2 = "".join(d1), "".join(d2)
    print(d1, d2)
    is_valid = (d1 in valid) and (d2 in valid)
    print(is_valid)
    print()
    count += is_valid
print(count)
