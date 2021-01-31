import win32api
import ctypes
import time
import pyttsx3
import random
import win32gui

#Loop settings
active = True
paused = False
#TTS Settings
engine = pyttsx3.init()
engine.setProperty("volume", 0.5)
engine.setProperty("rate", 350)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("Started")
engine.runAndWait() #Run engine.say and wait till done
########### Recoil Tables
Recoil_AK = [[-36.3583, 52.3906], [5.6019, 48.1107], [-57.7970, 43.7258], [-44.4413, 39.2358], [-0.1867, 34.6408], [17.4687, 29.9408], [30.7335, 25.1358], [39.6080, 20.2258], [44.0919, 15.2107], [44.1854, 10.0906], [39.8884, 10.3678], [31.2010, 19.1802], [18.1232, 26.1569], [0.9701, 31.1046], [-15.7055, 34.0233], [-28.9507, 34.9129], [-38.7704, 33.7734], [-45.1648, 30.6050], [-48.1337, 25.4073], [-47.6774, 18.1807], [-43.7956, 8.9251], [-36.4885, 5.1987], [-25.7559, 14.5390], [-11.5980, 21.8952], [12.5535, 26.8223], [37.8676, 29.3207], [50.8869, 29.3899], [51.5930, 27.0302], [39.9856, 22.2415]]
Recoil_LR = [[-2.5716, 26.2726], [-6.499, 32.5123], [-10.5691, 34.6882], [-15.0501, 32.8004], [-16.5015, 26.8927], [-14.8903, 21.6664], [-10.2167, 18.6228], [-2.3359, 15.8424], [9.5645, 13.3251], [18.0725, 11.0709], [21.0806, 9.0797], [18.5887, 7.3517], [10.5968, 5.9258], [-0.4584, 5.1813], [-5.8302, 4.6544], [-9.7352, 4.1882], [-12.7238, 3.7826], [-14.7961, 3.4377], [-15.952, 3.1534], [-16.1917, 2.9299], [-15.5149, 2.7669], [-13.9219, 2.6647], [-11.4124, 2.6231], [-7.9867, 2.6421], [-3.5444, 2.7219], [14.0846, 2.8623], [32.0283, 3.0633], [37.866, 3.325], [31.5974, 3.6474], [0, 8], [50, 0]]
Recoil_MP5 = [[0.0, 22.7147], [0.0, 30.6766], [0.0, 34.7248], [13.3435, 34.8592], [30.7689, 31.0798], [34.3019, 23.3867], [23.9426, 13.707], [0.8672, 11.269], [-18.9216, 10.0634], [-26.0428, 8.9233], [-20.646, 7.8488], [-3.9165, 6.8398], [8.0986, 5.8965], [14.5347, 5.0187], [17.5745, 4.2065], [17.2181, 3.4598], [13.4654, 2.7788], [6.3166, 2.1633], [-1.4959, 1.6134], [-5.6295, 1.129], [-8.8974, 0.7103], [-11.3639, 0.3571], [-13.0287, 0.0695], [-13.8921, -0.1525], [-13.9539, -0.3089], [-13.2142, -0.3999], [-11.673, -0.4251], [-9.3302, -0.3848], [-6.1859, -0.279], [0, 8], [50, 0]]
Recoil_Custom = [[-13.9306, 27.9232], [-6.7788, 27.6898], [-0.4073, 26.938], [6.248, 25.6679], [10.4567, 23.8793], [11.5526, 21.5724], [9.5355, 18.7471], [4.4055, 16.0817], [-3.1726, 14.6362], [-9.0352, 13.3281], [-11.5846, 12.1185], [-10.8178, 11.0074], [-6.7348, 9.9947], [0.2566, 9.0805], [6.347, 8.2648], [9.8395, 7.5476], [10.7665, 6.9289], [9.128, 6.4086], [4.9239, 5.9868], [-0.9875, 5.6635], [-4.7353, 5.4387], [-6.3062, 5.3123], [-5.7881, 5.2844], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]]
Recoil_Thompson = [[-15.8279, 33.4964], [-5.8047, 33.011], [3.5853, 31.6299], [11.3567, 29.353], [13.8312, 26.1803], [10.9266, 22.1118], [2.6596, 18.7347], [-7.7474, 16.766], [-13.3286, 14.9674], [-13.1795, 13.339], [-7.3, 11.8808], [2.7772, 10.5928], [10.0402, 9.4749], [12.8529, 8.5271], [11.2323, 7.7496], [5.1785, 7.1422], [-2.8139, 6.705], [-6.8923, 6.438], [-7.3495, 6.3412], [-29, 5], [-28, 0], [-21, 5], [-12, 13], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]]
########### Recoil Timings
ak_delay = (400 / 3) / 1000
lr_delay = 120 / 1000
mp5_delay = 100 / 1000
custom_delay = 100 / 1000
tom_delay = 129.22 / 1000
semi_delay = 150 / 1000
m249_delay = 103 / 1000
#Multipliers
all_scopes = ["None", "8x", "16x", "Holo", "Simple",]
all_weapons = ["None", "AK", "LR", "MP5", "Custom", "Thompson"]
active_weapon = 0
active_scope = 0
active_scope_value = 1
sense = 0.5
#Getting sensitvity
file = open('C:\Program Files (x86)\Steam\steamapps\common\Rust\cfg\client.cfg')
for line in file:
    if "input.sensitivity" in line:
        line = line.removeprefix("input.sensitivity")
        line = line.replace('"', '')
        sense = float(line)
