import pygame.font
from pygame.sprite import  Group
from ship import Ship


class Scoreboard():
    def __init__(self,ai_game):
        self.screen= ai_game.screen
        self.screen_rect= self.screen.get_rect()
        self.settings= ai_game.settings
        self.text_color= (250,0,0)
        self.font=pygame.font.SysFont(None,48)
        self.state=ai_game.stats
        self.ai_game=ai_game


        # self.rect=pygame.Rect(0,0, self.width ,self.height)

        # self.botton_color= self.settings.botton_color
        # self.rect.center=self.screen_rect.center
        # self.height=self.settings.botton_height 
        # self.width= self.settings.botton_width

        self._prep_score()
        self._prep_ships()

    
    def _prep_score(self):
        score_str = str(self.state.score)
        self.score_image=self.font.render(score_str, True, self.text_color, self.settings.black)
        self.sc_rect= self.score_image.get_rect()
        self.sc_rect.right= self.screen_rect.right -20
        self.sc_rect.top=10

    def _prep_ships(self):
        self.ships= Group()
        for ships_num in range(self.settings.ship_limit):
            ship= Ship(self.ai_game)
            ship.rect.x =5+ships_num * ship.rect.width
            ship.rect.y = 1
            self.ships.add(ship)




    def show_score(self):
        self.screen.blit(self.score_image,self.sc_rect)
        self.ships.draw(self.screen)



