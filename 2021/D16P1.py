import numpy as np
myfile = open("input.txt")
content = myfile.read()
content = content[:-1]

binary = ""
for char in content:
    binary += format(int(char, 16), '#06b')[2:]

def get_packet_sum(binary, i):
    packet_version_sum = 0
    packet_version_sum += int(binary[i:i+3], 2)
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
        return packet_version_sum, i
    else:
        if binary[i] == '0':
            i += 1
            total_length_of_subpackets = int(binary[i:i+15], 2)
            i += 15
            destination = i + total_length_of_subpackets
            while i < destination:
                result = get_packet_sum(binary, i)
                packet_version_sum += result[0]
                i = result[1]
            return packet_version_sum, i
        elif binary[i] == '1':
            i += 1
            num_immediate_subpackets = int(binary[i:i+11], 2)
            i += 11
            for j in range(num_immediate_subpackets):
                result = get_packet_sum(binary, i)
                packet_version_sum += result[0]
                i = result[1]
            return packet_version_sum, i

get_packet_sum(binary, 0)[0]
