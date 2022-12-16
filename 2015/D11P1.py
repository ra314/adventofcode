myfile = open("input2.txt")
content = "hxbxwxba"

def increment(string):
  nums = [ord(char)-ord('a') for char in string]
  nums[-1] += 1
  for i in reversed(range(len(nums))):
    if nums[i] == 26:
      nums[i] = 0
      if i-1 >= 0:
        nums[i-1] += 1
  retval = "".join([chr(ord('a')+num) for num in nums])
  return retval

import re
rx1 = re.compile(r'(.)\1.*(.)\2')

three_consecutive = ["abc"]
while three_consecutive[-1] != "xyz":
  consec = three_consecutive[-1]
  consec = "".join([chr(ord(char)+1) for char in consec])
  three_consecutive.append(consec)
def three_consecutive_in_string(string):
  for consec in three_consecutive:
    if consec in string:
      return True
  return False

while True:
  content = increment(content)
  print(content)
  if "i" in content or "o" in content or "l" in content:
    continue
  if not rx1.search(content):
    continue
  if not three_consecutive_in_string(content):
    continue
  print(content)
  break
  
