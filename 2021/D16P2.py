import numpy as np
myfile = open("input.txt")
content = myfile.read()
content = content[:-1]

binary = ""
for char in content:
    binary += format(int(char, 16), '#06b')[2:]

def evaluate(binary, i):
    i += 3
    packet_type_id = int(binary[i:i+3], 2)
    i += 3
    if packet_type_id == 4:
        literal = ""
        while True:
            curr_chunk = binary[i:i+5]
            i += 5
            literal += curr_chunk[1:]
            if curr_chunk[0] == '0':
                break
        return int(literal, 2), i
    else:
        subpackets = []
        if binary[i] == '0':
            i += 1
            total_length_of_subpackets = int(binary[i:i+15], 2)
            i += 15
            destination = i + total_length_of_subpackets
            while i < destination:
                result = evaluate(binary, i)
                subpackets.append(result[0])
                i = result[1]
        elif binary[i] == '1':
            i += 1
            num_immediate_subpackets = int(binary[i:i+11], 2)
            i += 11
            for j in range(num_immediate_subpackets):
                result = evaluate(binary, i)
                subpackets.append(result[0])
                i = result[1]
    
    if packet_type_id == 0:
        return sum(subpackets), i
    elif packet_type_id == 1:
        from math import prod
        return prod(subpackets), i
    elif packet_type_id == 2:
        return min(subpackets), i
    elif packet_type_id == 3:
        return max(subpackets), i
    elif packet_type_id == 5:
        return subpackets[0]>subpackets[1], i
    elif packet_type_id == 6:
        return subpackets[0]<subpackets[1], i
    elif packet_type_id == 7:
        return subpackets[0]==subpackets[1], i

evaluate(binary, 0)[0]
