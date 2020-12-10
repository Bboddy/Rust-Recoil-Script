import win32api
import time
import pyttsx3
from pynput.mouse import Button, Controller

engine = pyttsx3.init()
engine.setProperty("volume", 0.5)
engine.setProperty("rate", 200)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say("Hello and welcome")
engine.runAndWait()

mouse = Controller()
active = True

ControlTime_Ak47 =  121.96149709966872, 92.6333814724611, 138.60598637206294, 113.37874368443146, 66.25151186427745, 66.29530438019354, 75.9327831420658, 85.05526144256157, 89.20256669256554, 86.68010184667988, 78.82145888317788, 70.0451048111144, 60.85979604582978, 59.51642457624619, 71.66762996283607, 86.74060009403034, 98.3363599080854, 104.34161954944257, 104.09299204005345, 97.58780746901739, 85.48062700875559, 70.4889202349561, 56.56417811530545, 47.386907899993936, 56.63787408680247, 91.5937793023631, 112.38667610336424, 111.39338971888095, 87.5067801164596 

Recoil_Ak47 = { -69.0, 100.0, 10.0, 92.0, -110.0, 83.0, -85.0, 75.0, 0.0, 67.0, 33.0, 57.0, 58.0, 48.0, 76.0, 39.0, 84.0, 29.0, 85.0, 19.0, 76.0, 20.0, 60.0, 37.0, 34.0, 50.0, 2.0, 59.0, -30.0, 65.0, -55.0, 67.0, -74.0, 64.0, -86.0, 59.0, -92.0, 49.0, -91.0, 34.0, -84.0, 17.0, -70.0, 10.0, -49.0, 28.0, -22.0, 42.0, 24.0, 51.0, 72.0, 56.0, 97.0, 57.0, 98.0, 51.0, 77.0, 43.0 } #[0] belongs to [1] and [2] belongs to [3] so forth and so on
Recoil_Lr300 = { 0, 50, -11, 60, -22, 67, -28, 59, -31, 50, -29, 42, -9, 38, -9, 30, 23, 25, 36, 24, 35, 13, 40, 19, 18, 6, 0, 17, -13, 6, -16, 5, -19, 6, -34, 12, -31, 2, -29, 5, -28, 0, -21, 5, -12, 13, -7, 0, 19, 5, 3, 11, 61, 0, 73, 0, 54, 6, 0, 8, 50, 0 }
Recoil_Mp5a4 = { 0, 43, 0, 58, 0, 65, 25, 66, 59, 58, 63, 42, 46, 27, 3, 23, -37, 19, -47, 18, -40, 18, -8, 7, 16, 12, 28, 11, 35, 9, 34, 8, 25, 6, 12, 0, -4, 2, -6, 2, -18, 0, -27, 5, -26, 0, -27, 0, -20, 0, -32, 0, -12, 0, -25, 0, -4, 0, 0, 0, 43, 0 }
Recoil_Custom_g = { -28, 52, -10, 53, 0, 53, 11, 44, 20, 45, 22, 42, 17, 35, 7, 30, -9, 27, -13, 28, -23, 22, -21, 21, -15, 24, 0, 13, 20, 14, 16, 12, 29, 19, 7, 6, 11, 10, -4, 8, -8, 13, -7, 2, -13, 14 }
Recoil_Thompson_g = { -29, 63, -12, 61, 9, 61, 21, 55, 25, 52, 21, 43, 5, 32, -16, 33, -24, 25, -24, 26, -14, 21, 7, 17, 16, 18, 23, 16, 25, 17, 8, 16, -5, 5, -13, 15, -14, 8 }
Recoil_Semi_r = { 0, 75, 0, 75 }
Recoil_M249 = { 0, 58, 0, 58 }

ak_delay = 133.3333
lr_delay = 118
mp6_delay = 98
custom_delay = 99
tom_delay = 127
semi_delay = 150
m249_delay = 103

scope_x8 = 3.84
scope_x16 = 7.68
scope_holo = 1.2
scope_simple = 0.8
scope_none = 1.0

barrel_suppressor = 0.8
barrel_none = 1.0

Reload = False
AK47 = False
LR300 = False
MP5 = False
CSMG = False
THOMPSON = False
Semi = False
M249 = False
s8x = False
Holo = False
Simple = False
Suppressor = False
MuzzleBoost = False

userSens = 0.4

global all_weapons, current_weapon, current_weapon_name
all_weapons = ["None", "AK", "LR", "MP5", "Custom", "Thompson", "Sar", "M249"]
current_weapon = 0
current_weapon_name = all_weapons[0]

def weapon_change(num):
    current_weapon = current_weapon + num
    current_weapon_name = all_weapons[current_weapon]


while active:
    while win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0:
        mouse.move(-1,-1)
        time.sleep(0.001)
    if win32api.GetKeyState(0x2D) < 0: #insert key
        engine.say("Exiting")
        engine.runAndWait()
        active = False
    if win32api.GetKeyState(0x21) < 0: #page up
        weapon_change(1)
        engine.say(current_weapon_name)
        engine.runAndWait()
    if win32api.GetKeyState(0x22) < 0: #page down
        weapon_change(-1)
        engine.say(current_weapon_name)
        engine.runAndWait()