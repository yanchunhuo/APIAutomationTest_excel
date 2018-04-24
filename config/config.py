#!/usr/bin/python
#-*- coding:utf-8 -*-
import logging

'''[http config]'''
use_session=True

'''[case config]'''
excel_file='cases/cases.xlsx'
test_sheet_num=1

'''[log config]'''
log_file='logs/test.log'
fail_log_file='logs/test_fail.log'
formatter=logging.Formatter('%(asctime)s-%(filename)s-%(name)s-%(levelname)s : %(message)s')
#logger用于记录测试信息，包括测试成功、异常、错误
fileHandler=logging.FileHandler(log_file,'a')
#用于输出到屏幕
streamHandler=logging.StreamHandler()
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)
logger=logging.getLogger('log')
logger.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
#fail_logger用于记录测试错误，包括测试失败、异常、错误
fail_fileHandler=logging.FileHandler(fail_log_file,'a')
fail_fileHandler.setFormatter(formatter)
fail_logger=logging.getLogger('fail_log')
fail_logger.setLevel(logging.DEBUG)
fail_logger.addHandler(fail_fileHandler)
