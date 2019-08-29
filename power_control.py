# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 11:18:16 2015
@author: win7
"""
'''定时关机'''
'''脚本功能：windows下，用户按照一定格式输入关机时间，系统到指定时间自动关闭
  思路：从用户输入获取指定时间 分别以时分秒减去当前时间 最终计算得到当前时间距离指定
  时间还有多少秒 作为关机命令的时间参数
'''
'''需要用到的模块：
        os 用于执行设定的系统命令
        time 用于获取系统时间
 需要用到的命令： shutdown -s -t xxx 其中xxx为距离自动关机所用秒数，即时间参数      
        shutdown -a 取消关机计划
'''
import os,time
#获取用户指定关机时间
print u'使用说明：输入关机时间，格式如：小时:分钟 举个栗子：20:21 然后敲回车 即可.如果想取消定时关机 再次双击打开程序 输入 off 敲回车 即可'.encode('mbcs')
#u'xxx'.encode('mbcs') 使正文字符在控制台正确显示
input_time=raw_input(u'请输入关机时间，格式如：小时:分钟 ：'.encode('mbcs'))
#取消定时关机
#计划总有变化 先留条后路
if input_time == 'off':
  os.system('shutdown -a')
#输入数据检查
#由于是自用 暂时略过
#提取时分秒
h1 = int(input_time[0:2])
m1 = int(input_time[3:5])
#print h1,m1#验证获取是否正确
#获取当前系统时间
mytime = time.strftime('%H:%M:%S')
h2 = int(mytime[0:2])
m2 = int(mytime[3:5])
#print h2,m2 #验证获取是否正确
#对用户输入数据进行整理 防止出现25:76:66这样的时间数据
if h1 > 24:
  h1 = 24
  m2 = 0
if m1 > 60:
  m1 = 60
if h1<h2:
  h1 = h1 + 24 
#计算秒数
s1=(h1+(m1/60.0)-h2-(m2/60.0))*3600
print '距离关机还有 %d 秒' %s1
os.system('shutdown -s -t %d' %s1 )
