'''
Created on Jan 29, 2018

@author: klein
'''
import time
import serial

class MyLevel(object):
    '''
    classdocs
    '''


    def __init__(self, device):
        '''
        Constructor
        '''
        self.ser = serial.Serial(
            port = device,
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)

        counter=0
    
    def Measure(self):
        x=self.ser.readline()
        time.sleep(1)
        return x 

 
if __name__ == '__main__':
    device_name = '/dev/ttyAMA0'
    lev = MyLevel(device_name)
    lev.Measure()
        