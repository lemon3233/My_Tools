# -*- coding: utf-8 -*-
# 监控服务器性能，权利的游戏
import os
import datetime
import time
import psutil
import logging
import logging.handlers
import shutil


class setCPUInfo():

    def __init__(self):

        logPath = os.path.join(os.getcwd(), "severLog")
        if os.path.exists(logPath):
            shutil.rmtree(logPath)  # 将整个文件夹删除，清空文件夹功能

    #设置间隔时间
    #设置输出日志文本路径
    def newLogFile(self):
        #创建文件，命名方式为时间戳
        time = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        logPath = os.path.join(os.getcwd(), "severLog")
        if not os.path.exists(logPath):
            os.makedirs(logPath)
        logFile = os.path.join(logPath, "severLog" + time + ".txt")
        if not os.path.exists(logFile):
            f = open(logFile, 'w')
            f.close()
        return logFile

    #function of Get CPU State
    def getCPUstate(self):
        a = " CPU: " + str(psutil.cpu_percent()) + "%"
        return ("%-12s" %a)

    def getMemoryState(self):
        mem_rate = 0
        for pnum in psutil.pids():
            p = psutil.Process(pnum)
            mem_rate = mem_rate + p.memory_percent()
        return "%+8.2f%%" % mem_rate

    def getIOState(self):
        a = " Disk_IO: " + str(psutil.disk_io_counters(perdisk=False, nowrap=True))
        return a

    def getNetState(self):
        return (" Net_IO: " + str(psutil.net_io_counters(pernic=False)))

    def poll(self):
        """Retrieve raw stats within an interval window."""
        # get cpu state
        cpu_state = self.getCPUstate()
        # get memory
        memory_state = self.getMemoryState()
        # get DiskIO
        DiskIO_State = self.getIOState()
        # get NetIO
        NetIO_State = self.getNetState()
        #间隔时间
        time.sleep(2)
        return (cpu_state, memory_state, DiskIO_State, NetIO_State)

    def refresh_window(self, cpu_state, memory_state, DiskIO_State, NetIO_State):

        dt = datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S')
        text = dt + " | " + cpu_state + " | " + memory_state + " | " + DiskIO_State + " | " + NetIO_State
        return text

    def logSet(self):

        self.filePath = self.newLogFile()
        my_logger = logging.getLogger('MyLogger')
        my_logger.setLevel(logging.INFO)
        # maxBytes: 1024*10 即为10KB。最大设为10MB。
        self.handler = logging.handlers.RotatingFileHandler(self.filePath, maxBytes=1024 * 1024 * 10, backupCount=10, )
        my_logger.addHandler(self.handler)
        return my_logger


if __name__ == '__main__':

    s = ""
    try:
        A = setCPUInfo()
        filePath = A.newLogFile()
        my_logger = A.logSet()
        while 1:
            try:
                args = A.poll()
                s = A.refresh_window(*args)
                my_logger.info(s)
                print "?"
                try:
                    size = os.path.getsize(A.filePath)
                    #100KB 一个文件夹
                    if size > 1024 * 1024 * 5:
                        my_logger.removeHandler(A.handler)
                        my_logger = A.logSet()
                        print "换日志文件存储了！"
                    else:
                        pass
                except Exception as err:
                    print(err)
            except Exception as E:
                print(E)
                my_logger.info(E)

    except (KeyboardInterrupt, SystemExit):
        pass

