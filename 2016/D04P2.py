content = open("input.txt").read()

import re
from collections import Counter

def is_real_room(checksum, letters):
  counts = Counter(letters).items()
  most_common = sorted(counts, key=lambda x: (x[1],-ord(x[0])), reverse=True)
  calculated_checksum = [x[0] for x in most_common[:5]]
  return "".join(calculated_checksum) == checksum

def decrypt_room(number, letters):
  ords = [(ord(x)-ord('a')+number)%26 for x in letters]
  return "".join([chr(x+ord('a')) for x in ords])

for line in content.splitlines():
  checksum = re.search(r'\[(\w+)\]', line)[1]
  numbers = re.search(r'\d+',line)[0]
  letters = re.search(r'(\w+\-)+',line)[0].replace('-','')
  
  if is_real_room(checksum, letters):
    if "pole" in decrypt_room(int(numbers), letters):
      print(int(numbers))

  
