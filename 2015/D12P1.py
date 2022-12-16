myfile = open("input2.txt")
content = myfile.read()

import re

result = [int(d) for d in re.findall(r'-?\d+', content)]

print(result)
print(sum(result))
