from imports import *

lgap = r.randint(194, 234) / 1000
mgap = r.randint(52, 87) / 1000
sgap = r.randint(11, 15) / 1000

jump = 'space'
att1 = 'w'
att2 = 'e'
cdAtt1 = 'q'
cdAtt2 = 'r'

def attack():
    lgap = r.randint(160, 194) / 1000
    mgap = r.randint(52, 87) / 1000
    sgap = r.randint(11, 25) / 1000

    keyDown('down')
    keyDown(att1)
    keyDown(att2)
    t.sleep(sgap)
    keyUp(att1)
    t.sleep(sgap)
    keyUp('down')
    keyUp(att2)

def dashAtt():
    lgap = r.randint(180, 194) / 1000
    mgap = r.randint(52, 87) / 1000
    sgap = r.randint(11, 15) / 1000

    keyDown(jump)
    keyUp(jump)
    keyDown(jump)
    t.sleep(sgap)
    attack()
    keyUp(jump)

def jumpAtt(cycles = 2):
    lgap = r.randint(160, 194) / 1000
    mgap = r.randint(52, 87) / 1000
    sgap = r.randint(11, 25) / 1000
    
    for i in range(cycles):
        keyDown('up')
        keyDown(att1)
        t.sleep(sgap)
        keyUp('up')
        keyUp(att1)
        t.sleep(sgap)

    attack()

def forward(cycles = 2, dir = 'right'):
    lgap = r.randint(200, 213) / 1000

    keyDown(dir)
    for i in range(cycles):
        dashAtt()
        t.sleep(lgap)
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
    


t.sleep(3)
timerThr = thr.Thread(target = countdown())
timerThr.start()


while timer > 0:
    forward(3)
    t.sleep(sgap)
    jumpAtt()
    pd.press('left')
    t.sleep(mgap)
    forward(3, 'left')
    drop(2)
    attack()
    t.sleep(sgap)
    pd.press('right')
    t.sleep(mgap)


#while not k.is_pressed('esc'):
#    pa.press('space')