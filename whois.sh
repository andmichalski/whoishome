#! /bin/sh

host_list=$(sudo nmap -n -sP 192.168.1.1/24 | awk '/Nmap scan report for /{printf $5x;printf " ";getline;getline;print 3x}')
echo "$host_list"
