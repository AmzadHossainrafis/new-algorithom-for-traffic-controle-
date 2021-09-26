import pygame as pygame
import pygame.font


class Button():
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.height = self.settings.botton_height
        self.width = self.settings.botton_width
        self.botton_color = self.settings.botton_color
        self.text_color = self.settings.botton_textc
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_mag(msg)

    def _prep_mag(self, msg):
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.botton_color)
        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.center = self.screen_rect.center

    def draw_botton(self):
        self.screen.fill(self.botton_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_rect)
