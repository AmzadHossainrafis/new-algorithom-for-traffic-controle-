import pygame as pygame
from satting import Settings


class Ship(pygame.sprite.Sprite):
    """
    Ship class that hold the atribute of  ship and it's activaties 

    """

    def __init__(self, ai_game):
        super().__init__()
        self.settings = Settings()
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.transform.scale(pygame.image.load(
            "Image/spacex.png"), (self.settings.ship_height, self.settings.ship_width))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.right = False
        self.left = False

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def ship_move(self):
        if self.right and self.rect.x > 0:
            self.rect.x += self.settings.ship_spreed
        elif self.left and self.rect.x < self.rect.right:
            self.rect.x -= self.settings.ship_spreed

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
