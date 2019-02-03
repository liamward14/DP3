"""
Liam Ward
Team 24
DP3
Heart Rate Sample File
"""
#imports
import math
import time
from data_class import Data
from multiprocessing import Process
#from gpiozero import LED

#LED control function one
def LED1(pin_num1):
    #led_colour1 = LED(pin_num1)
    while True:
        led_colour1.on()
        time.sleep(0.05)
        led_colour1.off()
        time.sleep(0.05)
        

 #LEd control fucntion two       
def LED2(pin_num2):
    #led_colour2 = LED(pin_num2)
    while True:
        led_colour2.on()
        time.sleep(0.05)
        led_colour2.off()
        time.sleep(0.05)
    

def main():
    first_led = input("Enter the first pin location: ") #for physical computing purposes only
    second_led = input("Enter the second pin location: ") #for physical computing purposes only
    p1 = Process(target = LED1)
    p1.start()
    p2 = Process(target = LED2)
    p2.start()
    


if __name__ == "__main__":
    main()
        


