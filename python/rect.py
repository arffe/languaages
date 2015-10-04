#!/usr/bin/env python

import pygame, sys, random

print "start"

pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([200,200,200])

for i in range (100):
    r = random.randint(0, 200)
    b = random.randint(0, 200)
    g = random.randint(0, 200)
    width = random.randint(0, 250)
    height = random.randint(0, 100)
    top = random.randint(0, 400)
    left = random.randint(0, 500)
    pygame.draw.rect(screen, [r,g,b], [left, top, width, height], 2)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "quitting"
            sys.exit()


