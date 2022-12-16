import numpy as np

target_x = [20,30]
target_y = [-10,-5]

target_x = [153,199]
target_y = [-114,-75]

y = 0

def will_land_in_zone(target_y, v_y):
    y = 0
    while True:
        y += v_y
        # Gravity
        v_y -= 1
        if target_y[0] <= y <= target_y[1]:
            return True
        if y < target_y[0]:
            return False

def get_max_y(v_y):
    y = 0
    while v_y>0:
        y += v_y
        # Gravity
        v_y -= 1
    return y

def get_max_v_y(target_y):
    bools = [will_land_in_zone(target_y, i) for i in range(200)]
    index = len(bools) - bools[::-1].index(True) - 1
    return index

print(get_max_y(get_max_v_y(target_y)))
