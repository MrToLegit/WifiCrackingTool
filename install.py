import os
import platform
import time

clear = lambda: os.system('clear')

if platform.system() != "Linux":
    print("You can run this script only on Linux based devices.")
    quit()

print("Welcome to the autoinstaller. Please wait this can take some time....")
time.sleep(1)

os.system("apt-get install python3")

os.system("python3 -m pip install netifaces")
os.system("python3 -m pip install os")
os.system("python3 -m pip install platform")
os.system("python3 -m pip install time")
os.system("python3 -m pip install subprocess")
os.system("python3 -m pip install webbrowser")

print("Succesfully installed everything!\nNow you can run the program with 'python3 tool.py'")
