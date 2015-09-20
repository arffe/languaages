#!/usr/bin/env python 
#fruit game
#from "Ultimate Guide to raspberry Pi"
#
import pygame,random

class Fruit(pygame.sprite.Sprite):

    def __init__(self,WINDOWWIDTH):
        pygame.sprite.Sprite.__init__(self)
        self._species=random.choice(["raspberry", "strawberry", "cherry", "pear", "banana"])
        self.image=pygame.image.load("images/"+self._species+".png")
        self.rect=self.image.get_rect()
        self.rect.y=0-self.rect.height
        self.rect.x=(random.randint(self.rect.width/2,(WINDOWWIDTH-self.rect.width)))
        
    def update_position(self,speed,WINDOWHEIGHT,game):
        if self.rect.y<(WINDOWHEIGHT):
            self.rect.y+=speed*5
        else:
            if self._species=="raspberry":
                game.update_score(50)
                game.update_raspberries_saved()
            else:
                game.update_score(-10)
            self.kill()
            
    def shot(self,game):
        if self._species=="raspberry":
            game.update_score(-50)
        else:
            game.update_score(10)
        self.kill()
