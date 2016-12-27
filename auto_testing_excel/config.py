#!/usr/bin/python
#-*- coding:utf-8 -*-
import logging

#[http config]
use_session=True

#[case config]
excel_file='/root/automatic_testing/auto_testing_excel/case.xlsx'
test_sheet_num=1

#[log config]
log_file='/root/automatic_testing/auto_testing_excel/auto_testing_excel.log'
fail_log_file='/root/automatic_testing/auto_testing_excel/auto_testing_excel_fail.log'
formatter=logging.Formatter('%(asctime)s-%(filename)s-%(name)s-%(levelname)s : %(message)s')

fileHandler=logging.FileHandler(log_file,'a')
streamHandler=logging.StreamHandler()
fileHandler.setFormatter(formatter)
streamHandler.setFormatter(formatter)
logger=logging.getLogger('log')
logger.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)
logger.addHandler(streamHandler)

fail_fileHandler=logging.FileHandler(fail_log_file,'a')
fail_fileHandler.setFormatter(formatter)
fail_logger=logging.getLogger('fail_log')
fail_logger.setLevel(logging.DEBUG)
fail_logger.addHandler(fail_fileHandler)
