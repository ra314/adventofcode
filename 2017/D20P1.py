myfile = open("input2.txt")
content = myfile.read()
import numpy as np

class Particle:
  def __init__(self, position, velocity, acceleration):
    self.position = np.array(position)
    self.velocity = np.array(velocity)
    self.acceleration = np.array(acceleration)
  
  def update(self):
    self.velocity += self.acceleration
    self.position += self.velocity
  
  def distance_to_center(self):
    return np.sum(np.abs(self.position))
  
  def __str__(self):
    return " ".join(map(str, [self.position, self.velocity, self.acceleration]))

import re
particles = []
for line in content.splitlines():
  position = list(map(int, re.search('p=<(.*?)>', line)[1].split(',')))
  velocity = list(map(int, re.search('v=<(.*?)>', line)[1].split(',')))
  acceleration = list(map(int, re.search('a=<(.*?)>', line)[1].split(',')))
  particles.append(Particle(position, velocity, acceleration))


for particle in particles:
  for i in range(100000):
    particle.update()

distances = list(map(lambda x: x.distance_to_center(), particles))
print(distances.index(min(distances)))
