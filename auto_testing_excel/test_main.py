#!/usr/bin/python
#-*- coding:utf-8 -*-
import commands 
import unittest
import requests
import json
import re 

import config
from config import logger,fail_logger
from automatic_testing.common import HTMLTestRunner 
from automatic_testing.common.excelTools.excelOperator import ExcelTool 

def test(request_s,case):
    def doTest():
        uId=case['id']
        name=case['name']
        url=case['url']
        method=case['method']
        headers=case['headers']
        if(headers is not None and headers.strip()!=''):
            print 'headers::::::',headers
            headers=json.loads(headers)
        param=case['param']
        if(param is not None and param.strip()!=''):
            param=json.loads(param)
        expect=case['expect']
        r=None 
        logger.info('start testing '+str(uId))
        #rquest
        if(request_s is not None):
            if(method=='post'):
                r=request_s.post(url,data=param,headers=headers)
            elif(method=='get'):
                r=request_s.get(url,data=param,headers=headers)
            else:
                logger.error('case:'+str(uId)+',fail##the method \''+method+'\' is not support!')
                fail_logger.error('case:'+str(uId)+',fail##the method \''+method+'\' is not support!')
                raise ValueError('[the method \''+method+'\' is not support!]') 
        else:
            if(method=='post'):
                r=requests.post(url,data=param,headers=headers)
            elif(method=='get'):
                r=requests.get(url,data=param,headers=headers)
            else:
                logger.error('case:'+str(uId)+',fail##the method \''+method+'\' is not support!')
                fail_logger.error('case:'+str(uId)+',fail##the method \''+method+'\' is not support!')
                raise ValueError('[the method \''+method+'\' is not support!]') 
        #assert
        if(r is not None):
                if(assertTools.assertEqual(expect.strip(),r.text.decode('unicode-escape').strip())):
                    logger.info('case:'+str(uId)+',success##status_code:'+str(r.status_code)+'##'+expect.strip()+' equal '+r.text.decode('unicode-escape').strip())
                else:
                    logger.error('case:'+str(uId)+',fail##status_code:'+str(r.status_code)+'##'+expect.strip()+' not equal '+r.text.decode('unicode-escape').strip())
                    fail_logger.error('case:'+str(uId)+',fail##status_code:'+str(r.status_code)+'##'+expect.strip()+' not equal '+r.text.decode('unicode-escape').strip())
                    raise AssertionError(expect.strip()+' not equal '+r.text.decode('unicode-escape').strip())
        else:
            logger.error('case:'+str(uId)+',fail##request response None')
            fail_logger.error('case:'+str(uId)+',fail##request response None')
    return doTest

class assertTools():
    @staticmethod
    def assertEqual(regular,source):
        regular=regular.replace('[','\[')
        regular=regular.replace(']','\]')
        regular=regular.replace('*','\*')
        pattern=re.compile(regular)
        if(pattern.match(source)):
            return True 

class Test(unittest.TestCase):
    @classmethod
    def init(self):
        logger.info('init')
        logger.info('clean logs')
        status,output=commands.getstatusoutput('>'+config.log_file)
        status,output=commands.getstatusoutput('>'+config.fail_log_file)
        logger.info('read case from excel')
        excelTool=ExcelTool()
        self.cases=excelTool.readAsDictArray(config.excel_file,config.test_sheet_num)
        if(config.use_session):
            self.s=requests.Session()
        else:
            self.s=None

        logger.info('start to test')
        for curt_case in range(len(self.cases)):
            self.add_method('test'+str(self.cases[curt_case]['id']),test(self.s,self.cases[curt_case])) 

    @classmethod
    def add_method(cls,func_name,func):
        def newFunc(self,*args,**kw):
            func(*args,**kw)    
        setattr(cls,func_name,newFunc)

if __name__=='__main__':
    Test.init()    
    #HTMLTestRunner.main()
    unittest.main()
