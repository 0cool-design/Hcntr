import RPi.GPIO as GPIO, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

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
    GPIO.output(38,1)

def of3():
    GPIO.output(38,0)
#######4
def on4():
    GPIO.output(36,1)

def of4():
    GPIO.output(36,0)
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
#######################
def onall():
    GPIO.output(12,1)
    GPIO.output(18,1)
    GPIO.output(38,1)
    GPIO.output(36,1)
    GPIO.output(37,1)
    GPIO.output(29,1)

def ofall():
    GPIO.output(12,0)
    GPIO.output(18,0)
    GPIO.output(38,0)
    GPIO.output(36,0)
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
#######################
def sp():
    time.sleep(2)
#####################
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
