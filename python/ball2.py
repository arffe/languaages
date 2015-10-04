#!/usr/bin/env python

print "start"

import pygame, sys, time

pygame.init()
screen = pygame.display.set_mode([640, 480])
clock = pygame.time.Clock()
red=240
green=240
blue=240
r=10
y=200
ydir="up"
xshad=[-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100]
yshad=[-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100,-100]


for x in range (0, 650, 1):
    if (ydir == "down"):
        if (y < 480):
            y += 5
        else:
            ydir = "up"
            y -= 5
    else:
        if (y>0):
            y -= 5
        else:
            ydir = "down"
            y += 5
#    print x, "   ", y
    xshad.append(x)
    xshad.pop(0)
    yshad.append(y)
    yshad.pop(0)
    screen.fill([240,240,240])
    clock.tick(20)
    red=240
    green=240
    blue=240
    for n in range(13):
        pygame.draw.circle(screen, [red,green,blue], [xshad[n],yshad[n]], r, 0)
#        print red, green, blue
        red-=20
        green-=20
        blue-=20
    pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "quitting"
            sys.exit()
