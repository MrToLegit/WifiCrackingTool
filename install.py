import os
import platform
import time

clear = lambda: os.system('clear')

if platform.system() != "Linux":
    print("You can run this script only on Linux based devices.")
    quit()

print("Welcome to the autoinstaller. Please wait this can take some time....")
time.sleep(1)

os.system("apt-get update -y")

os.system("apt-get install python3 -y")

os.system("python3 -m pip install netifaces")

print("Succesfully installed everything!\nNow you can run the program with 'python3 tool.py'")