file.close()

def mouse_move_random(x,y,draw_delay):
    divider = random.randint(25,100)
    draw_delay = draw_delay / divider
    moveindex = 0
    dxindex = 0
    dyindex = 0
    dx = int(x / divider)
    rx = abs(x - dx * divider)
    dy = int(y / divider)
    ry = y % divider

    while moveindex < divider:
        start_time = time.perf_counter()
        ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 0)
        moveindex += 1

        if rx * moveindex  > (dxindex + 1) * divider:
            dxindex += 1
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 0)
        if ry * moveindex  > (dyindex + 1) * divider:
            dyindex += 1
            ctypes.windll.user32.mouse_event(0x0001, 0, int(y/abs(y)), 0, 0)
        # randomization add start
        if random.rand() < 0.3:
            rdx = random.choice([-2, -1, 0, 1, -2])
            rdy = random.choice([-2, -1, 0, 1, -2])
            ctypes.windll.user32.mouse_event(0x0001, int(rdx * x/abs(x)), int(rdy * y/abs(y)), 0, 0)
            dxindex += rdx
            dyindex += rdy
        # randomization add ended
        time.sleep(draw_delay - (time.perf_counter() - start_time))

    ctypes.windll.user32.mouse_event(0x0001, int(round(x) - dxindex*int(x/abs(x))-dx*moveindex), 
        int(round(y) - dyindex*int(y/abs(y))-dy*moveindex), 0, 0)
    # print(x, y, "=>", round(x), round(y))

def mouse_move(x,y,draw_delay):
    divider = random.randint(25,100)
    start_time = time.perf_counter()
    moveindex = 0
    dxindex = 0
    dyindex = 0
    dx = int(x / divider)
    absx = abs(x - dx * divider)
    dy = int(y / divider)
    ry = y % divider
    while moveindex < divider:
        ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 0)
        moveindex += 1
        if absx * moveindex  > (dxindex + 1) * divider:
            dxindex += 1
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 0)
        if ry * moveindex  > (dyindex + 1) * divider:
            dyindex += 1
            ctypes.windll.user32.mouse_event(0x0001, 0, int(y/abs(y)), 0, 0)
    if x != 0 and y != 0:
        if round(x) != dxindex*int(x/abs(x))+dx*moveindex:
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 0)
            dxindex += 1
        if round(y) != dyindex*int(y/abs(y))+dy*moveindex:
            ctypes.windll.user32.mouse_event(0x0001, int(y/abs(y)), 0, 0, 0)
            dyindex += 1
    time.sleep(draw_delay - (time.perf_counter() - start_time))
#print(x, y, "=>", dxindex*int(x/abs(x))+dx*moveindex, dyindex*int(y/abs(y))+dy*moveindex)

def call_move(draw_pattern, delay):
    current_index = 0
    while current_index < len(draw_pattern) and win32api.GetKeyState(0x01) < 0:
        recoil_x = (((draw_pattern[current_index][0] / 2) / sense) * active_scope_value)
        recoil_y = (((draw_pattern[current_index][1] / 2) / sense) * active_scope_value)
        # print(recoil_x)
        mouse_move(recoil_x, recoil_y, delay)
        current_index += 1

def scope_change(): #Changes the current scope value
    if active_scope == 4:
        return 0
    else:
        return active_scope + 1

def get_active_scope_value():
    if active_scope == 0: #None
        return 1
    elif active_scope == 1: #8x
        return 3.84
    elif active_scope == 2: #16x
        return 7.68
    elif active_scope == 3: #Holo
        return 1.2
    elif active_scope == 4: #Simple
        return 0.8

def weapon_change(int): #Changes the current weapon value
    if int == -1 and active_weapon == 0:
        return 5
    elif int == 1 and active_weapon == 5:
        return 0
    else:
        return (active_weapon + int)

def call_recoil_control(): #Passing control() the correct values
    if active_weapon == 1:
        call_move(Recoil_AK, ak_delay)
    elif active_weapon == 2:
        call_move(Recoil_LR, lr_delay)
    elif active_weapon == 3:
        call_move(Recoil_MP5, mp5_delay)
    elif active_weapon == 4:
        call_move(Recoil_Custom, custom_delay)
    elif active_weapon == 5:
        call_move(Recoil_Thompson, tom_delay)

while active: #Main loop
    if not paused and (win32gui.GetWindowText(win32gui.GetForegroundWindow()) != "Rust"): #Checks if rust is open
        if win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0:
            call_recoil_control()
        if win32api.GetKeyState(0x23) < 0: #End 
            engine.say("Exiting")
            engine.runAndWait()
            active = False
        if win32api.GetKeyState(0x22) < 0: #PageDown
            #win32api.SetCursorPos([300, 300]) #For drawing in paint (debugging)
            active_weapon = weapon_change(1)
            engine.say(all_weapons[active_weapon])
            engine.runAndWait()
        if win32api.GetKeyState(0x21) < 0: #PageUp
            active_weapon = weapon_change(-1)
            engine.say(all_weapons[active_weapon])
            engine.runAndWait()
        if win32api.GetKeyState(0x24) < 0: #Home
            active_scope = scope_change()
            active_scope_value = get_active_scope_value()
            engine.say(all_scopes[active_scope])
            engine.runAndWait()
    if win32api.GetKeyState(0x13) < 0: #Pause
        paused = not paused
        if paused:
            engine.say("Paused")
            engine.runAndWait()
        elif not paused:
            engine.say("Unpaused")
            engine.runAndWait()