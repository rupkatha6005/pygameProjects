import pygame
import time
import random


#initialising pygame
pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width,display_height))  #creating a surface
#pygame.display.update() #updates the screen
pygame.display.set_caption('Snake game')  

blue=(50, 153, 213)#(173, 216, 240)
red=(240,0,0)
black=(0,0,0)
white=(255,255,255)
green = (0, 255, 0)


snake_block = 10
clock = pygame.time.Clock() #tracks time
snake_speed= 10

font_style = pygame.font.SysFont(None,20)
score_font = pygame.font.SysFont('comicsansms',30)

def enlarge_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    display.blit(mesg, [display_width/3, display_height/2])

def gameLoop():
    game_over = False
    game_close = False

    #initial snake position--->
    x1 =  display_width/2   
    y1 = display_height/2  
    x1_change, y1_change = 0, 0#to hold the updating values of the x & y coordinates
    
    snake_list=[]
    length_of_snake = 1
    
    #foods==>
    #randrange() returns randomly selected element from a range, arguments: (start,end)
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody =round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0


    #this loop makes the screen stay
    while not game_over:

        while game_close == True:
            display.fill(blue)
            message('You lost! Press Q-Quit or C-Play again!', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over == True 
                        game_close == False
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():    #event.get()--> returns list of all events.
            if event.type == pygame.QUIT:   #QUIT-->(event)makes quit button work
                game_over = True
            #moving the snake
            #events of KEYDOWN class of pygame-->
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change =0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change =0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

            #game over if hits the boundary-->
        if x1 >= display_width or x1 < 0 or y1 >= display_height or  y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display,green,[foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
        enlarge_snake(snake_block, snake_list)
        pygame.display.update()



        #pygame.draw.rect(display,black,[x1,y1,snake_block,snake_block]) #creating the rectangular snake
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print('mmm')
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foodx = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    # message('You lost!', red)
    # pygame.display.update()
    # time.sleep(2)


    pygame.quit()
    quit()
gameLoop()
