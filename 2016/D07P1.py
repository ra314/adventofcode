content = open("input.txt").read()

import re

def has_abba(string):
  for match in re.findall(r'((\w)(\w)\3\2)', string):
    if len(set(match[0])) == 2:
      return True
  return False

def supports_TLS(string):
  hypernet_sequences = re.findall(r'\[(\w+)\]', string)
  non_hypernet_sequences = re.sub(r'\[\w+\]', ' ', string).split()
  hypernet_sequence_has_abba = bool(sum([has_abba(x) for x in hypernet_sequences]))
  non_hypernet_sequence_has_abba = bool(sum([has_abba(x) for x in non_hypernet_sequences]))
  return non_hypernet_sequence_has_abba and not hypernet_sequence_has_abba

total = 0  
for line in content.splitlines():
  total += supports_TLS(line)

print(total)
  
