myfile = open("input2.txt")
content = myfile.read()

class Reindeer:
  def __init__(self, topspeed, movement_duration, rest_duration):
    self.topspeed = topspeed
    self.movement_duration = movement_duration
    self.rest_duration = rest_duration
    self.resting = False
    self.distance = 0
    self.timer = movement_duration
    self.points = 0
  
  def fly(self):
    self.timer -= 1
    if not self.resting:
      self.distance += self.topspeed
    if self.timer == 0:
      self.resting = not self.resting
      if self.resting:
        self.timer = self.rest_duration
      else:
        self.timer = self.movement_duration

reindeers = []
for line in content.splitlines():
  line = line.split()
  reindeers.append(Reindeer(int(line[3]), int(line[6]), int(line[-2])))

for i in range(2503):
  for reindeer in reindeers:
    reindeer.fly()
  distances = list(map(lambda x: x.distance, reindeers))
  max_d = max(distances)
  for reindeer in reindeers:
      if reindeer.distance == max_d:
        reindeer.points += 1

points = list(map(lambda x: x.points, reindeers))
print(max(points))
