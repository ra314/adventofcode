import numpy as np
myfile = open("input2.txt")
content = myfile.read()
import itertools

def parse_scanner(lines):
    beacons = []
    for line in lines:
        beacons.append(list(map(int, line.split(','))))
    return np.array(beacons)

def parse_content(content):
    all_beacons = []
    for lines in content.split("---"):
        if lines and lines[0] == '\n':
            all_beacons.append(parse_scanner(lines.split()))
    return all_beacons

def sequence(beacon):
    X, Y, Z = beacon
    return [(X, Y, Z),(X, -Y, -Z),(X, Z, -Y),(X, -Z, Y),(-X, Y, -Z),(-X,-Y,Z),(-X,Z,Y),(-X,-Z,-Y),(Y,X,-Z),(Y,-X,Z),(Y,Z,X),(Y,-Z,-X),(-Y,X,Z),(-Y,-X,-Z),(-Y,Z,-X),(-Y,-Z,X),(Z,X,Y),(Z,-X,-Y),(Z,Y,-X),(Z,-Y,X),(-Z,X,-Y),(-Z,-X,Y),(-Z,Y,X),(-Z,-Y,-X)]

def generate_rotations(beacons):
    rotations = []
    for beacon in beacons:
        rotations.append(list(sequence(beacon)))
    return list(zip(*rotations))

from math import sqrt
def distance(beacon1, beacon2):
    return sqrt(((beacon1-beacon2)**2).sum())

def generate_distances(beacons):
    return set([distance(*beacon_duo) for beacon_duo in itertools.combinations(beacons, 2)])

def get_beacon_pair_indices(target_distance, beacons):
    for i in range(len(beacons)):
        for j in range(len(beacons)):
            if distance([beacons[i], beacons[j]]) == target_distance:
                return [i,j]
    return None

def rotate_and_align(known_beacons, unaligned_beacons):
    known_beacons = np.array(list(known_beacons))
    known_distances = generate_distances(known_beacons)
    unaligned_distances = generate_distances(unaligned_beacons)
    if len(known_distances & unaligned_distances) < 12:
        return None
    
    for beacons in generate_rotations(unaligned_beacons):
        for known_beacon in known_beacons:
            for unaligned_beacon in beacons:
                beacons = beacons - (unaligned_beacon-known_beacon)
                if len(set(map(tuple, beacons)).intersection(set(map(tuple, known_beacons)))) >= 12:
                    return beacons
    return None

all_beacons = parse_content(content)
total_num_shared = 0
known_beacons = set()

# Add the beacons from scanner 0 to populate initial data
known_beacons.update(list(map(tuple,all_beacons[0])))
all_beacons.pop(0)

while all_beacons:
    for i in range(len(all_beacons)):
        retval = rotate_and_align(known_beacons, all_beacons[i])
        if type(retval) != type(None):
            known_beacons.update(list(map(tuple,all_beacons[i])))
            all_beacons.pop(i)
            print(i)
            break

rotate_and_align(known_beacons, all_beacons[0])
