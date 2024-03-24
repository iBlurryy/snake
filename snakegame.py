'''
    Author: Karan Patel
    Snake Game
'''

import pygame

'''
Things to do:
    Collisions
    GUI - boxes, window, etc.
    Set up tkinter window loop
    Add difficulty/increasing difficulty
Extra:
    An account system
    Database to store login information (per user)
    Each login will save high score
'''

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

def main(): # the game will go here
    while running:
        for event in pygame.even.get():
            if event.type == pygame.QUIT:
                running = False

    screen.fill("purple")

    pygame.display.flip()

    clock.tick(60)


if __name__ == "__main__": # makes sure that the main() function is not imported 
    main() # the game


