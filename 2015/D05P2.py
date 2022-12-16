myfile = open("input2.txt")
content = myfile.read()

vowels = "aeiou"

import re
rx1 = re.compile(r'(..).*\1')
rx2 = re.compile(r'(.).\1')
def is_good(string):
  return bool(rx1.search(string) and rx2.search(string))
  
def num_vowels(string):
  return sum([string.count(vowel) for vowel in vowels])  

count = 0
for string in content.splitlines():
  count += is_good(string)
print(count)
