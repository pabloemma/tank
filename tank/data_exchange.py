'''
Created on Jan 28, 2018

@author: klein
'''
import socket
import sys

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Stripper


from multiprocessing.connection import Client


class Exchange(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.fig, self.ax = plt.subplots()
        self.scope = Stripper.Stripper(self.ax)
        
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
                #print "this is the receiver and I got",data, len(data)
                print data , " mm"
                if(len(data)==4):
                    fl_data = int(data)
                else:
                    fl_data = 1
            conn.send('thanks from server')
                #self.scope.emitter(int(data))
            #conn.close()
            ani = animation.FuncAnimation(self.fig, self.scope.update, fl_data, interval=100,
                              blit=True)
            plt.show()
    def CloseAll(self):
        self.mysock.close()
        print ' going away'
        sys.exit(0)
        
    def MakeHisto(self,title):
        
        # myhisto = ROOT.TH1I
        pass
    
            
if __name__ == '__main__':
    tel =Exchange()
    tel.Establish()
    tel.Looping()
    tel.CloseAll()
    