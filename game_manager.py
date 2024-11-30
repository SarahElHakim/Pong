# Importing pygame module and striker and ball classes
import pygame
from pygame.locals import *
from striker import Striker
from ball import Ball

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

# Game Manager
def main():
    running = True

    # Defining the objects
    striker1 = Striker(20, 0, 10, 100, 10, (255,255,255), window, font20)
    striker2 = Striker(900-30, 0, 10, 100, 10, (255,255,255), window, font20)
    ball1 = Ball(900//2, 600//2, 7, 7, (0,0,255), window)
    ball2 = Ball(900//2, 600//2, 7, -7, (255,0,255), window)

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