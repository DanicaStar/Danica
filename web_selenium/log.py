# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 6:17 下午
# @Author  : danica
# @FileName: log.py
# @Software: PyCharm


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


logger = get_logger()
logger.debug('debug message')
logger.info('infor message')
logger.warning('warning message')
logger.error('error message啦啦啦啦')
logger.critical('critical message')


# 创建日志器对象  (一个日志器对象可以有多个处理器，每个处理器都可有自己的格式器、过滤器)
logger = logging.getLogger('logger')
# 创建控制台处理器
sh = logging.StreamHandler()
# 格式器,日志内容：时间、事件、信息描述、谁操作
formatter = logging.Formatter(fmt=f'%(asctime)s  %(filename)s  %(levelname)s  %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
# logger日志器添加处理器
logger.addHandler(sh)
sh.setFormatter(formatter)
logger.info('小丸子')
logger.error('小丸子2')
# 通过级别控制不同端输出不同内容
