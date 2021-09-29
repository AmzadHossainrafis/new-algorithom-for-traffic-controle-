import pygame as pygame
import random as random
# load image
image_1 = pygame.transform.scale(
    pygame.image.load("Image/ship2.png"), (50, 50))
image_2 = pygame.transform.scale(
    pygame.image.load("Image/ship1.png"), (50, 50))


class Alien(pygame.sprite.Sprite):
    """this class handel the alian and it's activaties """

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = random.choice([image_1, image_2])
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def draw_alian(self):
        """this function draw the alian in the screen"""

        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        """this function handel the movement of the alian """
        self.rect.x += (self.settings.alien_spreed *
                        self.settings.fleet_direction)

    def chack_edgs(self):
        """this functin chk if the alian edge hits the edges of the screen"""
        self.screen_a = self.screen.get_rect()
        if self.rect.right >= self.screen_a.right or self.rect.left < 0:
            return True
