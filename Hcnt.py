## Hcnt.py - H control v1.0
# -*- coding: utf-8 -*-
##

import os, sys, time, RPi.GPIO as GPIO

###########################################################################

# ---colors---

colors = {
        'W' : '\033[0m',  # white (normal)
        'R' : '\033[31m', # red
        'G' : '\033[32m', # green
        'O' : '\033[33m', # orange
        'B' : '\033[34m', # blue
        'P' : '\033[35m', # purple
        'C' : '\033[36m', # cyan
        'GR': '\033[37m', # gray
        'D' : '\033[2m'   # dims current color. {W} resets.
    }

# ---banner---

spase = """
    {D}                 <>______________________
    {D}   .-^^^-.       || \|/ {R}@@@@{W};;;;;;;;;;;;{D}|
    {D}  /= ___  \      || /j \{R}@@@@{W};;;;;;;;;;;;{D}|
    {D} |- /~~~\  |     ||{R}@@@@@@@@@@@@@@@@@@@@@{D}|
   {D}  |=( '.' ) |     ||{R}@@@@@@@@@@@@@@@@@@@@@{D}|
   {D}  \__\_=_/__/     ||{R}@@@@@@@@{G}:::::::::::::{D}|
  {D}    {_______}      ||{R}@@@@@@@@{G}:::::::::::::{D}|
   {D} /` *       `'--._||~~~~~~~~~~~~~~~~~~~~~~
  {D} /= .     [] .     { >
 {D} /  /|ooo     |`'--'|| 
 {D}(   )\_______/      ||
 {D}\``\/       \      ||
  {D} `-| ==    \_|     ||
  {D}   /         |     ||
  {D}  |=   >\  __/     ||
 {D}   \   \ |- --|     ||
   {D}  \ __| \___/     ||
    {D} _{__} _{__}     ||
   {D} (....)(....)     ||
{D}^^~^^^~^^~~~^^^~^^^~^^^~^^~^^~~~^^~^^^~^^^~
"""

LED = """
  ..---..
 /       \
|         |
:         ;
 \  \~/  /
  `, Y ,'
   |_|_|
   |===|
   |===|
    \_/
"""

bacbn = """
   {G}[99] Back to main menu
   {G}[00] Exit the H control
"""

resban = """
   {G}[88] Restart system
   {G}[99] Back to main menu
   {G}[00] Exit the H control
"""

# ---function---

def res_p():
	os.system('reset')
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
        os.system('reset')
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
    os.system('reset')
    os.system('watch vcgencmd measure_temp')
    bac_mn()

def Update_System():
    os.system('reset')
    os.system('sudo rpi-update')
    os.system('sudo apt-get update && upgrade -y')
    os.system('echo " you need to reboot your system" |lolcat')
    time.sleep(3)
    res_mn()

def Netstat():
    os.system('reset')
    os.system('sudo netstat |lolcat')
    bac_mn()

def Ifconfig():
    os.system('reset')
    os.system('sudo ifconfig |lolcat')
    bac_mn()

def Htop():
    os.system('reset')
    os.system('sudo htop')
    bac_mn()

def Midnight_Commander():
    os.system('reset')
    os.system('mc')
    bac_mn()

def Matrix():
    os.system('reset')
    os.system('cmatrix')
    bac_mn()

def Config():
    os.system('reset')
    os.system('sudo raspi-config')
    bac_mn()

def Calender():
    os.system('reset')
    os.system('cal')
    bac_mn()

def Set_password():
    os.system('reset')
    os.system('sudo chpasswd root')
    bac_mn()

def About():
    os.system('reset')
    os.system('figlet H control | lolcat')
    os.system('echo ""')
    os.system('echo "     V1.2"|lolcat')
    print spase
    os.system('echo ""')
    os.system('echo ""')
    os.system('echo " Hi iam Hamood"|lolcat')
    os.system('echo " Instagram:q2_jz"|lolcat')
    os.system('echo " Facebook:Hamood Hamood"|lolcat')
    os.system('echo " githup: hamood9172h"|lolcat')
    bac_mn()

