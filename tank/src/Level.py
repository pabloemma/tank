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
        print device
        self.ser = serial.Serial(
            port = device,
            baudrate = 9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0)

        counter=0
    def InitFirst(self):
    	x=self.ser.readline()
	
    def Measure(self):
    	
        x=self.ser.readline()
	
	# since we only want to send one value every so often
	#we always send the first in the buffer, a level word is 6 bytes long including
	# a carraige return, so we only send the first 5 bytes. However stripping the 0 byte
	# also ensures that we can easily convert the measurement into an integer
        
	time.sleep(5)
	
        return x[1:5] 

 
if __name__ == '__main__':
    device_name = '/dev/ttyAMA0'
    lev = MyLevel(device_name)
    lev.InitFirst()
    while 1:
    	lev.Measure()

        
