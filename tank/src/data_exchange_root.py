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
import KeyBoardPoller


# Collect events until released


class ExchangeRoot(object):
    '''
    classdocs
    '''


    def __init__(self,filename):
        '''
        Constructor
        '''
        # set up ROOT system
        tanktree = RO.TTree("tanktr","level measurement")
        self.OpenOutput(filename)
        
        
        
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
        print " to stop program, press Ctrl/y"




        while True:
            try:
            # wait for data
                data = conn.recv(1024)
            #if not data: break
                if (len(data)>0): 
                #print "this is the receiver and I got",data, len(data)
                    print int(time.time()) ,"   ",data , " mm"
                
                
                    if(len(data)==4):
                        fl_data = int(data)
                        myline = str(int(time.time()))+','+data +'\n'
                        print myline
                        self.output.write(myline)
                    else:
                        fl_data = 1
                    conn.send('thanks from server')
            except (KeyboardInterrupt, SystemExit):
                print "got interrupt"
                self.CloseAll()        
                #self.scope.emitter(int(data))
            #conn.close()
    def CloseAll(self):
        self.mysock.close()
        print ' going away'

        self.output.close() #close output file
        
        sys.exit(0)
        
    def OpenOutput(self,filename):
        '''
        open level file n
        '''
        try:
            self.output = open(filename,"a")
        except:
            print " problem with out put file"
            sys.exit(0)
            
# help wth keyboards
        
            
if __name__ == '__main__':
    tel =ExchangeRoot('test.csv')
    tel.Establish()
    tel.Looping()
    tel.CloseAll()
   