## Hcnt.py - useful module of H control
# -*- coding: utf-8 -*-

import os, sys, time, RPi.GPIO as GPIO

# ---colors---

H = '\033[95m'
B = '\033[94m'
W = '\033[93m'
G = '\033[92m'
F = '\033[91m'
O = '\033[33m'
U = '\033[4m'
E = '\033[0m'
bacbn = """
   [99] Back to main menu
   [00] Exit the H control
"""
resban = """
   [88] Restart system
   [99] Back to main menu
   [00] Exit the H control
"""

def res_p():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()

def bac_mn():
    print bacbn
    baco = raw_input("Hcon >")
    if baco == "99":
        res_p()
    elif baco == "00":
        sys.exit()
    else:
        print "\nError: Wrong Input"
        time.sleep(2)
        res_p()

def res_mn():
    print resban
    reso = raw_input("Hcnt >")
    if reso == "88":
        os.system('sudo reboot')
    elif reso == "99":
        res_p()
    elif reso == "00":
        sys.exit()
    else:
        print "\nError: Wrong Input"
        time.sleep(2)
        res_p()

def BCM_Temperature():
    os.system('clear')
    os.system('watch vcgencmd measure_temp')
    bac_mn()

def Update_System():
    os.system('clear')
    os.system('sudo rpi-update')
    os.system('sudo apt-get update && upgrade -y')
    os.system('echo " you need to reboot your system" |lolcat')
    time.sleep(3)
    res_mn()

def Netstat():
    os.system('clear')
    os.system('sudo netstat |lolcat')
    bac_mn()

def Ifconfig():
    os.system('clear')
    os.system('sudo ifconfig |lolcat')
    bac_mn()

def Htop():
    os.system('clear')
    os.system('sudo htop')
    bac_mn()

def Midnight_Commander():
    os.system('clear')
    os.system('mc')
    bac_mn()

def Matrix():
    os.system('clear')
    os.system('cmayrix')
    bac_mn()

def Config():
    os.system('clear')
    os.system('sudo raspi-config')
    bac_mn()

def Calender():
    os.system('clear')
    os.system('cal')
    bac_mn()

def Set_password():
    os.system('clear')
    os.system('sudo chpasswd root')
    bac_mn()

def About():
    os.system('clear')
    os.system('figlet H control | lolcat')
    os.system('echo ""')
    os.system('echo "     V1.0|lolcat"')
    os.system('echo " Hi iam Hamood|lolcat"')
    os.system('echo " Instagram:q2_jz|lolcat"')
    os.system('echo " Facebook:Hamood Hamood|lolcat"')
    os.system('echo " githup: hamood9172h|lolcat"')
    bac_mn()
def Info():
    os.system('clear')
    os.system('neofetch')
    bac_mn()


