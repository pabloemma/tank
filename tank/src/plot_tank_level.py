




import sys
import time
import os
import datetime





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


        def ReadFile(self):
            with open('/home/klein/tankfiles/2018-07-13tank.csv','r') as csvfile:
                plots = csv.reader(csvfile, delimiter=',')
                for row in plots:
                    x.append(int(row[0]))
                    y.append(int(row[1]))
                    z.append(int(row[1]))
