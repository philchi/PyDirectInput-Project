import pydirectinput as pd
import pyautogui as pa
import time as t
import os

with open('read.txt') as read:
    out = read.readlines()

'''
os.startfile('write.txt')
'''

t.sleep(5)
for n in out:
    pa.write(n)