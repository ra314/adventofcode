myfile = open("input.txt")
content = myfile.read()
import re

low = int(content.split('-')[0])
high = int(content.split('-')[1])

def count_passwords(low, high):
  count = 0
  for password in range(low, high):
    password = str(password)
    if "".join(sorted(password)) != password:
      continue
    if 2 not in [len(m.group(0)) for m in re.finditer(r"(\d)\1*", password)]:
      continue
    count += 1
  return count

print(count_passwords(low, high))
