




import sys
import time
import os
import datetime

import matplotlib.pyplot as plt
import csv





class plot_tank_level(object):
    """ main plot class"""
    
    def __init__(self, filedate):
        
        """"
        filedate is the date we want to look at for the level
        """
        print int(time.time()) # strip frac seconds
        print "starting up the tank server on port" ,self.port
        print "**********************************\n\n"
        print " to stop program, press Ctrl/c \n\n"
        print "**********************************\n\n"
        self.x = 0
        self.y = 0
        self.z = 0
        self.filedate = filedate


        def ReadFile(self):
            
            
            a = datetime.datetime.today().strftime('%Y-%m-%d')
            filename = a+'tank.csv'
            # if filename exists we open in append mode
            #otherwise we will create it
            homedir = os.environ['HOME']
            filename = homedir + '/tankfiles/'+filename
            print filename
            if os.path.isfile(filename):
                self.input = open(filename,'r',0)
            else :
                print "cannot find file"
                sys.exit()

            
            with open('/home/klein/tankfiles/2018-07-13tank.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter=',')
                for row in plots:
                    self.x.append(int(row[0]))
                    self.y.append(int(row[1]))
                    self.z.append(int(row[2]))
                    
    def PlotLevel(self):
        plt.plot(self.x,self.z, label='levels in tank')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Irrigation System')
        plt.legend()
        plt.show()
