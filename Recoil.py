import win32api, ctypes, pyttsx3, random, time
from datetime import datetime, timedelta
#Loop settings
active = True
paused = False
########### Recoil Tables
Recoil_Tables = [
    #Recoil_AK
    [[-35, 50],[5, 46],[-55, 42],[-42, 37],[0, 33],[16, 28],[29, 24],[38, 19],[42, 14],[42, 9],[38, 9],[30, 18],[17, 25],[0, 29],[-15, 32],[-27, 33],[-37, 32],[-43, 29],[-46, 24],[-45, 17],[-42, 8],[-35, 5],[-24, 14],[-11, 21],[12, 25],[36, 28],[49, 28],[49, 26],[38, 21]],
    #Recoil_LR
    [[-2.5716, 26.2726], [-6.499, 32.5123], [-10.5691, 34.6882], [-15.0501, 32.8004], [-16.5015, 26.8927], [-14.8903, 21.6664], [-10.2167, 18.6228], [-2.3359, 15.8424], [9.5645, 13.3251], [18.0725, 11.0709], [21.0806, 9.0797], [18.5887, 7.3517], [10.5968, 5.9258], [-0.4584, 5.1813], [-5.8302, 4.6544], [-9.7352, 4.1882], [-12.7238, 3.7826], [-14.7961, 3.4377], [-15.952, 3.1534], [-16.1917, 2.9299], [-15.5149, 2.7669], [-13.9219, 2.6647], [-11.4124, 2.6231], [-7.9867, 2.6421], [-3.5444, 2.7219], [14.0846, 2.8623], [32.0283, 3.0633], [37.866, 3.325], [31.5974, 3.6474], [0, 8], [50, 0]],
    #Recoil_MP5
    [[0, 21],[0, 29],[0, 33],[12, 33],[29, 29],[33, 22],[23, 13],[0, 10],[-18, 9],[-25, 8],[-19, 7],[-3, 6],[7, 5],[14, 4],[16, 4],[16, 3],[12, 2],[6, 2],[-1, 1],[-5, 1],[-8, 0],[-10, 0],[-12, 0],[-13, 0],[-13, 0],[-12, 0],[-11, 0],[-8, 0],[-5, 0]],
    #Recoil_Custom
    [[-13.9306, 27.9232], [-6.7788, 27.6898], [-0.4073, 26.938], [6.248, 25.6679], [10.4567, 23.8793], [11.5526, 21.5724], [9.5355, 18.7471], [4.4055, 16.0817], [-3.1726, 14.6362], [-9.0352, 13.3281], [-11.5846, 12.1185], [-10.8178, 11.0074], [-6.7348, 9.9947], [0.2566, 9.0805], [6.347, 8.2648], [9.8395, 7.5476], [10.7665, 6.9289], [9.128, 6.4086], [4.9239, 5.9868], [-0.9875, 5.6635], [-4.7353, 5.4387], [-6.3062, 5.3123], [-5.7881, 5.2844], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]],
    #Recoil_Thompson
    [[-15.8279, 33.4964], [-5.8047, 33.011], [3.5853, 31.6299], [11.3567, 29.353], [13.8312, 26.1803], [10.9266, 22.1118], [2.6596, 18.7347], [-7.7474, 16.766], [-13.3286, 14.9674], [-13.1795, 13.339], [-7.3, 11.8808], [2.7772, 10.5928], [10.0402, 9.4749], [12.8529, 8.5271], [11.2323, 7.7496], [5.1785, 7.1422], [-2.8139, 6.705], [-6.8923, 6.438], [-7.3495, 6.3412], [-29, 5], [-28, 0], [-21, 5], [-12, 13], [-7, 0], [19, 5], [3, 11], [61, 0], [73, 0], [54, 6], [0, 8], [50, 0]],
    #M249
    [[0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62], [0, 62]],
    #Sar
    [85,  0],
    #M92
    [82, 0], #Could be 2x'd
    #Python
    [155, 0] #Could be 2x'd
]
Recoil_Delays = [
    0.1333333333, #ak_delay
    0.12, #lr_delay
    0.1, #mp5_delay
    0.1, #custom_delay
    0.12922, #tom_delay
    0.103, #m249_delay
    0.15, #semi_delay
    0.20,
    0.20,
    0.20,
    0.20
]
Scope_Values = [
    #None
    1,
    #8x
    3.84,
    #16x
    7.68,
    #Holo
    1.2,
    #Simple
    0.8
]
#Multipliers
all_scopes = ["None", "8x", "16x", "Holo", "Simple",]
all_weapons = ["AK", "LR", "MP5", "Custom", "Thompson", "M2", "Sar", "M9", "Python"]
active_weapon, active_scope, start_time = 0, 0, 0

def get_sense(): #Getting sensitivity
    global sense
    file = open('C:\Program Files (x86)\Steam\steamapps\common\Rust\cfg\client.cfg') #Path to rust
    for line in file:
        if "input.sensitivity" in line:
            line = line.replace('"', '')
            sense = float(line.replace('input.sensitivity', ''))
    file.close()

