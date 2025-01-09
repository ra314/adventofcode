import reader
content = reader.read()

import re

mults = re.findall(r'mul\((\d+),(\d+)\)', content)
print(sum([int(x)*int(y) for x,y in mults]))

# Cleaned up solution.
# Not required, well done.
