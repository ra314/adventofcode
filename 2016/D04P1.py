content = open("input.txt").read()

import re
from collections import Counter

def is_real_room(checksum, letters):
  counts = Counter(letters).items()
  most_common = sorted(counts, key=lambda x: (x[1],-ord(x[0])), reverse=True)
  calculated_checksum = [x[0] for x in most_common[:5]]
  return "".join(calculated_checksum) == checksum

total = 0
for line in content.splitlines():
  checksum = re.search(r'\[(\w+)\]', line)[1]
  numbers = re.search(r'\d+',line)[0]
  letters = re.search(r'(\w+\-)+',line)[0].replace('-','')
  
  if is_real_room(checksum, letters):
    total += int(numbers)

print(total)
  
