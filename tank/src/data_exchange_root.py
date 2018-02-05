'''
Created on Jan 28, 2018

@author: klein
'''
import socket
import sys
import time

import ROOT as RO
from array import  array
from multiprocessing.connection import Client


class ExchangeRoot(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # set up ROOT system
        tanktree = RO.TTree("tanktr","level measurement")
        
        
        
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


        print int(time.time()) # strip frac seconds
        print "got connection form ",addr

        while True:
            # wait for data
            data = conn.recv(1024)
            #if not data: break
            if (len(data)>0): 
                #print "this is the receiver and I got",data, len(data)
                print int(time.time()) ,"   ",data , " mm"
                
                if(len(data)==4):
                    fl_data = int(data)
                else:
                    fl_data = 1
            conn.send('thanks from server')
                #self.scope.emitter(int(data))
            #conn.close()
    def CloseAll(self):
        self.mysock.close()
        print ' going away'
        sys.exit(0)
        
    def MakeHisto(self,title):
        
        # myhisto = ROOT.TH1I
        pass
    
            
if __name__ == '__main__':
    tel =ExchangeRoot()
    tel.Establish()
    tel.Looping()
    tel.CloseAll()
   