def Info():
    os.system('reset')
    os.system('neofetch')
    bac_mn()

def CPU_inf():
	os.system('reset')
	os.system('cat /proc/cpuinfo|lolcat')
	bac_mn()

def memore():
	os.system('reset')
	os.system('cat /proc/meminfo|lolcat')
	bac_mn()

def disk_usg():
	os.system('reset')
	os.system('df -h|lolcat')
	bac_mn()

def kernel():
	os.system('reset')
	os.system('uname -a|lolcat')
	bac_mn()

def linuxv():
	os.system('reset')
	os.system('cat /proc/version|lolcat')
	bac_mn()

###########################################################################

# ---GPIO---

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#########################

#01
GPIO.setup(12,GPIO.OUT)
#02
GPIO.setup(18,GPIO.OUT)
#03
GPIO.setup(32,GPIO.OUT)
#04
GPIO.setup(38,GPIO.OUT)
#05
GPIO.setup(37,GPIO.OUT)
#06
GPIO.setup(29,GPIO.OUT)
####################

# ---show_function---

#######1
def on1():
     GPIO.output(12,1)

def of1():
    GPIO.output(12,0)
#######2
def on2():
    GPIO.output(18,1)
    
def of2():
    GPIO.output(18,0)
#######3
def on3():
    GPIO.output(32,1)

def of3():
    GPIO.output(32,0)
#######4
def on4():
    GPIO.output(38,1)

def of4():
    GPIO.output(38,0)
#######5
def on5():
    GPIO.output(37,1)

def of5():
    GPIO.output(37,0)
#######6
def on6():
    GPIO.output(29,1)

def of6():
    GPIO.output(29,0)

###############################

def onall():
    GPIO.output(12,1)
    GPIO.output(18,1)
    GPIO.output(32,1)
    GPIO.output(38,1)
    GPIO.output(37,1)
    GPIO.output(29,1)

def ofall():
    GPIO.output(12,0)
    GPIO.output(18,0)
    GPIO.output(32,0)
    GPIO.output(38,0)
    GPIO.output(37,0)
    GPIO.output(29,0)

def lo():
    on1()
    sp()
    of1()
    on2()
    sp()
    of2()
    on3()
    sp()
    of3()
    on4()
    sp()
    of4()
    on5()
    sp()
    of5()
    on6()
    sp()
    of6()

def ol():
    on6()
    sp()
    of6()
    on5()
    sp()
    of5()
    on4()
    sp()
    of4()
    on3()
    sp()
    of3()
    on2()
    sp()
    of2()
    on1()
    sp()
    of1()

def cake():
	on1()
    sp()
    of1()
    on2()
    sp()
    of2()
    on3()
    sp()
    of3()
    on4()
    sp()
    of4()
    on5()
    sp()
    of5()
    on6() #06
    
    sp()

    on1()
    sp()
    of1()
    on2()
    sp()
    of2()
    on3()
    sp()
    of3()
    on4()
    sp()
    of4()
    on5() #05
    
    sp()
	
	on1()
    sp()
    of1()
    on2()
    sp()
    of2()
    on3()
    sp()
    of3()
    on4() #04
   
    sp()
	
	on1()
    sp()
    of1()
    on2()
    sp()
    of2()
    on3() #03
    
    sp()
	
	on1()
    sp()
    of1()
    on2() #02
    
    sp()
	
	on1() #01

def ekac():
	on6()
    sp()
    of6()
    on5()
    sp()
    of5()
    on4()
    sp()
    of4()
    on3()
    sp()
    of3()
    on2()
    sp()
    of2()
    on1() #01
    
    sp()
	
	on6()
    sp()
    of6()
    on5()
    sp()
    of5()
    on4()
    sp()
    of4()
    on3()
    sp()
    of3()
    on2() #02
    
    sp()
	
	on6()
    sp()
    of6()
    on5()
    sp()
    of5()
    on4()
    sp()
    of4()
    on3() #03
    
    sp()
	
	on6()
    sp()
    of6()
    on5()
    sp()
    of5()
    on4() #04

    sp()

	on6()
    sp()
    of6()
    on5() #05
    
    sp()
	
	on6() #05

