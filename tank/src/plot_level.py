import matplotlib.pyplot as plt
import matplotlib.dates as md
import csv
import time
import sys
import datetime
#from scipy.special._mptestutils import Arg

# check for arguments
for arg in sys.argv[1:]:
    print arg
    if (arg == 'today'):
        date_string=datetime.datetime.today().strftime('%Y-%m-%d')
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

plt.plot(x1,y1, label='Loaded from file!')

plt.plot(x2,y2,"r-")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
