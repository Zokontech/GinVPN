CIS4362 Introduction to Cryptology
GinVPN-Final Project
Alexander Krasny
December 9, 2020
GINVpn  Installation Guide and User Manual
Installation instructions
Depending on system configurations, the python running scripts is likely ‘python’ or ‘python3’
For the remainder of the user manual, I will assume this command is ‘python’
GinVPN is installable from PyPi
To install, use the following command:
>python -m pip install GinVPN-Zokontech
It should install the necessary dependencies. If this fails, use pip in the same manner to install the following packages
•	proxy.py
•	aiohttp
•	PyAutoGUI
When GinVPN and proxy.py are installed, they should create the executables required to run the program in a folder that is in the path environmental variable, however, if this folder is not in path, add it to the path. 

Configuration
In order to properly utilize GinVPN, you must first run the GinConfig script
>GinConfig
It will generate the AES key, and prompt the input of a server and port for the VPN server to run on. By default, it will run on 127.0.0.1 port 5000, but depending on the OS, the address might need to be altered. 
GinConfig can also be run to alter the parameters of the program individually. It can generate a new key, and alter the server parameters.
Running
To run the program use the following commands in separate terminal windows.
>GinServer
>proxy --plugins GinVPN.plugin.GinVPNPlugin --hostname 0.0.0.0
To use, make a curl request like the following using the proxy.
>curl -x localhost:8899 http://www.example.com
Depending on the OS, localhost might need to be substituted for 127.0.0.1 (linux)
The server tends to get overwhelmed from multiple requests. The system works best when performing one request at a time. 
Happy Encrypting!