# ---sleep---

def sp():
    time.sleep(2)

def sp5():
	time.sleep(5)

# ---show---

def rgb():
    while True:
        ofall()
        sp()
        on1()
        sp()
        on2()
        sp()
        on3()
        sp()
        on4()
        sp()
        on5()
        sp()
        on6()
        sp()
        sp()
        sp()
        ofall()
        sp()
        on4()
        on1()
        sp()
        onall()
        sp()
        sp()
        ofall()
        lo()
        ol()
        lo()
        ol()
        lo()
        ol()
        onall()
        sp()
        sp()
        sp()
        sp()
        sp()
        cake()
        sp()
        sp()
        ofall()
        sp()
        ekac()
        sp()
        sp()
        onall()
        ofall()
        onall()
        ofall()
        onall()
        sp5()

###########################################################################

os.system('reset')
os.system('figlet H control | lolcat')
os.system('echo ""')
os.system('echo "     V1.2                By Hamood Alsalmani"|lolcat')
os.system('echo ""')
os.system('echo ""')
os.system('echo "  [01] RGB           [02] BCM Temperature" |lolcat')
os.system('echo "  [03] Update        [04] Netstat" |lolcat')
os.system('echo "  [05] Calender      [06] Ifconfig" |lolcat')
os.system('echo "  [07] Htop          [08] Midnight Commander" |lolcat')
os.system('echo "  [09] Matrix        [10] Info" |lolcat')
os.system('echo "  [11] Set password  [12] Config" |lolcat')
os.system('echo "  [13] CPU Info      [14] RAM" |lolcat')
os.system('echo "  [15] Disk usage    [16] kernel Version" |lolcat')
os.system('echo "  [17] Uptime        [18] Linux version" |lolcat')
os.system('echo "  [00] About         [99] Exit" |lolcat')
os.system('echo ""')
os.system('echo ""')
hmin = raw_input("{G}Hcon >")
if hmin == "1" or hmin == "01":
    os.system('reset')
    os.system('figlet RGB| lolcat')
    os.system('echo " [01] On    [02] Off" |lolcat')
    rgbin= raw_input("Hcon >")
    if rgbin == "1" or rgbin == "01":
        rgb()
        bac_mn()
    elif rgbin == "2" or rgbin == "02":
        ofall()
        bac_mn()
    else:
        os.system('echo "ERROR"')
        time.sleep(2)
        res_p()
elif hmin == "2" or hmin == "02":
    BCM_Temperature()
elif hmin == "3" or hmin == "03":
    Update_System()
elif hmin == "4" or hmin == "04":
    Netstat()
elif hmin == "5" or hmin == "05":
    Calender()
elif hmin == "6" or hmin == "06":
    Ifconfig()
elif hmin == "7" or hmin == "07":
    Htop()
elif hmin == "8" or hmin == "08":
    Midnight_Commander()
elif hmin == "9" or hmin == "09":
    Matrix()
elif hmin == "10":
    Info()
elif hmin == "11":
    Set_password()
elif hmin == "12":
    Config()
elif hmin == "13":
	CPU_inf()
elif hmin == "14":
	memore()
elif hmin == "15":
	disk_usg()
elif hmin == "16":
	kernel()
elif hmin == "17":
	uptime()
elif hmin == "18":
	linuxv()
elif hmin == "00":
    About()
elif hmin == "99":
    os.system('reset')
    os.system('echo " {G}Good bye" |lolcat')
    time.sleep(3)
    os.system('reset')
    sys.exit()
else:
    os.system('reset')
    print "\nError: Wrong Input"
    time.sleep(2)
    res_p()
