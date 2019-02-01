#!/usr/bin/env python
import PCF8591_3 as ADC
import RPi.GPIO as GPIO
import time

DO = 17
GPIO.setmode(GPIO.BCM)
list1 = []

def setup():
        ADC.setup(0x48)
        GPIO.setup(DO, GPIO.IN)


def loop():
        status = 1
        if ADC.read(0) != 0:
                while True:
                        print ('Value: ', ADC.read(0))
                        time.sleep(0.2)
        else:
                print("working")

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	
