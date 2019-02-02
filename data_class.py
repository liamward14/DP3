"""
Team 24
DP3
Sensor Data Class
"""
#imports
#none
class Data(object):

    def __init__(self, temp1, temp2, gsr, heart):
        self._temp1 = temp1
        self._temp2 = temp2
        self._gsr = gsr
        self._heart = heart

    #accessors
    def get_temp1(self):
        return self._temp1

    def get_temp2(self):
        return self._temp2

    def get_gsr(self):
        return self._gsr
    
    def get_heart(self):
        return self._heart

    #mutators
    def set_temp1(self, temp1_read):
        self._temp1 = temp1_read
        return self._temp1

    def set_temp2(self, temp2_read):
        self._temp2 = temp2_read
        return self._temp2

    def set_gsr(self, gsr_read):
        self._gsr = gsr_read
        return self._gsr

    def set_heart(self, heart_read):
        self._heart = heart_read
        return self._heart

    def __str__(self):
        string1 = ("Temperature 1 is: ", self._temp1, "C")
        string2 = ("Temperature 2 is: ", self._temp2, "C")
        string3 = ("GSR Data indicates: ", self._gsr) #will have to add units
        string4 = ("Heart Rate is: ", self._heart, "BPM")
    
    
