# -*- coding:utf-8 -*-
# @Time : 2020-12-03 19:31
# @Author: Danica
# @File : util.py
import pickle, random, string, time, os
from myPythonProject.lib.ShowapiRequest import ShowapiRequest
from PIL import Image
import logging.handlers
import datetime


def get_code(driver, id):
    # 获取验证码图片
    t = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    path = os.path.dirname(os.path.dirname(__file__)) + "\\screenshots"      #获取screenshots目录路径
    picture_name1 = path +'\\' + str(t) + '.png'
    driver.save_screenshot(picture_name1)    #将截屏图片保存到screenshots目录下

    ce = driver.find_element_by_id('captchaimg')
    print(ce.location)
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top

    im = Image.open(picture_name1)
    img = im.crop((left, top, right, height))  # 抠图

    t = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    picture_name2 = path +'\\' + str(t) + '.png'
    img.save(picture_name2)  # 这里就是截取到的验证码图片

    r = ShowapiRequest("http://route.showapi.com/184-4", "377219", "5ccd886ca0db45e28b352d8177d74cab")
    r.addFilePara("image", picture_name2)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    body = res.json()['showapi_res_body']  # 字符串要转换为字典格式
    code = body['Result']
    return code

def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


def save_cookie(driver, path):
    with open(path, 'wb') as filehandle:
        cookies = driver.get.cookies()
        print(cookies)
        pickle.dump(cookies, filehandle)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


def get_logger():
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    log_path=os.path.dirname(os.path.dirname(__file__))+"\\logs"
    log_name1 = log_path + '\\'  + 'all.log'
    rf_handler = logging.handlers.TimedRotatingFileHandler(log_name1, when='midnight', interval=1, backupCount=7,atTime=datetime.time(0,0,0,0),encoding='utf-8')
    rf_handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(message)s'))

    log_name2 = log_path + '\\' + 'error.log'
    f_handle = logging.FileHandler(log_name2,encoding='utf-8')
    f_handle.setLevel(logging.ERROR)
    f_handle.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d-%(message)s]'))
    logger.addHandler(rf_handler)
    logger.addHandler(f_handle)
    return logger