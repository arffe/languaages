#!/usr/bin/env python

print "start"

import pygame, sys, time

pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
x = 100
y = 100
screen.fill([50,89,130])
pygame.draw.circle(screen, [150,50,50], [x,y], 30, 0)
pygame.display.flip()
time.sleep(2)
while x < 641:
        print x , " " , y
        screen.fill([50,89,130])
        clock.tick(60)
        pygame.draw.circle(screen, [150,50,50], [x,y], 30, 0)
        pygame.display.flip()
        x += 4
        y += 3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "quitting"
            sys.exit()


