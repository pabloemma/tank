'''
Created on Jan 29, 2018

@author: klein
this runs on the raspi with the sonic level meter
the sonic leve is a maxbot 
makre sure that this raspi has the serial login disabled, by going into
the raspi-config
also it is important which serial port to use.


If you do a dmesg | grep tty you will get something like:

[    0.000487] console [tty1] enabled
[    0.276024] 3f215040.uart: ttyS0 at MMIO 0x3f215040 (irq = 59, base_baud = 31250000) is a 16550
[    0.832827] 3f201000.uart: ttyAMA0 at MMIO 0x3f201000 (irq = 87, base_baud = 0) is a PL011 rev2

I tried first ttyAMA0 in my case, but the one which worked was ttyS0; this is on a 
debian stretch version

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
        print " we are using ",device
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
    	#print "in measure"
        x=self.ser.readline()
	
	# since we only want to send one value every so often
	#we always send the first in the buffer, a level word is 6 bytes long including
	# a carraige return, so we only send the first 5 bytes. However stripping the 0 byte
	# also ensures that we can easily convert the measurement into an integer
        
        time.sleep(10)
	   
        return x[1:5] 
	

 
if __name__ == '__main__':
    #device_name = '/dev/ttyAMA0'
    device_name = '/dev/ttyS0'
    lev = MyLevel(device_name)
    lev.InitFirst()
    while 1:
    	print lev.Measure()

        