def mouse_move_curved(x,y,delay): #Recoil control for curved weapons
    global start_time
    divider = random.randint(10,40) #Smoothing factor
    moveindex, dxindex, dyindex = 0, 0, 0
    dx = int(x / divider)
    absx = abs(x - dx * divider)
    dy = int(y / divider)
    ry = y % divider
    bullet_delay = (delay / (divider)) * 0.60 # 60% of the delay between shots
    while moveindex < divider:
        bullet_start_time = datetime.now()
        ctypes.windll.user32.mouse_event(0x0001, dx, dy, 0, 5) #Move recoil / divider
        moveindex += 1
        if absx * moveindex  > (dxindex + 1) * divider:
            dxindex += 1
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 5)
        if ry * moveindex  > (dyindex + 1) * divider:
            dyindex += 1
            ctypes.windll.user32.mouse_event(0x0001, 0, int(y/abs(y)), 0, 5)
        sleepTime = timedelta(seconds = bullet_delay)
        while bullet_start_time + sleepTime > datetime.now(): #Sleeping in between each smoothing move
            pass
    if x != 0 and y != 0: #Accounting for loss
        if round(x) != dxindex * int(x/abs(x)) + dx * moveindex:
            ctypes.windll.user32.mouse_event(0x0001, int(x/abs(x)), 0, 0, 5)
            dxindex += 1
        if round(y) != dyindex * int(y/abs(y)) + dy * moveindex:
            ctypes.windll.user32.mouse_event(0x0001, int(y/abs(y)), 0, 0, 5)
            dyindex += 1
    sleepTime = timedelta(seconds = delay)
    while start_time + sleepTime > datetime.now(): #This is more accurate then time.sleep()
        pass #This also wont brick if -slept time

def call_move(recoil_pattern, delay):
    global start_time
    current_bullet = 0
    if active_weapon < 6: #Curved weapons that need smoothing
        while current_bullet < len(recoil_pattern) and win32api.GetKeyState(0x01) < 0:
            if current_bullet != 0:
                start_time = datetime.now()
            recoil_x = (((recoil_pattern[current_bullet][0] / 2) / sense) * Scope_Values[active_scope])
            recoil_y = (((recoil_pattern[current_bullet][1] / 2) / sense) * Scope_Values[active_scope])
            if active_weapon == 5 and win32api.GetKeyState(0x11) < 0:
                recoil_x = recoil_x / 2
                recoil_y = recoil_y / 2
            mouse_move_curved(recoil_x, recoil_y, delay)
            current_bullet += 1
    else:
        if current_bullet != 0: # Recoil control for linear weapons that need to be clicked each shot
                start_time = datetime.now()
        recoil_x = (((recoil_pattern[0] / 2) / sense) * Scope_Values[active_scope])
        recoil_y = (((recoil_pattern[1] / 2) / sense) * Scope_Values[active_scope])
        if win32api.GetKeyState(0x11) < 0: #If player crouched, recoil is .5 for these weapons
                recoil_x = recoil_x / 2
                recoil_y = recoil_y / 2
        ctypes.windll.user32.mouse_event(0x0001, int(recoil_y), int(recoil_x), 0, 5)
        sleepTime = timedelta(seconds = delay)
        while start_time + sleepTime > datetime.now() or win32api.GetKeyState(0x01) < 0:
                pass

def scope_change(): #Changes the current scope value
    global active_scope
    if active_scope == 4: #Max number of scopes
        active_scope = 0
    else:
        active_scope += 1

def weapon_change(int): #Changes the current weapon value
    if int == -1 and active_weapon == 0:
        return 8
    elif int == 1 and active_weapon == 8: #Max number of weapons
        return 0
    else:
        return (active_weapon + int)

def run():
    global active, paused, active_weapon, start_time, Recoil_Tables, Recoil_Delays
    #Setting sense
    get_sense()
    #TTS Settings
    engine = pyttsx3.init()
    engine.setProperty("volume", 0.5)
    engine.setProperty("rate", 350)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    engine.say("Started")
    engine.runAndWait() #Run engine.say and wait till done
    while active: #Main loop
        #While not paused
        if not paused:
            if win32api.GetKeyState(0x01) < 0 and win32api.GetKeyState(0x02) < 0: #Left n Right MB
                start_time = datetime.now()
                call_move(Recoil_Tables[active_weapon], Recoil_Delays[active_weapon])
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
                scope_change()
                engine.say(all_scopes[active_scope])
                engine.runAndWait()
        #Doesnt Matter if Paused
        if win32api.GetKeyState(0x91) < 0: #ScrLk
            get_sense()
            engine.say("Updated")
            engine.runAndWait()
        if win32api.GetKeyState(0x13) < 0: #Pause
            paused = not paused
            if paused:
                engine.say("Paused")
                engine.runAndWait()
            elif not paused:
                engine.say("Unpaused")
                engine.runAndWait()
        if win32api.GetKeyState(0x23) < 0: #End 
                engine.say("Exiting")
                engine.runAndWait()
                active = False