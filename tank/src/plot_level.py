import matplotlib.pyplot as plt
import matplotlib.dates as md
import csv
import time
import sys
import datetime as dt
import numpy as np
#from scipy.special._mptestutils import Arg

# check for arguments
for arg in sys.argv[1:]:
    print arg
    if (arg == 'today'):
        date_string=dt.datetime.today().strftime('%Y-%m-%d')
    elif("-" in arg): date_string = arg
        
    else:
        date_string ='2018-10-01'
x1 = []
y1 = []
x2 = []
y2 =[]

# for date plotting
n=20  
duration =1000
filename = '/home/klein/tankfiles/'+date_string+'tank.csv'
with open(filename,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if(int(row[1]) == 61):
        	x1.append(int(row[0]))
        	y1.append(int(row[2]))
	elif(int(row[1]) == 60):
        	x2.append(int(row[0]))
        	y2.append(int(row[2]))
	else:
		print "Invalid control, wrong IP \n" 

#plt.plot(x1,y1, label='Loaded from file!')

#plt.plot(x2,y2,"r.") # plot with red points

#plt.figure(1)
#plt.plot(x1,y1,'g^',x2,y2,'r.')
#plt.xlabel('unix time')
#plt.ylabel('tank level')
#plt.title('Plot of tanklevels ')
#plt.legend()
#plt.show()


# now do second way of plotting
plt.figure(2)

time_date1 = [dt.datetime.fromtimestamp(ts) for ts in x1]
time_date2 = [dt.datetime.fromtimestamp(ts) for ts in x2]

time_convert1 = md.date2num(time_date1)
time_convert2 = md.date2num(time_date2)
#print time_date


plt.subplot(211)
plt.xticks(rotation = 25)
ax=plt.gca()
#xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
xfmt = md.DateFormatter(' %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
ax.xaxis_date()
#plt.gcf().autofmt_xdate()

#plt.locator_params(axis='x',nbins =5)
plt.grid(True)

plt.plot(time_date1,y1, 'g^',label='Loaded from file!')

plt.subplot(212)

# note these adjustments have to happen within the respective figure part
plt.subplots_adjust(bottom = .1)
plt.xticks(rotation = 25)
ax=plt.gca()
#xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
xfmt = md.DateFormatter(' %H:%M:%S')
ax.xaxis.set_major_formatter(xfmt)
ax.xaxis_date()
#plt.gcf().autofmt_xdate()

#plt.locator_params(axis='x',nbins =5)
plt.plot(time_date2,y2,"r.") # plot with red points
plt.grid(True)
plt.subplots_adjust(hspace=.3)
plt.show()

