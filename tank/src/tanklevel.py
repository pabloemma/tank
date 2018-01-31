'''
Created on Jan 30, 2018

@author: klein
'''
import Level as Lv
import data_push as dp
if __name__ == '__main__':
    #establish connection
    ip_server = '192.168.2.9' # change for apporpitae server
    server_port = 5478
    # serial connection device
    device_name = '/dev/ttyAMA0'

    
    MyPush = dp.Push(ip_server,server_port)
    MyPush.Connect2Server()
    # now open up the serial port
    lev = Lv.MyLevel(device_name)

    data = lev.Measure()

    MyPush.PushData(data)
    data = lev.Measure()

    MyPush.PushData(data)
    data = lev.Measure()

    MyPush.PushData(data)
    
    MyPush.CloseConnection()    
    
    
    
