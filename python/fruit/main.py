#!/usr/bin/env python 
#fruit game
#from "Ultimate Guide to raspberry Pi"
#
import math,random,pygame,sys
from fruit import *; from game import *; from turret import *; from bullet import *

##TOP LEVEL CONSTANTS
FPS=30
WINDOWWIDTH=480; WINDOWHEIGHT=640
GAMETITLE="Pi Splat"
WHITE=[255,255,255]; RED=[255,0,0]; GREEN=[0,255,0];
BLUE=[0,0,255]; BLACK=[0,0,0]
SPEED=0.5

#MAIN
def main():
    game=Game()
    
    #set up initial display
    pygame.init()
    pygame.key.set_repeat(1, 75)
    scoreFont=pygame.font.Font("256BYTES.TTF",32)
    clock=pygame.time.Clock()
    surface=pygame.display.set_mode([WINDOWWIDTH,WINDOWHEIGHT])
    pygame.display.set_caption(GAMETITLE)

    # main game loop
    game_over=False
    live_fruit_sprites=pygame.sprite.Group()
    bullet_sprites=pygame.sprite.Group()
    other_sprites=pygame.sprite.Group()
    turret=Turret(WINDOWWIDTH,WINDOWHEIGHT)
    other_sprites.add(turret)    
    ticktock=1
    while game_over==False:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    game_over=True

        if ticktock % (FPS/SPEED)==1:
            if len(live_fruit_sprites)<10:
                live_fruit_sprites.add((Fruit(WINDOWWIDTH)))
        for sprite in bullet_sprites:
            sprite.update_position()
        
        collision=pygame.sprite.groupcollide(live_fruit_sprites.bullet_sprites.False.True)
        if collisions:
            for fruit in collisions:
                fruit.shoot(game)
        
        surface.fill(BLACK)
        bullet_sprites.draw(surface)
        other_sprites.draw(surface)
        
        for sprite in live_fruit_sprites:
            sprite.update_position(SPEED,WINDOWHEIGHT,game)
        
        live_fruit_sprites.draw(surface)
        scoreText=scoreFont.render('Score: '+str(game.get_score()),True,GREEN)
        surface.blit(scoreText,(10,10))
               
        pygame.display.update()
        ticktock+=1
        if game.get_raspberries_saved()>=10:
            game_over=True

        clock.tick(FPS)
# handle end of game
    surface.fill(BLACK)
    scoreText=scoreFont.render('Game over. Score: '+str(game.get_score()),True,GREEN)
    surface.blit(scoreText,(10,200))
    pygame.display.update()
    
    raw_input("press any key")





if __name__ == '__main__':
    main()
