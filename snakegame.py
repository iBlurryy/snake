'''
    Author: Karan Patel
    Snake Game
'''

import pygame

'''
Goal of Project:
Create a game to understand the basics of game development with pygame. Making a game without OOP. 
'''

'''
Things to do:
    Collisions
    GUI - boxes, window, etc.
    Add difficulty/increasing difficulty
Extra:
    An account system
    Database to store login information (per user)
    Each login will save high score
'''


def main(): # the game will go here
    pygame.init()

    width, height = 1280, 720

    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    running = True
    dt = 0 # delta time

    player_pos = pygame.Vector2(width / 2, height / 2) # starts player position at the center of the screen
    radius = 40 # radius of the circle


    # Basic game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()

        # Basic collisions using if statements for the x axis
        if player_pos[0] - radius < 0: # finds the x coordinate of the player position and then subtracts the radius giving you the very left point of the circle and if it is less than 0 meaning you hit the left side of the screen
            player_pos[0] = radius # keeps the player x coordinate at 40 so that it doesn't leave the screen. 
        elif player_pos[0] + radius > width:
            player_pos[0] = width - radius

        # Basic collisions using if statements for the y axis
        if player_pos[1] + radius > height: # if it ever passes the bottom of the screen then
            player_pos[1] = height - radius # reset the y coordinate to the height of the window subtracted by the radius of the ball
        elif player_pos[1] - radius < 0:
            player_pos[1] = radius




        # Gets wasd input and moves circle
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

        screen.fill("#1b0369") # draws screen color
        pygame.draw.circle(screen, "red", player_pos, radius) # where to draw, color, where on screen, radius
        pygame.display.flip()


        dt = clock.tick(60) / 1000


if __name__ == "__main__": # makes sure that the main() function is not imported 
    main() # the game


