import random as r
import pyautogui as pa
import time as t
import keyboard as k
import win32api as wa
import win32con as wc
import win32gui as wg
import win32ui as wu
from pywinauto import application
import pydirectinput as pd
import threading as thr
import sys
import signal as sgn
import ctypes

pd.FAILSAFE = True
kStack = {}

def countdown(mins = 0.07):
    global timer
    timer = mins * 60

    while timer > 0:
        t.sleep(1)
        timer -= 1

def keyDown(key):
    pd.keyDown(key)
    kStack[key] = 1

def keyUp(key):
    pd.keyUp(key)
    kStack[key] = 0

def stop():
    pd.FAILSAFE = False
    for key in kStack:
        if kStack[key] == 1:
            keyUp(key)
            print(f"reset '{key}'")

    sys.exit()