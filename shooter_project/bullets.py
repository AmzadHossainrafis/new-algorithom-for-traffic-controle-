import pygame as pygame
# from pygame.sprite import Sprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.setting= ai_game.settings
        self.color=self.setting.bullet_color
        self.rect=pygame.Rect(0,0,self.setting.bullet_width,self.setting.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop


    def update(self):

        self.rect.y -=self.setting.bullet_spreed 

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
