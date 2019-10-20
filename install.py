import os
import platform
import time

clear = lambda: os.system('clear')

colorgreen = "\033[0;0;32m"
colorreset = "\033[0m"
colorred = "\033[0;0;31m"
colorblue = "\033[0;0;34m"

if platform.system() != "Linux":
    print(colorred + "You can run this script only on Linux based devices." + colorreset)
    quit()

print(colorgreen+"Welcome to the autoinstaller. Please wait this can take some time....")
time.sleep(1)

os.system("apt-get update -y")

os.system("apt-get install python3 -y")

os.system("python3 -m pip install netifaces")
os.system("python3 -m pip install playsound")

print("Succesfully installed everything!\nNow you can run the program with 'python3 tool.py'" + colorreset)
