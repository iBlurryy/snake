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
class Ball():
    def __init__(self) -> None:
        pass

    def Collisions(self):
        pass


def main(): # the game will go here
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0 # delta time

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("purple") # draws screen color
        pygame.draw.circle(screen, "red", player_pos, 40) # where to draw, color, where on screen, radius

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt


        pygame.display.flip()


        dt = clock.tick(60) / 1000


if __name__ == "__main__": # makes sure that the main() function is not imported 
    main() # the game


