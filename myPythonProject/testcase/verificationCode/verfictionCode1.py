# -*- coding:utf-8 -*-
# @Time : 2020-12-03 19:38
# @Author: Danica
# @File : verfictionCode1.py
from selenium import webdriver
from PIL import Image
import time,pytesseract

def test1():
    driver=webdriver.Chrome()
    url='http://localhost:8080/jpress/user/register'
    driver.get(url)
    driver.maximize_window()

    #获取验证码图片
    t=time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))      #获取当前时间
    picture_name1=str(t)+'.png'     #定义图片的名称
    driver.save_screenshot(picture_name1)    #截屏

    ce=driver.find_element_by_id('captchaimg')    #获得验证码的id
    print(ce.location)       #包含左顶点的坐标，宽、高
    left=ce.location['x']    #左顶点的x
    top=ce.location['y']     #左顶点的y
    right=ce.size['width']+left    #右底点的x
    height=ce.size['height']+top   #右底点的y

    im=Image.open(picture_name1)
    img=im.crop((left,top,right,height))  #抠图

    t = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    picture_name2=str(t)+'.png'
    img.save(picture_name2)   #这里就是截取到的验证码图片

def test2():
    # picture_name2='checkCode.png'
    image1=Image.open('2020-10-26-20_32_25.png')
    str=pytesseract.image_to_string(image1)   #将图片转换为str,图片过于复杂就无法识别其中的文本
    print(str)
