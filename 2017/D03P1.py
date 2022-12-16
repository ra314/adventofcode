content = 361527

from math import sqrt, ceil

closest_root = ceil(sqrt(content))
if (closest_root%2 == 0):
  closest_root += 1

closest_square = closest_root**2
distance_between_midpoints = closest_root-1
midpoints = [closest_square-(distance_between_midpoints//2),closest_square-(distance_between_midpoints//2)-(distance_between_midpoints),
closest_square-(distance_between_midpoints//2)-(distance_between_midpoints*2),
closest_square-(distance_between_midpoints//2)-(distance_between_midpoints*3)]

import numpy as np
midpoints = np.array(midpoints)

print(min(abs(midpoints-content))+((closest_root-1)//2))
