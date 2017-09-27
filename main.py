#developing snake game

import pygame
import sys, random, time


# 1. Initializing pygame module

if_any_error = pygame.init()    #this modules checks for errors and returns the output in form of tuple.

if if_any_error[1] > 0:
    print("{0} errors were found! Terminating the program....".format(if_any_error[1]))
    sys.exit(-1)
else:
    print("All modules initialized successfully!")
    
    
# 2. Playing surface are for game

resolution = (800,600)
display_size = pygame.display.set_mode(resolution)
pygame.display.set_caption('Snake Game')


#3. colors
red = pygame.Color(255, 255, 0) #Game over
white = pygame.Color(255,255,255) #background
black = pygame.Color(0,0,0) #score

#4. Variables for game play

direction = 'RIGHT'
change_dir_to = direction

snakePosition = [700,100]
snakeLength = [[100,50],[90,50],[80,50]]

foodPosition = [random.randrange(1,80)*10, random.randrange(1,60)*10]
foodSpawn = True

