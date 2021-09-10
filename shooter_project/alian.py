import pygame as pygame
import random as random
image_1 =pygame.transform.scale(pygame.image.load("Image/ship2.png"),(80,80))
image_2 = pygame.transform.scale(pygame.image.load("Image/ship1.png"),(80,80))



class Alien(pygame.sprite.Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image =random.choice([image_1,image_2])
        self.rect=self.image.get_rect()
        self.rect.x= self.rect.width
        self.rect.y= self.rect.height


    def draw_alian(self):

        pass

    def move_alian(self):
        pass