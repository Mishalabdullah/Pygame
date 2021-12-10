import pygame
import os



from pygame.time import Clock




WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")
FPS = 60
WHITE = (255,255,255)
BLACK = (0,0,0)
SPACESHIP_HIGHT,SPACESHIP_WIDTH = 55,40
VEL = 5
BORDER = (WIDTH/2 -5,0,10,HEIGHT)
BULLET_VEL = 8
MAX_BULLETS = 3



red_bullets = []
yellow_bullets = []


YELLOW_SPACESHIP_IMAGE = pygame.image.load('Spacefight/Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_HIGHT,SPACESHIP_WIDTH)),90)
RED_SPACESHIP_IMAGE = pygame.image.load('Spacefight/Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_HIGHT,SPACESHIP_WIDTH)),270)
red = pygame.Rect(800,200,SPACESHIP_HIGHT,SPACESHIP_WIDTH)
yellow = pygame.Rect(30,200,SPACESHIP_HIGHT,SPACESHIP_WIDTH)
def draw():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.draw.rect(WIN,BLACK,BORDER)
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
        if keys_press[pygame.K_RIGHT]and red.x + VEL + yellow.width  <=WIDTH+9:#UP :#UP
            red.x += VEL
        if keys_press[pygame.K_UP]and red.y - VEL > 0:#left
            red.y -= VEL
        if keys_press[pygame.K_DOWN]and red.y + VEL +yellow.height+15 < HEIGHT:#Right
            red.y += VEL

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(yellow_bullets)< MAX_BULLETS:
                        bullet = pygame.Rect(yellow.x+yellow.width,yellow.height/2)
                        yellow_bullets.append(bullet)
                    if event.key == pygame.K_RCTRL and len(red_bullets)< MAX_BULLETS:
                        bullet = pygame.Rect(red.x+red.width,yellow.height/2)
                        red_bullets.append()
        draw()
        keys_press = pygame.key.get_pressed()
        yellow_movement(keys_press, yellow)
        red_movement(keys_press,red)

    pygame.quit()


if __name__  == "__main__":
    main()
