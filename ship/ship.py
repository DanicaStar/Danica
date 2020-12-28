# -*- coding:utf-8 -*-
# @Time : 2020-12-12 13:59
# @Author: Danica
# @File : ship.py
import pygame

class Ship():
    def __init__(self,screen):
        #初始化飞船并设置其初始位置
        self.screen=screen

        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('image/ship.bmp')
        self.rect=pygame.image.get_rect()
        self.screen_rect=self.screen.get_rect()

        #将每艘新飞船都放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.buttom=self.screen_rect.buttom

    def blitme(self):
        pass