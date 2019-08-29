# -*- encoding: utf-8 -*-
import psutil
import csv
import time
from datetime import datetime

def getPidByName(Str):
    pids = psutil.process_iter()
    pidList = []
    for pid in pids:
        if pid.name() == Str:
            pidList.append(pid.pid)
    #print(pidList)
    return pidList


def getMemByPid(pid):
    PID = psutil.Process(pid)
    memory = float(PID.memory_info().rss/1024/1024)
    real_mem = memory
    return float(real_mem)

'''
def getMemByPid(pid, sampleNum):
    PID = psutil.Process(pid)
    memoryList = []    
    for i in range(0, sampleNum):
        memory = PID.memory_info().rss/1024/1024
        memoryList.append(memory.rss/1024/1024)
        time.sleep(2)
        #print(memoryList)
    return memoryList
'''

def returnTime():
    startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return startTime

def save_to_txt(PID_Number):
    f = open('memory.txt','a+')
 #   f.write("当前时间：%s PID-%s UIH.ClientProxy.Service.exe 当前内存：%dM（工作集）\r\n"  % (returnTime(),PID_Number,getMemByPid(PID_Number)))
    f.write("%s PID%s %dM\r\n"  % (returnTime(),PID_Number,getMemByPid(PID_Number)))
    f.close()

def main(data):
    datetime_from_db='2019-08-15 19:50:00'
    datetime_of_datetime_from_db=datetime.strptime(datetime_from_db,'%Y-%m-%d %H:%M:%S')
    data=getPidByName('UIH.ClientProxy.Service.exe')
    while True:
        delta_time=datetime.now()-datetime_of_datetime_from_db
        if delta_time.days<0:
            for i in data:
                save_to_txt(i)
            time.sleep(2)
        else:
            print('到达指定时刻，停止记录内存')
            break



data=getPidByName('UIH.ClientProxy.Service.exe')
main(data)         
