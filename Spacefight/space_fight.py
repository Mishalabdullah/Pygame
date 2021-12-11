from abc import abstractclassmethod
import pygame
import os
from pygame.draw import rect



from pygame.time import Clock




WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
SPACESHIP_HIGHT,SPACESHIP_WIDTH = 55,40
VEL = 5
BORDER = (WIDTH//2 -5,0,10,HEIGHT)
BULLET_VEL = 8
MAX_BULLETS = 3
YELLOW_HIT  = pygame.USEREVENT +1
RED_HIT = pygame.USEREVENT +2 





## loading all the assests
YELLOW_SPACESHIP_IMAGE = pygame.image.load('Spacefight/Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_HIGHT,SPACESHIP_WIDTH)),90)
RED_SPACESHIP_IMAGE = pygame.image.load('Spacefight/Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_HIGHT,SPACESHIP_WIDTH)),270)
SPACE = pygame.transform.scale(pygame.image.load('Spacefight/Assets/space.png'),(WIDTH,HEIGHT))




def draw(red,yellow,red_bullets,yellow_bullets):
    WIN.blit(SPACE,(0,0))
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.draw.rect(WIN,BLACK,BORDER)

    for bullets in red_bullets:
        pygame.draw.rect(WIN,RED,bullets)
    for bullets in yellow_bullets:
        pygame.draw.rect(WIN,YELLOW,bullets)
    pygame.display.update()


def yellow_movement(keys_press,yellow):
        if keys_press[pygame.K_a] and yellow.x- VEL > 0:#BACK
            yellow.x -= VEL
        if keys_press[pygame.K_d] and yellow.x + VEL + yellow.width  < WIDTH/2:#UP 
            yellow.x += VEL
        if keys_press[pygame.K_w]and yellow.y - VEL > 0:#left
            yellow.y -= VEL
        if keys_press[pygame.K_s]and yellow.y + VEL +yellow.height+15 < HEIGHT:#Right
            yellow.y += VEL

def red_movement(keys_press,red):
        if keys_press[pygame.K_LEFT]and red.x- VEL > WIDTH/2+15:#BACK
            red.x -= VEL
        if keys_press[pygame.K_RIGHT]and red.x + VEL + red.width  <=WIDTH+9:#UP :#UP
            red.x += VEL
        if keys_press[pygame.K_UP]and red.y - VEL > 0:#left
            red.y -= VEL
        if keys_press[pygame.K_DOWN]and red.y + VEL + red.height+15 < HEIGHT:#Right
            red.y += VEL


def handle_bullets(yellow_bullets,red_bullets,red,yellow):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x >WIDTH:
            yellow_bullets.remove(bullet)
        

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x <0:
            red_bullets.remove(bullet)



def main():
    red = pygame.Rect(800,200,SPACESHIP_HIGHT,SPACESHIP_WIDTH)
    yellow = pygame.Rect(30,200,SPACESHIP_HIGHT,SPACESHIP_WIDTH)
    red_bullets = []
    yellow_bullets = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets)< MAX_BULLETS:
                    bullet = pygame.Rect(red.x,red.y+ red.height//2 , 10, 5)
                    red_bullets.append(bullet)

        
        
        keys_press = pygame.key.get_pressed()
        yellow_movement(keys_press, yellow)
        red_movement(keys_press,red)
        handle_bullets(yellow_bullets,red_bullets,red,yellow)
        draw(red,yellow,red_bullets,yellow_bullets)
    


if __name__  == "__main__":
    main()
