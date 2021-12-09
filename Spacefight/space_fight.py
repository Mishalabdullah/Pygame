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
        if keys_press[pygame.K_a]:#BACK
            yellow.x -= VEL
        if keys_press[pygame.K_d]:#UP
            yellow.x += VEL
        if keys_press[pygame.K_w]:#left
            yellow.y -= VEL
        if keys_press[pygame.K_s]:#Right
            yellow.y += VEL

def red_movement(keys_press,red):
        if keys_press[pygame.K_LEFT]:#BACK
            red.x -= VEL
        if keys_press[pygame.K_RIGHT]:#UP
            red.x += VEL
        if keys_press[pygame.K_UP]:#left
            red.y -= VEL
        if keys_press[pygame.K_DOWN]:#Right
            red.y += VEL

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
        keys_press = pygame.key.get_pressed()
        yellow_movement(keys_press, yellow)
        red_movement(keys_press,red)

    pygame.quit()


if __name__  == "__main__":
    main()
