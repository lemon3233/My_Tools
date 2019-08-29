#coding=utf-8
from pyecharts import Line
import re,os

path=(r'E:\\test')
a=os.listdir(path)#列出指定目录下所有的文件名和文件夹名，并赋给a
text=''#初始化text变量
for i in range(len(a)):#迭代a中所有元素，找出符合要求的元素
    if os.path.isfile(os.path.join(path,a[i]))and os.path.splitext(os.path.join(path,a[i]))[1]=='.txt':#判断是否为txt文件
        with open(os.path.join(path,a[i]),'r') as f:#读取txt文件中的内容，并加到text变量里
            text+=f.read()
time=re.compile(r'\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2}')#创建正则表达式
PID=re.compile(r'PID[0-9]{4,5}')
memory=re.compile(r'[0-9]{1,9}M')
test=re.compile(r'[0-9]{1,9}')

text1=  time.findall(text)#找出匹配正则表达式的内容
text2=  PID.findall(text)
text3=  memory.findall(text)
a1=[]
for i in text3:
    a1.append(test.findall(i))#带M的值在表中无法显示，需要提取数字

line = Line("折线图","内存使用量")
#is_label_show是设置上方数据是否显示
line.add(text2[0], text1[::2], a1[::2], is_label_show=False)
line.add(text2[1], text1[::2], a1[1::2], is_label_show=False)
line.render(r'E:\\test\\my_first_chart.html')
