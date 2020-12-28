# -*- coding:utf-8 -*-
# @Time : 2020-12-12 13:59
# @Author: Danica
# @File : alien_invasion.py
import  sys
import pygame
from ship.settings import Settings

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()    #初始化pygame,设置和屏幕对象
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color=(ai_settings.bg_color)



    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(bg_color)    #用背景色填充屏幕，该方法只接收一个参数

        #让最近绘制的屏幕可见
        pygame.display.flap()
run_game()