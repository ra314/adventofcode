from collections import Counter,defaultdict
#from functools import lru_cache
import itertools  # itertools.permutations
from queue import PriorityQueue
import re

#@lru_cache(maxsize=5000)
def cost(distance):
  pass

def rotations(x,y,z):
  def spin_right(x,y,z):
    return y,-x,z
  
  def turn_right(x,y,z):
    return z, y, -x
    
  def turn_up(x,y,z):
    return x,z,-y
  
  for _ in range(4):
    yield x,y,z
    x,y,z = spin_right(x,y,z)
    yield x,y,z
  
    x,y,z = spin_right(x,y,z)
    yield x,y,z
  
    x,y,z = spin_right(x,y,z)
    yield x,y,z
  
    x,y,z = spin_right(x,y,z)
    x,y,z = turn_right(x,y,z)
  
  x,y,z = turn_up(x,y,z)
  yield x,y,z
  
  x,y,z = spin_right(x,y,z)
  yield x,y,z

  x,y,z = spin_right(x,y,z)
  yield x,y,z

  x,y,z = spin_right(x,y,z)
  yield x,y,z

  x,y,z = spin_right(x,y,z)
  
  x,y,z = turn_up(x,y,z)
  x,y,z = turn_up(x,y,z)
  yield x,y,z
  
  x,y,z = spin_right(x,y,z)
  yield x,y,z

  x,y,z = spin_right(x,y,z)
  yield x,y,z

  x,y,z = spin_right(x,y,z)
  yield x,y,z
  

def main():
  sections = [sec.strip() for sec in open('input.txt').read().split('\n\n')]
  
  pts_sets = []

  for section in sections:
    hdr, body = section.split(' ---\n')
    scanner_num = hdr.split(' ')[2]
    lines = [l.split(',') for l in body.split('\n')]
    pt_set = set()
    for x,y,z in lines:
      pt_set.add( (int(x),int(y),int(z)) )
    pts_sets.append(pt_set)
    
  beacon_absolute_locations = set()
  for pt in pts_sets[0]:
    beacon_absolute_locations.add(pt)
  print(f'Starting with {len(beacon_absolute_locations)} beacons')
  
  unaligned_readings = pts_sets[1:]
  
  sensor_offsets = [(0,0,0)]
  
  while unaligned_readings:
    for aligning_with_beacon in list(beacon_absolute_locations):
      for unaligned_reading in list(unaligned_readings):
        rotation_possibilities = list(zip(*[list(rotations(x,y,z)) for x,y,z in unaligned_reading]))
        rotation_possibilities = [set(x) for x in rotation_possibilities]
        for i in range(24):
          possible_rotation = rotation_possibilities[i]
          for candidate_alignment_beacon in possible_rotation:
            dx = candidate_alignment_beacon[0] - aligning_with_beacon[0]
            dy = candidate_alignment_beacon[1] - aligning_with_beacon[1]
            dz = candidate_alignment_beacon[2] - aligning_with_beacon[2]
            possible_aligned_rotation = {(x-dx, y-dy, z-dz) for x,y,z in possible_rotation}
            overlap = len(possible_aligned_rotation.intersection(beacon_absolute_locations))
            if overlap >= 12:
               print('Found a match')
               sensor_offsets += [(dx, dy, dz)]
               beacon_absolute_locations.update(possible_aligned_rotation)
               unaligned_readings.remove(unaligned_reading)
               break
      
  print(len(beacon_absolute_locations))
  
  best_man_dist = 0
  for one, two in itertools.combinations(sensor_offsets, 2):
    man_dist = abs(one[0]-two[0]) + abs(one[1]-two[1]) + abs(one[2]-two[2])
    best_man_dist = max(best_man_dist, man_dist)
  print(f'Part 2: {best_man_dist}')
