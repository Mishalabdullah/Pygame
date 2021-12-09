import pygame
import os


#from tim.main import RED_SPACESHIP_IMAGE, YELLOW_SPACESHIP_IMAGE

from pygame.time import Clock


WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")
FPS = 60
WHITE = (255,255,255)
SPACESHIP_HIGHT,SPACESHIP_WIDTH = 55,40


YELLOW_SPACESHIP_IMAGE = pygame.image.load('Spacefight/Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_HIGHT,SPACESHIP_WIDTH)),90)
RED_SPACESHIP_IMAGE = pygame.image.load('Spacefight/Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_HIGHT,SPACESHIP_WIDTH)),270)

def draw():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(30,200))
    WIN.blit(RED_SPACESHIP,(800,200))
    pygame.display.update()




def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    
    pygame.quit()
        

if __name__  == "__main__":
    main()