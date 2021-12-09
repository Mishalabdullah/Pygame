import pygame
class charecter:
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/123.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)
print("done")