"""
pygame project no:1 
type : shooting 

name: Amzad hossain
date : 14/8/2021 

description : This is a shooting  game  between 2 players . 
If any player get 10 hit to othe oponnent player ,
the player wins the game is




"""
import pygame as pygame
# import datetime
# import random
# import argparse as argparse
# from game_lib_shooter import *
pygame.font.init()
pygame.mixer.init()


#vriable 
COLOR_WITHE= (255,255,255)
COLOR_BLACK= (0,255,0)
COLOR_RED = (255,0,0)
WHITE=(255,255,255)


width = 500
height = 500
fps= 60
mov= 5
bullet_mov= 7
num_bullet= 4

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

# YELLOW_HIT = pygame.USEREVENT + 1
# RED_HIT = pygame.USEREVENT + 2


#events 
rect_1_hit=pygame.USEREVENT+1
rect_2_hit=pygame.USEREVENT+2

BORDER=pygame.Rect(500//2,0,10,500)






#load_ship 
ship_red=pygame.image.load("image/ship_red.jpg")
ship_yolo=pygame.image.load("image/ship_yolo.jpg")
back_g=pygame.transform.scale(pygame.image.load("image/back.jpg"),(500,500))

#resize the ship 
ship_red=pygame.transform.scale(ship_red, (50,50))
ship_yolo=pygame.transform.scale(ship_yolo, (50,50))

#rotate the ship 
ship_red=pygame.transform.rotate(ship_red, 270)
ship_yolo=pygame.transform.rotate(ship_yolo, 90)


WIN= pygame.display.set_mode((width,height))
pygame.display.set_caption("test game ")

BORDER = pygame.Rect(width//2 - 5, 0, 10, width)






def display_update(rect_1, rect_2,BORDER,rect_1_bullet, rect_2_bullet, rect_1_health , rect_2_health):
    WIN.blit(back_g,(0,0))
    
    WIN.blit(ship_red,(rect_1.x, rect_1.y))
    WIN.blit(ship_yolo,(rect_2.x,rect_2.y))
    
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(rect_1_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(rect_2_health), 1, WHITE)
    pygame.draw.rect(WIN, COLOR_BLACK, BORDER )
    WIN.blit(red_health_text, (500 - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    for bullet in rect_1_bullet:
        pygame.draw.rect(WIN, COLOR_BLACK, bullet)

    for bullet in rect_2_bullet:
        pygame.draw.rect(WIN, COLOR_RED, bullet)
    pygame.display.update()


def move_rect_1(key_press,rect_1):
    if key_press[pygame.K_a] and rect_1.x - mov > 0:
        rect_1.x -= mov
    if key_press[pygame.K_d] and rect_1.x +mov < 210:
        rect_1.x += mov
    if key_press[pygame.K_w] and rect_1.y > 0:
        rect_1.y-= mov
    if key_press[pygame.K_s] and rect_1.y < 450:
        rect_1.y+= mov

def move_rect_2(key_press,rect_2):
    if key_press[pygame.K_LEFT] and rect_2.x - mov > BORDER.x +BORDER.width:
        rect_2.x -= mov
    if key_press[pygame.K_RIGHT] and rect_2.x + mov + rect_2.width < 490:
        rect_2.x += mov
    if key_press[pygame.K_UP] and rect_2.y > 0:
        rect_2.y-= mov
    if key_press[pygame.K_DOWN] and rect_2.y < 450:
        rect_2.y+= mov


def bullet_move(rect_1_bullet,rect_2_bullet, rect_1, rect_2):
    for bullet in rect_1_bullet:
        bullet.x+= bullet_mov
        if rect_2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(rect_2_hit))
            rect_1_bullet.remove(bullet)
        elif bullet.x > 500:
            rect_1_bullet.remove(bullet)

    for bullet in rect_2_bullet:
        bullet.x-= bullet_mov
        if rect_1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(rect_1_hit))
            rect_2_bullet.remove(bullet)
        elif bullet.x < 0:
            rect_2_bullet.remove(bullet)

def main():
    rect_1_bullet=[]
    rect_2_bullet=[]


    rect_1_health= 10
    rect_2_health = 10


    rect_1=pygame.Rect(10,250 , 50 , 50 )
    rect_2=pygame.Rect(450, 250 , 50 , 50)
    run = True
    clock = pygame.time.Clock() 

    

    while run:
        clock.tick(fps) #fps control 
        for event in pygame.event.get(): #event chack 
            if event.type == pygame.QUIT:
                run=False 
                pygame.quit()
                  

            if event.type == pygame.KEYDOWN:
            

                if event.key == pygame.K_SPACE and len(rect_1_bullet) < num_bullet:
                    bullet= pygame.Rect(rect_1.x +rect_1.width, rect_1.y+rect_1.height+rect_1.y//2-2, 10, 5 )  
                    rect_1_bullet.append(bullet)

                if event.key == pygame.K_RCTRL and len(rect_2_bullet)< num_bullet:

                    bullet= pygame.Rect(rect_2.x , rect_2.y//2+rect_2.height+70, 10, 5 )
                    rect_2_bullet.append(bullet)
            if event.type == rect_1_hit:
                rect_1_health -=1
            
                if rect_1_health <=0:
                    win_1=" player 2 win "
                    
            if event.type == rect_2_hit:
                rect_2_health -=1

                if rect_2_health<=0:
                    win_1=" player 1 win "
                 
            # update the present display 
        
        bullet_move(rect_1_bullet,rect_2_bullet, rect_1, rect_2) 
        key_press=pygame.key.get_pressed()
        move_rect_1(key_press, rect_1)
        move_rect_2(key_press, rect_2) 
        display_update(rect_1,rect_2,BORDER,rect_1_bullet,rect_2_bullet,rect_1_health, rect_2_health) 
                
  



if __name__ == '__main__':
    main()