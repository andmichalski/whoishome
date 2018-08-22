#!/bin/sh

sudo nmap -n -sP 192.168.2.1/24 | awk '/Nmap scan report for /{printf $5x;printf " ";getline;getline;print $3x}' > active_macs.txt
my_ip=$(hostname -I)
echo "$my_ip" >> active_macs.txt
python whois.py
