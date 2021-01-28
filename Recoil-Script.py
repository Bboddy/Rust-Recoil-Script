import numpy as np
import win32api
import ctypes
import time
#Interp-Movements Branch
draw_pattern = [[-36.3583, 52.3906], [5.6019, 48.1107], [-57.7970, 43.7258], [-44.4413, 39.2358], [-0.1867, 34.6408], [17.4687, 29.9408], [30.7335, 25.1358], [39.6080, 20.2258], [44.0919, 15.2107], [44.1854, 10.0906], [39.8884, 10.3678], [31.2010, 19.1802], [18.1232, 26.1569], [0.9701, 31.1046], [-15.7055, 34.0233], [-28.9507, 34.9129], [-38.7704, 33.7734], [-45.1648, 30.6050], [-48.1337, 25.4073], [-47.6774, 18.1807], [-43.7956, 8.9251], [-36.4885, 5.1987], [-25.7559, 14.5390], [-11.5980, 21.8952], [12.5535, 26.8223], [37.8676, 29.3207], [50.8869, 29.3899], [51.5930, 27.0302], [39.9856, 22.2415]]
draw_delay = (400 / 3 / 1000)
divider = 25

def mouse_move(x,y):
    moveindex = 0
    dxindex = 0
    dyindex = 0
    dx = int(x / divider)
    rx = abs(x - dx * divider)
    dy = int(y / divider)
    ry = y % divider

    while moveindex < divider:
        ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 0)
        moveindex += 1

        if rx * moveindex  > (dxindex + 1) * divider:
            dxindex += 1
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 0)
        if ry * moveindex  > (dyindex + 1) * divider:
            dyindex += 1
            ctypes.windll.user32.mouse_event(0x0001, 0, int(y/abs(y)), 0, 0)
        time.sleep(draw_delay / divider)

    if round(x) != dxindex*int(x/abs(x))+dx*moveindex:
        ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 0)
        dxindex += 1
    if round(y) != dyindex*int(y/abs(y))+dy*moveindex:
        ctypes.windll.user32.mouse_event(0x0001, int(y/abs(y)), 0, 0, 0)
        dyindex += 1
        
    print(x, y, "=>", dxindex*int(x/abs(x))+dx*moveindex, dyindex*int(y/abs(y))+dy*moveindex)
    

def draw():
    current_index = 0
    active_value = 1
    sense = 0.5
    while current_index < len(draw_pattern) and win32api.GetKeyState(0x01) < 0:
        recoil_x = (((draw_pattern[current_index][0] / 2) / sense) * active_value)
        recoil_y = (((draw_pattern[current_index][1] / 2) / sense) * active_value)
        # print(recoil_x)
        mouse_move(recoil_x, recoil_y)
        current_index += 1

active = True

while active:
    if win32api.GetKeyState(0x01) < 0:
        draw()
    if win32api.GetKeyState(0x22) < 0: #PageDown
        win32api.SetCursorPos([300, 300]) #For drawing in paint (debugging)