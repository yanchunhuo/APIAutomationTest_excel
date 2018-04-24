#!/usr/bin/python
#-*- coding:utf-8 -*-
'''
该模块存放一些共用的修饰器
'''
#日志修饰器
def log(func):
    def wrapper(*args,**kw):
        print '调用函数的参数为:',args,kw
        print '开始执行函数'
        func(*args,**kw)
        print '结束执行函数'
    return wrapper


if __name__=='__main__':
    print "手术室"
