# import dependencies
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
from winotify import Notification, audio
import time

toast = Notification(
    app_id="MuteApp", title="MuteApp", msg="MuteApp has stopped!", duration="short"
)
toast.set_audio(audio.Default, loop=False)


# gets the process name and PID, checking for invalid PID that could crash script
def get_process_name():
    try:
        hwnd = win32gui.GetForegroundWindow()
        time.sleep(0.05)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        if pid > 0:
            process = psutil.Process(pid)
            process_name = process.name()
            return process_name
        else:
            return None

    except psutil.NoSuchProcess:
        return None


# draw ui
myUI.create_ui()

# import the variables set after the ui is closed
from variables import *

# main function to monitor process' and control volume
while running:
    process_name = get_process_name()
    if process_name is not None:
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
            toast.show()
            break
