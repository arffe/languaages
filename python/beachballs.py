#!/usr/bin/env python
import pygame, sys
from random import *
pygame.init()

#----- ball subclass definition -------
class myBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self) # call sprite initialisation
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
        print "self.rect.left = ", self.rect.left, \
        "self.rect.top = ", self.rect.top
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
#------ main program ------------------

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
img_file = "beach_ball.png"
balls = []
for row in range (0,3):
    for column in range(0, 3):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-2, 2]), choice([-2, 2])]
        ball = myBallClass(img_file, location, speed)
        balls.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
#    pygame.time.delay(20)
#    screen.fill([255,255,255])
#    for ball in balls:
#        ball.move()
#        screen.blit(ball.image, ball.rect)
#    pygame.display.flip()
