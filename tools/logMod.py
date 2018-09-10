#!/usr/local/bin/python
# -*- coding:utf-8 -*-
import logging

# 通过下面的方式进行简单配置输出方式与日志级别
logger = logging.getLogger("Log_Name")

logging.basicConfig(filename='logger.log', level=logging.INFO)
logger.setLevel(logging.ERROR) # 设置日志级别为ERROR，即只有日志级别大于等于ERROR的日志才会输出
logger.addHandler('handle_name') # 为Logger实例增加一个处理器
logger.removeHandler('handle_name') # 为Logger实例删除一个处理器
formatter = logging.Formatter(fmt=None, datefmt=None)


logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
