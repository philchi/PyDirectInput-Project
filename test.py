from imports import *

#txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#txt2 = "My name is {0}, I'm {1}".format("John",36)
'''
pressed = {}
pressed['good'] = 0
pressed['wow'] = 0

for i in pressed:
    print(i)
'''

pd.keyDown('a')

if ctypes.windll.user32.GetKeyState(0x41):
    print('worked')
pd.keyUp('a')


'''
import sys
import time
import ctypes as ct
from ctypes import wintypes as wt


def main(*argv):
    user32 = ct.WinDLL("User32.dll")
    GetKeyState = user32.GetKeyState
    GetKeyState.argtypes = (ct.c_int,)
    GetKeyState.restype = wt.USHORT  # !!! It's actually wt.SHORT, but chose unsigned for display purposes !!!

    while 1:
        vkc = 0x41  # 65, 'A'
        ks = GetKeyState(vkc)
        print("Key (0x{:02X}) state: 0x{:04X}\nPressed: {:d}".format(vkc, ks, ks >> 15))
        time.sleep(0.5)


if __name__ == "__main__":
    print("Python {:s} {:03d}bit on {:s}\n".format(" ".join(elem.strip() for elem in sys.version.split("\n")),
                                                   64 if sys.maxsize > 0x100000000 else 32, sys.platform))
    rc = main(*sys.argv[1:])
    print("\nDone.")
    sys.exit(rc)
'''
t.sleep(2)
buff = '9'
pd.press(buff)