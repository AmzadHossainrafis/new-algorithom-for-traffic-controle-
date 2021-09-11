import pygame as pygame
import random as random
image_1 =pygame.transform.scale(pygame.image.load("Image/ship2.png"),(50,50))
image_2 = pygame.transform.scale(pygame.image.load("Image/ship1.png"),(50,50))



class Alien(pygame.sprite.Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.image =random.choice([image_1,image_2])
        self.rect=self.image.get_rect()
        self.rect.x= self.rect.width
        self.rect.y= self.rect.height


    def draw_alian(self):

        pygame.draw.rect(self.screen, self.color, self.rect)

    def move_alian(self):
        pass