from imports import *

lgap = r.randint(194, 234) / 1000
mgap = r.randint(84, 96) / 1000
sgap = r.randint(12, 16) / 1000

jump = 'space'
att1 = 'e'
att2 = 'q'
cdAtt1 = 'a'
cdAtt2 = 'd'
cdAtt3 = 'f'
cdAtt4 = 't'
cdAtt5 = '5'
cdAtt6 = 's'
cdAtt7 = '4'
buff = '9'
totem = '6'

lrot = 0
srot = 0

def attack():
    if srot % 73 == 0:
        pd.press(cdAtt5)
        t.sleep(0.1)
        t.sleep(mgap)
    elif srot % 27 == 0:
        pd.press(cdAtt1)
        t.sleep(0.1)
        t.sleep(mgap)
    elif srot % 13 == 0:
        pd.press(cdAtt2)
        t.sleep(0.1)
        t.sleep(mgap)
    else:
        pd.press(att1)
        pd.press(att2)

def dashAtt():
    global srot
    lgap = r.randint(180, 194) / 1000
    mgap = r.randint(52, 67) / 1000
    sgap = r.randint(13, 16) / 1000

    pd.PAUSE = 0.05
    pd.press(jump)
    keyDown(jump)
    pd.PAUSE = 0.1
    t.sleep(sgap)
    attack()
    t.sleep(0.03)
    keyUp(jump)
    srot += 1

def DdashAtt():
    global srot
    lgap = r.randint(180, 194) / 1000
    mgap = r.randint(52, 67) / 1000
    sgap = r.randint(13, 16) / 1000

    pd.PAUSE = 0.05
    pd.press(jump)
    pd.press(jump)
    keyDown(jump)
    pd.PAUSE = 0.1
    t.sleep(sgap)
    attack()
    t.sleep(0.03)
    keyUp(jump)
    srot += 1

def forward(cycles = 2, dir = 'right'):
    lgap = r.randint(200, 213) / 1000
    mgap = r.randint(52, 87) / 1000
    sgap = r.randint(20, 22) / 1000

    keyDown(dir)
    for i in range(cycles):
        dashAtt()
        t.sleep(sgap)
    keyUp(dir)

def Dforward(cycles = 2, dir = 'right'):
    lgap = r.randint(200, 213) / 1000
    mgap = r.randint(52, 87) / 1000
    sgap = r.randint(20, 22) / 1000

    keyDown(dir)
    for i in range(cycles):
        DdashAtt()
        t.sleep(sgap)
    keyUp(dir)

def drop(cycles = 1):
    lgap = r.randint(194, 234) / 1000
    sgap = r.randint(11, 25) / 1000

    for i in range(cycles):
        keyDown('down')
        keyDown('space')
        t.sleep(sgap)
        keyUp('space')
        keyUp('down')
        t.sleep(lgap)

def jumpAtt():
    lgap = r.randint(200, 213) / 1000
    mgap = r.randint(52, 87) / 1000
    sgap = r.randint(20, 22) / 1000

    pd.PAUSE = 0.05
    pd.press(jump)
    keyDown('up')
    pd.press(jump)
    pd.PAUSE = 0.1
    keyUp('up')
    t.sleep(lgap)
    attack()
    t.sleep(mgap)

def altPath():
    pd.press('right')
    pd.press(jump)
    t.sleep(lgap)
    keyDown('up')
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('up')
    pd.press('right')
    keyDown('right')
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('right')
    t.sleep(sgap)
    keyDown(cdAtt7)
    t.sleep(0.2)
    keyUp(cdAtt7)
    t.sleep(2.7)
    keyDown('down')
    keyDown('space')
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('down')
    keyUp('space')
    pd.press('left')
    keyDown('left')
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('left')

def altPath2():
    keyDown('right')
    t.sleep(lgap)
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('right')
    keyDown('right')
    t.sleep(lgap)
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('right')
    t.sleep(sgap)
    keyDown(cdAtt7)
    t.sleep(0.2)
    keyUp(cdAtt7)
    t.sleep(2.7)
    keyDown('right')
    t.sleep(lgap)
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('right')
    keyDown('right')
    t.sleep(lgap)
    pd.press(cdAtt3)
    t.sleep(sgap)
    keyUp('right')
    t.sleep(mgap)


t.sleep(3)

limit = 91

'''
try:
    while lrot < limit:
        print(lrot)
        if lrot % 10 == 0:
            keyDown(cdAtt4)
            t.sleep(0.2)
            keyUp(cdAtt4)
            t.sleep(0.5)
            keyDown(totem)
            t.sleep(mgap)
            keyUp(totem)
            t.sleep(lgap)

        if lrot % 27 == 0:
            pd.press(buff)
            t.sleep(1)

        if (lrot - 5) % 9 == 0:
            altPath2()
        else:
            forward(3)
            t.sleep(mgap)
            if lrot % 9 == 0:
                pd.press(cdAtt6)
                t.sleep(1)
            forward(3, 'left')
        lrot += 1

finally:
    stop()
'''

try:
    while lrot < limit:
        if lrot % 14 == 0:         #whether buff (was 27)
            pd.press('9')
            t.sleep(1)
            print('buffed')

        print(lrot)
        if lrot % 5 == 0:         #whether shadow veil and totem (was 7)
            keyDown(cdAtt4)
            t.sleep(0.2)
            keyUp(cdAtt4)
            t.sleep(0.6)
            keyDown(totem)
            t.sleep(mgap)
            keyUp(totem)
            t.sleep(lgap * 3)

        if (lrot - 5) % 9 == 0:    #whether altpath2
            altPath2()
            forward(2)
        else:
            forward(5)
        
        t.sleep(mgap)
        if lrot % 9 == 0:
            pd.press(cdAtt6)
            t.sleep(1)
        pd.press('left')
        jumpAtt()

        if (lrot - 3) % 4 == 0:     #whether alt return route
            keyDown('left')
            jumpAtt()
            keyUp('left')
            forward(3, 'left')
            t.sleep(0.3)
            forward(1, 'left')
            t.sleep(lgap)
            drop()
            t.sleep(mgap)
        else:
            Dforward(3, 'left')
            t.sleep(lgap)
        
        lrot += 1

finally:
    stop()