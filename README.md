Please read the LICENSE.

First run "install.py" with python3
like so: python3 install.py
no error means success

Then start "tool.py"
again with python3
python3 tool.py

It will ask for check for update hit "y" it will
automatically update the repository
after that the script will close itself 
start it again with python3 tool.py

After the update screen it will ask for you wifi
interface if you leave it blank and press enter
it will choose the default one (wlan0)

After asking for the interface the script will ask
which way it should use to put your
wifi card into monitor mode 

it will automatically do airmon-ng check kill
no mattr wich option you choose

while option
1 is using airmon-ng (airmon-ng start [interface])

2 is using iwconfig (iwconfig [interface] mode monitor)

3 is using iwconfig (ifconfig [interface] down then mode monitor and again up)

After that it will ask you if you wifi card is in monitor mode
after processing with y for yes 
it will ask you if you want to crack a wifi password
(but dont use it because its a little bit buggy)
(work in progress)

you can use the script in a GUI when you start the script with "python3 MonitorModeGUI.py"
