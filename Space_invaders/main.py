import pygame
import sys
import os
import time
import random
from ship import *
import enemy_ship
pygame.font.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")


# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background-black.png")), (WIDTH, HEIGHT))


def main():
    FPS = 60 
    clock = pygame.time.Clock()
    main_font = pygame.font.SysFont(("comicsans"), 50)
    lost_font = pygame.font.SysFont(("comicsans"), 60)
    lost = False
    run = True
    lost_count = 0
    level1 = 0
    lives = 5
    player_vel = 8
    player = Player(300, 200)
    fire_bullet = []
    enemies = []
    wave_length = 5
    enemy_vel = 1
    laser_vel = 8
    Yellow=(255,255,0)
    
    def handle_lasers(fire_bullet):  
   
        for lasers in fire_bullet:
            lasers.y -= laser_vel        
    def redraw_window(fire_bullet):
        WIN.blit(BG, (0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level1}", 1, (255,255,255))
        bullet = assets.YELLOW_LASER
        for lasers in fire_bullet:
            pygame.draw.rect(WIN,Yellow,lasers)
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH -195,10))
        #blasting = WIN.blit(bullet,(player.x,player.y))

            #WIN.blit(bullet,(player.x,player.y))
        '''for i in fire_bullet:
            pygame.draw.rect(WIN,Yellow,i)'''
        for enemy in enemies:
            enemy.draw(WIN)
        handle_lasers(fire_bullet)
        player.draw(WIN)
        
        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2-130,HEIGHT/2-100))     

    
        pygame.display.update()
    def handle_laser(laser_fire):
        for i in fire_bullet:
            i.y += laser_vel
            

    while run:
        clock.tick(FPS)
        

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue
        if len(enemies)==0:
            level1 += 1
            wave_length += 5
            for i in range(wave_length):

                enemy = enemy_ship.enemy(random.randrange(50,WIDTH-100),random.randrange(-1000,-100),random.choice(["red","blue","green"])) 
                enemies.append(enemy)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        #movemnt 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x -player_vel >0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x - player_vel < WIDTH -110:
            player.x += player_vel
        if keys[pygame.K_s] and player.y - player_vel <HEIGHT - 100:
            player.y += player_vel
        if keys[pygame.K_w]and player.y -player_vel >0:
            player.y -= player_vel
        if keys[pygame.K_SPACE]: 
                lasers = pygame.Rect(player.x+45, player.y-20 , 10, 25)
                fire_bullet.append(lasers)

                  
            
        for enemy in enemies:
            enemy.move(enemy_vel)
            if enemy.y + 30  > HEIGHT:
                lives -= 1
                enemies.remove((enemy))
        
        redraw_window(fire_bullet)
    pygame.display.flip()
main()