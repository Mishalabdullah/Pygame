import pygame
import os
import assets
from ship import Ships
import assets
class enemy(Ships):
    clour_map={
        "red":(assets.RED_SPACE_SHIP,assets.RED_LASER),
        "blue":(assets.BLUE_SPACE_SHIP,assets.BLUE_LASER),
        "green":(assets.GREEN_SPACE_SHIP,assets.GREEN_LASER)

        
    }
    def __init__(self, x, y,colour,health = 100): 
        super().__init__(x,y,health)
        self.ship_img,self.laser_img = self.clour_map[colour]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self,vel):
        self.y += vel
         