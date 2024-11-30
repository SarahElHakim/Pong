# Importing pygame module
import pygame
from pygame.locals import *

# Ball class
class Ball:
    def __init__(self, posx, posy, radius, speed, color,window):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xDir = 1
        self.yDir = -1
        self.ball = pygame.draw.circle(window, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
        self.window = window
 
    def display(self):
        self.ball = pygame.draw.circle(self.window, self.color, (self.posx, self.posy), self.radius)
 
    def update(self):
        self.posx += self.speed*self.xDir
        self.posy += self.speed*self.yDir
 
        # If the ball hits the top or bottom surfaces,
        # then the sign of yDir is changed and it
        # results in a reflection
        if self.posy <= 0 or self.posy >= 600:
            self.yDir *= -1
 
        # If the ball touches the left wall for the first time,
        # The firstTime is set to 0 and we return 1
        # indicating that Striker2 has scored
        # firstTime is set to 0 so that the condition is
        # met only once and we can avoid giving multiple
        # points to the player
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= 900 and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
 
    # Used to reset the position of the ball
    # to the center of the screen
    def reset(self):
        self.posx = 900//2
        self.posy = 600//2
        self.xDir *= -1
        self.firstTime = 1
 
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xDir *= -1
 
    def getRect(self):
        return self.ball