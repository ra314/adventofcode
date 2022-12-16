myfile = open("input2.txt")
content = myfile.read()
import numpy as np
from collections import defaultdict

class Particle:
  particles = []
  def __init__(self, position, velocity, acceleration):
    self.position = np.array(position)
    self.velocity = np.array(velocity)
    self.acceleration = np.array(acceleration)
    self.live = True
    Particle.particles.append(self)
  
  def get_key(self):
    return str(self.position)
  
  def update(self):
    self.velocity += self.acceleration
    self.position += self.velocity
  
  def updateall():
    positions = defaultdict(list)
    for particle in Particle.particles:
      particle.update()
      positions[particle.get_key()].append(particle)
    for value in positions.values():
      if len(value) > 1:
        for particle in value:
          particle.live = False
    Particle.particles = list(filter(lambda x: x.live, Particle.particles))
  
  def distance_to_center(self):
    return np.sum(np.abs(self.position))
  
  def __str__(self):
    return " ".join(map(str, [self.position, self.velocity, self.acceleration]))

import re
for line in content.splitlines():
  position = list(map(int, re.search('p=<(.*?)>', line)[1].split(',')))
  velocity = list(map(int, re.search('v=<(.*?)>', line)[1].split(',')))
  acceleration = list(map(int, re.search('a=<(.*?)>', line)[1].split(',')))
  Particle(position, velocity, acceleration)

for i in range(1000):
  Particle.updateall()

print(len(Particle.particles))
