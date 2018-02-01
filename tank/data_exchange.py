'''
Created on Jan 28, 2018

@author: klein
'''
import socket
import sys
from multiprocessing.connection import Client
class Exchange(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def Establish(self):
        '''
        establish connection with Client
        for us that should be 192.168.2.22
        '''
        self.mysock = socket.socket() # create socket
        myip = '192.168.2.22'
        myport = 5478
        self.mysock.bind(('',myport))
        self.mysock.listen(5) # start listening
        
    def Looping(self):
        '''
        Here we listen for the Client
        '''
        conn,addr = self.mysock.accept() # connection address pair
        print "got connection form ",addr

        while True:
            # wait for data
            data = conn.recv(1024)
            #if not data: break
            if (len(data)>0): 
                print "this is the receiver and I got",data, len(data)
                conn.send('thanks from server')
            #conn.close()
            
    def CloseAll(self):
        self.mysock.close()
        print ' going away'
        sys.exit(0)
            
if __name__ == '__main__':
    tel =Exchange()
    tel.Establish()
    tel.Looping()
    tel.CloseAll()
    