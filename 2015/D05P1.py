myfile = open("input.txt")
content = myfile.read()

vowels = "aeiou"

import re
rx = re.compile(r'(.)\1{1,}')
def is_good(string):
  for bad_pattern in ["ab", "cd", "pq", "xy"]:
    if bad_pattern in string:
      return False
  if not rx.search(string):
    return False
  return num_vowels(string) >= 3
  
def num_vowels(string):
  return sum([string.count(vowel) for vowel in vowels])  

count = 0
for string in content.splitlines():
  count += is_good(string)
print(count)
