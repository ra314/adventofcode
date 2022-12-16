import numpy as np
myfile = open("input.txt")
content = myfile.read()

import re
content = re.findall(r'\|.*\n', content)
content = [match.split() for match in content]

from itertools import chain
content = list(chain.from_iterable(content))

lens = np.array(list(map(len, content)))
total = sum(lens==7)+sum(lens==4)+sum(lens==3)+sum(lens==2)
print(total)
