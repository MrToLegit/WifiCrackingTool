import os
import time
import platform
import subprocess
import netifaces

clear = lambda: os.system('clear')


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

clear()

print("Here are your interfaces:")
os.system("iwconfig")

print("Please enter your interface name. \nDefault: wlan0")

wlaninput = input()

if wlaninput == "":
    wlaninput = "wlan0"

def is_interface_up(interface1):
    interface_list = netifaces.interfaces()
    if interface1 in interface_list:
        return True
    return False

print("\n" + str(is_interface_up(wlaninput)))

while not is_interface_up(wlaninput):
    print("Interface not found or is not online.")
    wlaninput1 = input()
    if wlaninput1 == "":
        wlaninput1 = "wlan0"
    wlaninput = wlaninput1

clear()

print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode")

mode = input()

while not mode == 1 and not mode == 2:
    print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode")
    modenew = input()
    mode = modenew

if mode == 1:
    os.system("airmon-ng check kill")
    time.sleep(0.2)
    os.system("airmon-ng start " + wlaninput )
    time.sleep(0.2)
elif mode == 2:
    os.system("airmon-ng check kill")
    time.sleep(0.2)
    os.system("iwconfig " + wlaninput + " mode monitor")
    time.sleep(0.2)

clear()

os.system("iwconfig " + wlaninput)

print("Is the interface in monitor mode? [y/n]")

interfacecheck = input()

while True:
    if interfacecheck != "y" and not "Y":
        if mode == 1:
            os.system("airmon-ng check kill")
            time.sleep(0.2)
            os.system("airmon-ng start " + wlaninput )
            time.sleep(0.2)
        elif mode == 2:
            os.system("airmon-ng check kill")
            time.sleep(0.2)
            os.system("iwconfig " + wlaninput + " mode monitor")
            time.sleep(0.2)

        os.system("iwconfig " + wlaninput)

        print("Is the interface now in monitor mode? [y/n]")

        interfacecheck1 = input()

        interfacecheck = interfacecheck1
    else:
        break

print("Gud Gud my soldier")