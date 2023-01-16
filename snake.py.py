from ctypes import sizeof
import pygame
import random
pygame.init()

white=(225,225,225)
red=(225,0,0)
black=(0,0,0)
fps=30

screen_width= 900
screen_height=500
game_window=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snakes with Solomon")
pygame.display.update()

game_exit= False
game_over= False
snake_x=50
snake_y=50
food_x=random.randint(40,screen_width/2)
food_y=random.randint(40,screen_height/2)
snake_size=20
velocity_x=0
velocity_y=0
score=0
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,30)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(game_window,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

snake_list=[]
snake_length=1

while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=10
                velocity_y=0

            if event.key==pygame.K_LEFT:
                velocity_x= -10
                velocity_y=0

            if event.key==pygame.K_UP:
                velocity_y= -10
                velocity_x=0

            if event.key==pygame.K_DOWN:
                velocity_y=10
                velocity_x=0

    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        score+=10
        food_x=random.randint(40,screen_width/2)
        food_y=random.randint(40,screen_height/2)
        snake_length+=4

    game_window.fill(white)
    pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])

    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)
    if len(snake_list)>(snake_length):
        del snake_list[0]
    
    plot_snake(game_window,black,snake_list,snake_size)

    text_screen("Score= "+str(score),red,5,5)
    pygame.display.update()
    clock.tick(fps)
    snake_x+= velocity_x
    snake_y+=velocity_y
    
    
pygame.quit()
quit()