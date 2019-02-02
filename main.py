"""
Group 24
DP-3
Preliminary Python Program
Main Program File
"""
#imports
import math
import os.path
import time
#from gpiozero import LED
#import therm_control
#from gpiozero import Button
from data_class import Data
import heart_rate_control

#notes:
''' Add double confirmation and user input to choose
whether to the patient wants to use each sensor or not. So the
patient can still run code if one or more sensors are not available.'''

#file names:
save_path = r'C:\Users\liamw\OneDrive\McMasterUniversity\IBEHS 1P10\IBioMed Projects\DP-3\code\VSC_DP3'
name_of_file1 = "tempFile"
name_of_file2 = "gsrFile"
name_of_file3 = "heartFile"
complete_name1 = os.path.join(save_path, name_of_file1+".txt")
complete_name2 = os.path.join(save_path, name_of_file2+".txt")
complete_name3 = os.path.join(save_path, name_of_file3+".txt")

#variables cretaing the data object
init_temp1 = 34
init_temp2 = 34
init_gsr = 30 #need to modify
init_heart = 70

    
def file_creation(): #creates files containing sensor data
    
    file1 = open(complete_name1, "w+")
    file1.close()

    file2 = open(complete_name2, "w+")
    file2.close()

    file3 = open(complete_name3, "w+")
    file3.close()
    
def temp_analysis(sensor_data):
    #comparing temp
    compared_temp = []
    temp1 = sensor_data.get_temp1()
    temp2 = sensor_data.get_temp2()
    diff = abs(temp1-temp2)
    compared_temp.append(temp1)
    compared_temp.append(temp2)
    if diff > 2.0: #open to change
        temp_write(diff)
        difference = diff
    else:
        difference = None
    return difference

#temp writing function
def temp_write(temp_difference):
    temp_difference = str(temp_difference)
    file = open(complete_name1, "a")
    file.write(temp_difference)
    file.write(" ")
    file.close()
    fileread = open("tempFile.txt", "r")
    x1 = fileread.readlines()
    fileread.close()
    return x1

#gsr analysis function
def gsr_analysis(sensor_data):
    gsr_compared_data = []
    gsr_data = sensor_data.get_gsr()
    gsr_compared_data.append(gsr_data)
    if gsr_data > 20: #will have to adjust value accordingly
        gsr_write(gsr_data)
        gsr_data_bad = gsr_data
    else:
        gsr_data_bad = None
    return gsr_data_bad

#gsr writing function
def gsr_write(gsr_data):
    gsr_data = str(gsr_data)
    file = open("gsrFile.txt", "a")
    file.write(gsr_data)
    file.write(" ")
    file.close()
    fileread = open("gsrFile.txt", "r")
    x2 = fileread.readlines()
    fileread.close()
    return x2

#heart analysis function
def heart_analysis(sensor_data):
    hbeat_list = []
    hbeat = sensor_data.get_heart()
    hbeat_list.append(hbeat)
    if hbeat < 50 or hbeat > 140: #will have to test different thresholds
        heart_write(hbeat)
        hbeat_bad = hbeat
    else:
        hbeat_bad = None
    return hbeat_bad

#heart write function
def heart_write(heart_data):
    heart_data = str(heart_data)
    file = open("heartFile.txt", "a")
    file.write(heart_data)
    file.write(" ")
    file.close()
    fileread = open("heartFile.txt", "r")
    x3 = fileread.readlines()
    fileread.close()
    return x3
    
def main():
    time_value = 0.3
    file_creation()
    pin_num = input("Enter the button pin number: ") #computing prototype purposes only
    print("Only for physical computing type purposes ^^") #remove later
    print(" ")
    #Button_Creation(pin_num)
    init_data = Data(init_temp1, init_temp2, init_gsr, init_heart)
    x = 30
    xx = 50
    y = 26
    z = 60
    while True:
        #all values below will be read form sensors to creat a new class object
        """s_temp1 = temp1.read()
        s_temp2 = temp2.read()
        s_gsr = GSR.read()
        s_hbeat = PHOTORESIST.read()"""
        #values meant for testing code:
        s_temp1 = x
        s_temp2 = xx
        s_gsr = y
        s_hbeat = z #info will come from heart_rate_control.py
        
        new_sensor_data = Data(s_temp1, s_temp2, s_gsr, s_hbeat)
        temp_warning = temp_analysis(new_sensor_data)
        gsr_warning = gsr_analysis(new_sensor_data)
        heart_warning = heart_analysis(new_sensor_data)
        
        #printing data if it meets warning thresholds:
        if temp_warning and gsr_warning and heart_warning != type(None): #comparing results from sensors
            print("You may be experiencing an episode of autonomic dysreflexia")
            time.sleep(time_value)
            print("Please notify a physician or caretaker immediately")
            time.sleep(time_value)
            print("Remove tight clothing, sit upright, & empty your bladder if possible")
            time.sleep(time_value)
            avg = (new_sensor_data.get_temp1() + new_sensor_data.get_temp2())/2
            print("Your current approximate skin temperature is: ", avg, "degrees C")
            time.sleep(time_value)
            print("Your current heartrate is approximately: ", new_sensor_data.get_heart(), "BPM")
            time.sleep(time_value)
            print("You current GSR reading is approximately: ", new_sensor_data.get_gsr())
            time.sleep(time_value)
            print("To accept this information, press the button.")
            input() #simulation of pressing button
        else:
            #printing measured data, regardless of value:
            avg_temp = (new_sensor_data.get_temp1()+new_sensor_data.get_temp2()/2)
            current_heart = new_sensor_data.get_heart()
            current_gsr = new_sensor_data.get_gsr()
            print("Your current temperature is: ", avg_temp, "C")
            time.sleep(time_value)
            print("your current heart rate is: ", current_heart, "BPM")
            time.sleep(time_value)
            print("Your current GSR reading is: ", current_gsr) #must add GSr unit - not sure atm
            print(" ")
            time.sleep(3.5)
 
            
        x += 0.5 #simulated changes in sensor readings
        y -= 1 #^^
        z += 5 #^^
        '''button.wait_for_press #not sure if necessary - will need to keep collecting data
        print("The device will continue collecting data.")'''
        time.sleep(0.3)

if __name__ == "__main__":
    main()
        
        
    
            
