# -*- coding:utf-8 -*-
#作者 ：Lyle.Li
#时间 :2019/10/9 16:27
#文件 :spam.py

print('from the spam.py')

money = 1000

def read1():
    print('spam模块',money)

def read2():
    print('spam模块')
    read1()

def change():
    global money
    money=0