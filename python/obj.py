#!/usr/bin/env python

print "start obj"

import ball

colours = ["red", "blue", "green", "black"]

myBall = ball.Ball(colours[0], "big", "up")
yourBall = ball.Ball(colours[0], "small", "up")

for i in range (0,4):
    for n in range (0,2):
        myBall.colour=colours[i]
        if i == 3: 
            x = 0
        else:
            x = i + 1
        yourBall.colour=colours[x]   
        if (i == 0) and (n == 0):
            print "I have a {}, {} ball and you have a {}, {} ball".format(myBall.size, myBall.colour, yourBall.size, yourBall.colour) 
        if n == 0: 
            print "bounce my {} ball and bounce your {} ball".format(myBall.colour, yourBall.colour)
        myBall.bounce()
        yourBall.bounce()
        print "my {} ball goes {} and your {} ball goes {}".format(myBall.colour, myBall.direction, yourBall.colour, yourBall.direction)
print myBall
print yourBall
