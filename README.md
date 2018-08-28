Simple python program to check who is in home.
Author: Andrzej Michalski
WWW: www.michalski.in

Code consist two main scripts - bash script - "whois.sh" and python script - "whois.py
In addition there are unittests in file "tests.py"

Bash script require to have nmap installed: https://nmap.org/

It scan WIFI and search hosts. After searching hosts are written in file "active_macs.txt".
Each host in new line in style: "MAC_adress IP_adress"

Python script need to have file "home_macs.txt" created in convencion:
"MAC_adress IP_adress HOST_name"

To see what is text files structure see "tests.py" file.

Python script cope with text files and print output text in console.

It is designed to work on Raspberry Pi Zero W.

