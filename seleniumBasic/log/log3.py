# -*- coding:utf-8 -*-
# @Time : 2020-12-03 19:22
# @Author: Danica
# @File : log3.py

# 封装log2
import logging.handlers
import datetime
def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7,
                                                           atTime=datetime.time(0, 0, 0, 0), encoding='utf-8')
    rf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))

    f_handle = logging.FileHandler('error.log', encoding='utf-8')
    f_handle.setLevel(logging.ERROR)
    f_handle.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d-%(message)s]'))
    logger.addHandler(rf_handler)
    logger.addHandler(f_handle)
    return logger

logger=get_logger()
logger.debug('debug message')
logger.info('infor message')
logger.warning('warning message')
logger.error('error message啦啦啦啦')
logger.critical('critical message')