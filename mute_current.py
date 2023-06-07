from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume,
    ISimpleAudioVolume,
    AudioSession,
)
import psutil
import win32process, win32gui
import keyboard
import time
import myUI

myUI.create_ui()

from variables import *


while True:
    hwnd = win32gui.GetForegroundWindow()
    time.sleep(0.05)
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    process = psutil.Process(pid)

    process_name = process.name()

    if pid > 0:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))

        sessions = AudioUtilities.GetAllSessions()

        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == process_name:
                if keyboard.is_pressed(muteKey):
                    volume.SetMute(1, None)

                if keyboard.is_pressed(unmuteKey):
                    volume.SetMute(0, None)

        if keyboard.is_pressed(exitKey):
            break
