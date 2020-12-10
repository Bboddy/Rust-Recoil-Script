import win32api
import time
from pynput.mouse import Button, Controller

mouse = Controller()
active = True
# pageUp = win32api.GetKeyState(0x21)
# pageDown = win32api.GetKeyState(0x22)

while active:
    while win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0:
        mouse.move(-1,-1)
        time.sleep(0.001)
    if win32api.GetKeyState(0x2D) < 0:
        active = False