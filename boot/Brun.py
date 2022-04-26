import RPi.GPIO as GPIO, sys, os, time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.IN)
#01
GPIO.setup(12,GPIO.OUT)
#02
GPIO.setup(18,GPIO.OUT)
#03
GPIO.setup(38,GPIO.OUT)
#04
GPIO.setup(36,GPIO.OUT)
#05
GPIO.setup(37,GPIO.OUT)
#06
GPIO.setup(29,GPIO.OUT)
####################
def ofall():
    GPIO.output(12,0)
    GPIO.output(18,0)
    GPIO.output(38,0)
    GPIO.output(36,0)
    GPIO.output(37,0)
    GPIO.output(29,0)
    
while True:
    if(GPIO.input(7) == False):
        ofall()
        os.system('cd')
        os.system('sudo python Desktop/Hcnt/Hcnt.py')
        time.sleep(5)