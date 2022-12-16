import numpy as np

target_x = [20,30]
target_y = [-10,-5]

target_x = [153,199]
target_y = [-114,-75]

def will_land_in_zone(target_x, target_y, v_x, v_y):
    y = 0
    x = 0
    while True:
        y += v_y
        # Gravity
        v_y -= 1
        
        x += v_x
        # Drag
        if v_x != 0:
            v_x -= (1 if v_x > 0 else -1)
        
        if (target_y[0] <= y <= target_y[1]) and (target_x[0] <= x <= target_x[1]):
            return True
        if y < target_y[0]:
            return False

count = 0
valids = []
for i in range(-200, 200):
    for j in range(-200, 200):
        if will_land_in_zone(target_x, target_y, i, j):
            valids.append(f"{i},{j}")
            count += 1

print(count)
