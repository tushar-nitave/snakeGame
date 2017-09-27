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
playArea = pygame.display.set_mode(resolution)
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


#5. Method Game Over

def gameOver():
    disFont = pygame.font.SysFont('Monaco', 68)
    surface = disFont.render('Game Over', True, white)
    rect = surface.get_rect()
    rect.midtop = (400,15)
    playArea.blit(surface, rect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()   #termination pygame module
    sys.exit()  #terminating python console

#gameOver()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_dir_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_dir_to = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_dir_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_dir_to = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                sys.exit()
                
                
    #checking for valid directions
    if change_dir_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if change_dir_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_dir_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_dir_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
        
    #changing snake length
    if direction == 'RIGHT' or direction == 'DOWN':
        snakePosition[0] += 10
    if direction == 'UP' or direction == 'LEFT':
        snakePosition[0] -= 10
        
    #snake body mechanism
    snakeLength.insert(0, list(snakePosition))
    if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
        foodSpawn = False
    else:
        snakeLength.pop()
    if foodSpawn == False:
        foodPosition = [random.randrange(1,80)*10, random.randrange(1,60)*10]
    foodSpawn = True
    
    #adding elements to the canvas(playing surface)
    
    playArea.fill(white)
    pygame.display.flip()
    