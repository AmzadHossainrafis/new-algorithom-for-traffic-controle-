import pygame as pygame
from satting import Settings 

class Ship():
    """
    Ship class that hold the atribute of  ship and it's activaties 
    
    """

    def __init__(self,ai_game):
        self.settings=Settings()
        self.screen=ai_game.screen
        self.screen_rect= self.screen.get_rect()
        self.image=pygame.transform.scale(pygame.image.load("Image/spacex.png"),(self.settings.ship_height,self.settings.ship_width))
        self.image_rect= self.image.get_rect()
        self.image_rect.midbottom= self.screen_rect.midbottom 
        self.right= False
        self.left=False

    def blit_me(self):
        self.screen.blit(self.image,self.image_rect)


    def ship_move(self):
        if self.right and self.image_rect.x > 0:
            self.image_rect.x +=self.settings.ship_spreed
        elif self.left and self.image_rect.x <  self.image_rect.right :
            self.image_rect.x -=self.settings.ship_spreed
        

        

            





