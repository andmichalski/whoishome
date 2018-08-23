#!/bin/sh

while : 
do
	sudo nmap -n -sP 192.168.1.1/24 | awk '/Nmap scan report for /{printf $5x;printf " ";getline;getline;print $3x}' > active_macs.txt
	echo "$(hostname -I)$(ip a  | grep -A 1 wlo1: | awk '/link/{printf $2x}')" >> active_macs.txt
	clear
	python whois.py 
done
