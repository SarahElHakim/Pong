# Importing pygame module
import pygame
from pygame.locals import *

# Striker class
class Striker:
    def __init__(self, posx, posy, width, height, speed, color, window, font):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.window = window
        self.font = font
        
        # Rectangle that is used to control the position and collision of the object
        self.strikerRect = pygame.Rect(posx, posy, width, height)
        # Object that is blit on the screen
        self.striker = pygame.draw.rect(window, self.color, self.strikerRect)

    # Display the object on the screen
    def display(self):
        self.striker = pygame.draw.rect(self.window, self.color, self.strikerRect)

    # Used to update the state of the object
    # yDir represents the direction of the striker movement
    # if yDir == -1 ==> The object is moving upwards
    # if yDir == 1 ==> The object is moving downwards
    # if yDir == 0 ==> The object is not moving
    def update(self, yDir):
        self.posy = self.posy + self.speed*yDir
        # Restricting the striker to be below
        # the top surface of the screen
        if self.posy <= 0:
            self.posy = 0
        # Restricting the striker to be above
        # the bottom surface of the screen
        elif self.posy + self.height >= 600:
            self.posy = 600-self.height
 
        # Updating the rect with the new values
        self.strikerRect = (self.posx, self.posy, self.width, self.height)
 
    # Used to render the score on to the screen
    # First, create a text object using the font.render() method
    # Then, get the rect of that text using the get_rect() method
    # Finally blit the text on to the screen
    def displayScore(self, text, score, x, y, color):
        text = self.font.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        self.window.blit(text, textRect)
 
    def getRect(self):
        return self.strikerRect