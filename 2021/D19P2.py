import numpy as np
myfile = open("input.txt")
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

from math import sqrt
def distance(beacon_pair):
    beacon1 = beacon_pair[0]
    beacon2 = beacon_pair[1]
    return sqrt(((beacon1-beacon2)**2).sum())

def generate_triangle(beacon_trio):
    return tuple(sorted(list(map(distance, itertools.combinations(beacon_trio, 2)))))

def generate_triangles(beacons):
    return set([generate_triangle(beacon_trio) for beacon_trio in itertools.combinations(beacons, 3)])

def generate_distances(beacons):
    return set([distance(beacon_duo) for beacon_duo in itertools.combinations(beacons, 2)])

# This is code to generate triangles for all beacons within a given scanner, no longer being used
#all_beacons = parse_content(content)
#all_triangles = list(map(generate_triangles, all_beacons))
#len(all_triangles[0].intersection(all_triangles[1]))

from math import comb
def reverse_n_choose_k(x, k):
    n = 0
    while comb(n, k) != x:
        n += 1
        if n > 20: return 0
    return n

def get_beacon_pair_indices(target_distance, beacons):
    for i in range(len(beacons)):
        for j in range(len(beacons)):
            if distance([beacons[i], beacons[j]]) == target_distance:
                return [i,j]
    return None

def sequence(beacon):
    X, Y, Z = beacon
    return [(X, Y, Z),(X, -Y, -Z),(X, Z, -Y),(X, -Z, Y),(-X, Y, -Z),(-X,-Y,Z),(-X,Z,Y),(-X,-Z,-Y),(Y,X,-Z),(Y,-X,Z),(Y,Z,X),(Y,-Z,-X),(-Y,X,Z),(-Y,-X,-Z),(-Y,Z,-X),(-Y,-Z,X),(Z,X,Y),(Z,-X,-Y),(Z,Y,-X),(Z,-Y,X),(-Z,X,-Y),(-Z,-X,Y),(-Z,Y,X),(-Z,-Y,-X)]

def generate_rotations(beacons):
    rotations = []
    for beacon in beacons:
        rotations.append(list(sequence(beacon)))
    return list(zip(*rotations))

def rotate_and_align(beacons1, beacons2, i1, i2):
    rotations = generate_rotations(beacons2)
    for i in range(len(rotations)):
        rotation = rotations[i]
        rotation = rotation - (rotation[i2]-beacons1[i1])
        if len(set(map(tuple, beacons1)).intersection(set(map(tuple, rotation)))) >= 12:
            return rotation
    return None

def mold_beacons(first_scanner_indices, second_scanner_indices, beacons1, beacons2):
# transform the beacons for the second scanner such that beacon 1 has the same coordinates in both scanners
    for i1 in first_scanner_indices:
        for i2 in second_scanner_indices:
            retval = rotate_and_align(beacons1, beacons2, i1, i2)
            if type(retval) == type(np.array([])):
                return retval

all_beacons = parse_content(content)
from copy import deepcopy
og_beacons = deepcopy(all_beacons)
all_distances = list(map(generate_distances, all_beacons))
num_beacons = sum(map(len, all_beacons))
total_num_shared = 0
solved_scanners = set()
for i, j in itertools.combinations(range(len(all_distances)), 2):
    if j in solved_scanners:
        i, j = j, i
    intersecting_distances = all_distances[i].intersection(all_distances[j])
    num_intersecting_distances = len(intersecting_distances)
    num_shared_beacons = reverse_n_choose_k(num_intersecting_distances, 2)
    if num_shared_beacons >= 12: total_num_shared += num_shared_beacons
    if num_shared_beacons >= 12:
        # Pick two beacons that are the same for both scanners
        first_scanner_indices = get_beacon_pair_indices(list(intersecting_distances)[0], og_beacons[i])
        second_scanner_indices = get_beacon_pair_indices(list(intersecting_distances)[0], og_beacons[j])
        retval = mold_beacons(first_scanner_indices, second_scanner_indices, all_beacons[i], all_beacons[j])
        all_beacons[j] = retval
        solved_scanners.add(i)
        solved_scanners.add(j)
        print(i,j)

print(total_num_shared)
print(len(set(map(tuple, np.concatenate(all_beacons)))))
print(np.sort(np.concatenate(all_beacons), axis = 0))
