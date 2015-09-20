#!/usr/bin/env python 
#fruit game
#from "Ultimate Guide to raspberry Pi"
#
import pygame
class Turret(pygame.sprite.Sprite):
    def __init__(self,WINDOWWIDTH,WINDOWHEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("images/turret.png")
        self.rect.x = self.image.get_rect()
        self.rect.x = (WINDOWWIDTH-self.rect.width)/2
        self.rect.y = WINDOWHEIGHT-self.rect.height
        
    def update_position(self,direction,WINDOWWIDTH):
        if direction=="left" and self.rect.x>10:
            self.rect.x-=10
        elif direction=="right" and self.rect.x<(WINDOWWIDTH-10):
            selfrect.x+=10
        
    def get_gun_position(self):
        position={}
        position["x"]=self.rect.x+(self.rect.width/2)
        position["y"]=self.rect.y+(self.rect.height/2)
        return position
