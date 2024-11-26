# Importing pygame module
import pygame
from pygame.locals import *

# Initiating pygame
pygame.init()

# Font used for text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# Create the display window 
window = pygame.display.set_mode((900, 600))
window.fill((79, 219, 232))
pygame.display.set_caption("Pong")


# Used to control the frame rate
clock = pygame.time.Clock()
FPS = 30

# Striker class
class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        
        # Rectangle that is used to control the position and collision of the object
        self.strikerRect = pygame.Rect(posx, posy, width, height)
        # Object that is blit on the screen
        self.striker = pygame.draw.rect(window, self.color, self.strikerRect)

    # Display the object on the screen
    def display(self):
        self.striker = pygame.draw.rect(window, self.color, self.strikerRect)

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
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        window.blit(text, textRect)
 
    def getRect(self):
        return self.strikerRect



# Ball class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xDir = 1
        self.yDir = -1
        self.ball = pygame.draw.circle(window, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
 
    def display(self):
        self.ball = pygame.draw.circle(window, self.color, (self.posx, self.posy), self.radius)
 
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


# Game Manager
def main():
    running = True

    # Defining the objects
    striker1 = Striker(20, 0, 10, 100, 10, (255,255,255))
    striker2 = Striker(900-30, 0, 10, 100, 10, (255,255,255))
    ball1 = Ball(900//2, 600//2, 7, 7, (0,0,255))
    ball2 = Ball(900//2, 600//2, 7, 5, (255,0,255))

    listOfStrikers = [striker1, striker2]

    # Initial parameters of the players
    striker1Score, striker2Score = 0, 0
    striker1YDir, striker2YDir = 0, 0

    while running:
        window.fill((79, 219, 232))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    striker2YDir = -1
                if event.key == pygame.K_DOWN:
                    striker2YDir = 1
                if event.key == pygame.K_w:
                    striker1YDir = -1
                if event.key == pygame.K_s:
                    striker1YDir = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    striker2YDir = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    striker1YDir = 0

        # Collision detection
        for striker in listOfStrikers:
            if pygame.Rect.colliderect(ball1.getRect(), striker.getRect()):
                ball1.hit()
            if pygame.Rect.colliderect(ball2.getRect(), striker.getRect()):
                ball2.hit()

        # Updating the objects
        striker1.update(striker1YDir)
        striker2.update(striker2YDir)
        point1 = ball1.update()
        point2 = ball2.update()

        # -1 -> Striker_1 has scored
        # +1 -> Striker_2 has scored
        # 0 -> None of them scored
        if point1 == -1:
            striker1Score += 1
        elif point1 == 1:
            striker2Score += 1
            
        if point2 == -1:
            striker1Score += 1
        elif point2 == 1:
            striker2Score += 1

        if point1: 
            # Someone has scored a point and the
            # ball is out of bounds. So, we reset it's position
            ball1.reset()
        
        if point2: 
            ball2.reset()
        

        # Displaying the objects on the screen
        striker1.display()
        striker2.display()
        ball1.display()
        ball2.display()

        # Displaying the scores of the players
        striker1.displayScore("Player_1 : ", striker1Score, 100, 20, (0,0,0))
        striker2.displayScore("Player_2 : ", striker2Score, 900-100, 20, (0,0,0))

        pygame.display.update()
        # Adjusting the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()