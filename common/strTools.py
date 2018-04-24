#!/usr/bin/python
#-*- coding:utf-8 -*-
import uuid
'''
@description 获取一些资源
'''

'''
@description 获得唯一名称
@param preStr 加前缀
@return string 
'''
def getUUID(preStr):
    if(preStr=='' or preStr is None):
        return 'autotesting_'+(str)(uuid.uuid1())
    else:
        return 'autotesting_'+str(preStr)+'_'+(str)(uuid.uuid1())

'''
@description 如果目录路径最后一位不是'/'，则修改
@dirPath 需要修改的目录路径
@return string
'''
def amendDirPath(dirPath):
    if(dirPath[-1]!='/'):
        return dirPath+'/'
    return dirPath