import tkinter as tk
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import asyncio

window = tk.Tk()
window.title("LoudReducer - 1.0")
window.geometry('500x500')

reduceLoudSounds = tk.BooleanVar()


def print_selection():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Get current volume 
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb - 10.0, None)

reduceCheckBox = tk.Checkbutton(window, text='Reduce loud sounds',variable=reduceLoudSounds, onvalue=True, offvalue=False, command=print_selection)
reduceCheckBox.pack()

window.mainloop()