#!/usr/bin/env python
#import PCF8591_3 as ADC
#import RPi.GPIO as GPIO
import time
import math

DO = 17 #will have to change pin num
#GPIO.setmode(GPIO.BCM)

#def setup():
	#ADC.setup(0x48)
	#GPIO.setup(DO, GPIO.IN)

def read():
    #while True:
        #analogVal = ADC.read(0)
        #Vr = 5 * float(analogVal) / 255
        #Rt = 10000 * Vr / (5 - Vr)
        #temp = 1/(((math.log(Rt / 10000)) / 3950) + (1 / (273.15+25)))
        #temp = temp - 273.15
        #temp = 30 # test value
    temp = 25
    return temp

def main():
    read()
if __name__ == '__main__':
    main()
    #setup()

	
