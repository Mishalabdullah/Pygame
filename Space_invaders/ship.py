import pygame
import os
import assets


class Ships:
    def __init__(self,x,y,health= 100):
        self.x = x
        self.y = y
        self.health = health
        self.laser_img = None
        self.ship_img = None
    def draw(self,window):
        window.blit(self.ship_img,(self.x,self.y))


class Player(Ships):
    def __init__(self,x,y,health = 100):
        super().__init__(x,y,health)
        self.ship_img = assets.YELLOW_SPACE_SHIP
        self.laser_img = assets.YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health





