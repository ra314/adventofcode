import numpy as np
myfile = open("input.txt")
content = myfile.read()

import re
content = re.findall(r'\|.*\n', content)
content = [match.split() for match in content]

from itertools import chain
content = list(chain.from_iterable(content))
digits_4 = list(filter(lambda x: x != "|", content))

# Deducing connections
myfile = open("input.txt")
content = myfile.read()

def f(line):
    line = line.split()
    digits_10 = line[:line.index('|')]
    digits_4 = line[line.index('|')+1:]
    dic = {}
    dic[1] = list(filter(lambda x: len(x) == 2, digits_10))[0]
    dic[4] = list(filter(lambda x: len(x) == 4, digits_10))[0]
    dic[7] = list(filter(lambda x: len(x) == 3, digits_10))[0]
    dic[8] = list(filter(lambda x: len(x) == 7, digits_10))[0]
    # These could be 3, 5, or 2
    can_be_235 = list(filter(lambda x: len(x) == 5, digits_10))
    dic[3] = list(filter(lambda x: len(set(x).intersection(set(dic[1])))==2, can_be_235))[0]
    # These could be 0, 6, or 9
    can_be_069 = list(filter(lambda x: len(x) == 6, digits_10))
    dic[9] = list(filter(lambda x: len(set(x).intersection(set(dic[4])))==4, can_be_069))[0]

    for num in [1,4,7,8,3,9]:
        digits_10.remove(dic[num])

    # These could be 0 or 6
    can_be_06 = list(filter(lambda x: len(x) == 6, digits_10))
    dic[0] = list(filter(lambda x: len(set(x).intersection(set(dic[1])))==2, can_be_06))[0]
    digits_10.remove(dic[0])

    dic[6] = list(filter(lambda x: len(x) == 6, digits_10))[0]
    digits_10.remove(dic[6])

    # These could be 3 or 5
    can_be_35 = list(filter(lambda x: len(x) == 5, digits_10))
    dic[5] = list(filter(lambda x: len(set(x).intersection(set(dic[6])))==5, can_be_35))[0]
    digits_10.remove(dic[5])

    dic[2] = list(filter(lambda x: len(x) == 5, digits_10))[0]
    digits_10.remove(dic[2])

    for i in range(len(digits_4)):
        digit = digits_4[i]
        for key in dic:
            if sorted(dic[key]) == sorted(digit):
                digits_4[i] = key

    return int("".join(map(str, digits_4)))

print(sum(list(map(f, content.splitlines()))))
