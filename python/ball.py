#!/usr/bin/env python

class Ball:
    def __init__(self, colour, size, direction):
        self.colour = colour
        self.size = size
        self.direction = direction

    def __str__(self):
        msg = "I am now a " + self.size + ", " + self.colour + " ball"
        return msg

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
        elif self.direction == "up":
            self.direction = "down"
