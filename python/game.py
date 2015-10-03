#!/usr/bin/env python

print "start"

import pygame, sys

pygame.init()
screen = pygame.display.set_mode([640, 480])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print "quitting"
            sys.exit()
    
    
