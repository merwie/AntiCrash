import psutil
import os
import time
import sys
from infi.systray import SysTrayIcon

global on
on = "yes"
test = "yes"


def Version(systray):
    print("Public.V1")


menu_options = (("Version", None, Version),)
systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options)


def on_quit_callback(systray):
    global on
    on = "no"
    print("Stopping the script(Might run one more time")


systray = SysTrayIcon("icon.ico", "Example tray icon", menu_options, on_quit=on_quit_callback)
systray.start()

while on == "yes":
    ipr = "no"
    alr = "no"
    for process in psutil.process_iter():
        if process.name() == 'iproyal_pawns.exe':
            print("already running")
            alr = "yes"

    if process.name() != 'iproyal_pawns.exe':
        print("not running")
        ipr = "yes"
        if alr == "yes":
            ipr = "no"

    if ipr == "yes":
        os.startfile('C:\Program Files (x86)\IPRoyalPawns\iproyal_pawns.exe')
    time.sleep(300)

input('Press ENTER to exit')
