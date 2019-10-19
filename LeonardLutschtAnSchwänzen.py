import os
import time
import platform

print("\033[0;0;32mWelcome to the WlanCrack automatic script. Made by ToLegit & MikeMike.\nIf you want to quit press simply CTRL and C. Please follow the steps.\nHave a nice day. \033[0m\n")

print("Do you agree that this script is only for educational use? [y/n]")

agreeinput = input()

if agreeinput != "y" and not "Y":
    print("You have to agree. Good bye.")
    quit()

print("I hope it for you.\n")

if platform.system() != "Linux":
    print("You can run this script only on Linux based devices.")
    quit()

time.sleep(0.2)

print("Please enter your interface name. \nDefault: wlan0")

wlaninput = input()

if wlaninput == "":
    wlaninput = "wlan0"

while os.system("cat /sys/class/net/"+wlaninput+"/operstate") != "up":
    print("Interface not found or is not online.")
    wlaninput1 = input()

    if wlaninput1 == "":
        wlaninput1 = "wlan0"

    wlaninput = wlaninput1

print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode")

mode = input()

while mode != 1 and not 2:
    print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode")

    modenew = input()

    mode = modenew

def function_mode_1():
    os.system("airmon-ng check kill")
    time.sleep(0.2)
    os.system("airmon-ng start " + wlaninput)
    time.sleep(0.2)

def function_mode_2():
    os.system("airmon-ng check kill")
    time.sleep(0.2)
    os.system("iwconfig " + wlaninput + " mode monitor")
    time.sleep(0.2)

if mode == 1:
    function_mode_1()
elif mode == 2:
    function_mode_2()

os.system("iwconfig " + wlaninput)

print("Is the interface in monitor mode? [y/n]")

interfacecheck = input()

while interfacecheck != "y" and not "Y":
    if mode == 1:
        function_mode_1()
    elif mode == 2:
        function_mode_2()

    os.system("iwconfig " + wlaninput)

    print("Is the interface now in monitor mode? [y/n]")

    interfacecheck1 = input()

    interfacecheck = interfacecheck1