'''
Created on Jan 29, 2018
will push the tank data
needs to run on raspberry

@author: klein
'''

import socket
import sys
from multiprocessing.connection import Client
class Push(object):
    '''
    classdocs
    '''


    def __init__(self,ip_server,server_port):
        '''
        Constructor
        '''
        self.tank_server = ip_server # connect with ip of server
        self.tank_port = server_port
	print "tank server", self.tank_server,"on port ", self.tank_port
    
    def Connect2Server(self):
        '''
        this establisk the socket connection with the server
        '''
        self.mysocket = socket.socket()  #use default protocol and stream
        # now connect to the server
    print "Esatablishing connection"
        self.mysocket.connect((self.tank_server,self.tank_port))
    def PushData(self,databuffer): 
        '''
        pushes data to server
        '''
        # make sure we know that we transmitted all the bytes
        temp=len(databuffer.encode('utf-8')) # length in bytes of databuffer, whih needs to be a string
        bytes_sent =self.mysocket.send(databuffer) # returns number of bytes sent
        if(temp - bytes_sent != 0):
            print "got ",temp," bytes  but sent ",bytes_sent,"  bytes"
        # get ack back from server
        #response = self.mysocket.recv(1024)
        #print response 
        
        
           
    def CloseConnection(self):  
        '''
        closes all connections
        '''
        self.mysocket.close()
         
if __name__ == '__main__':
    ip_server = '192.168.2.9' # change for apporpitae server
    server_port = 5478
    
    MyPush = Push(ip_server,server_port)
    MyPush.Connect2Server()
    MyPush.PushData('R0430')
    MyPush.CloseConnection()
