"""
alian invator is space shooting game which is a single player game that
this is a university project 
game name : alian invator
name : amzad hossain 
e-mail: amzad.rafi@northsouth.edu
id : 1530530o42

"""


# import

# import math as math     #for math calculation
from bullets import Bullet
from satting import Settings
from scoreboard import Scoreboard
from button import Button
from game_stats import GameState
from alian import Alien
from ship import Ship
import sys
import argparse  # argparse
import pygame as pygame  # main game module
import random
from time import sleep  # random module
from pygame import mixer  # mixer for music

pygame.font.init()
pygame.mixer.init()
pygame.init()
clock = pygame.time.Clock()

# class import


class Game():
    '''this is the main game class this class handel the '''

    def __init__(self):
        self.settings = Settings()  # creat a instance of Settings class
        self.screen = pygame.display.set_mode(
            (self.settings.height, self.settings.width))
        pygame.display.set_caption("Alian invator")
        self.rect = self.screen.get_rect()
        self.background_music = mixer.music.load("music/background.wav")

        # self.fire_music=mixer.music.load("music/background.wav")

        # allow to acces screen right lefe top and bollom etc
        self.ship = Ship(self)
        self.stats = GameState(self)
        self.scoreboard = Scoreboard(self)
        self.bullets = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()
        self.play_button = Button(self, "play")
        self.create_fleet()

    def main(self):
        # main while loop
        mixer.music.play(-1)
        while True:

            self._event()
            self.ship.ship_move()
            self.update_bullets()
            self.update_alien()

            # update the display
            self._update_display()
            # control the frame rate
            clock.tick(60)

    # update the display

    def _update_display(self):
        # fill the display
        self.screen.fill(self.settings.black)
        # draw ship
        self.ship.blit_me()
        # display all the  bullet in sprites group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)
        self.scoreboard.show_score()

        if not self.stats.game_active:
            self.play_button.draw_botton()

        pygame.display.flip()

    # chak event
    def _event(self):
        '''
        this fucntion chack any kind of event like key pressed or key up and 
        depanding on the event type it's run functions 
        '''

        # collect all the event in a list
        for event in pygame.event.get():
            # chack if game is cross or not
            if event.type == pygame.QUIT:
                sys.exit()
            # chack any event is keydonw or not
            elif event.type == pygame.KEYDOWN:

                self.key_down(event)
                self.fire_bullets(event)

            elif event.type == pygame.KEYUP:
                self.key_up(event)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.click_play(mouse_pos)

    def update_bullets(self):
        '''
        chack the bullet activaties like move it and if it hit the top of the screen 
        then remove the bullet ,chack the it cullidite with the  buttom  

        '''

        self.bullets.update()
        for Bullet in self.bullets.copy():
            if Bullet.rect.bottom < 0:
                self.bullets.remove(Bullet)
        self.collision_and_new_alian()

    def key_up(self, event):
        """ chack the key up event """
        if event.key == pygame.K_a:
            self.ship.left = False

        elif event.key == pygame.K_d:
            self.ship.right = False

    def key_down(self, event):
        """ chack the key down event"""
        if event.key == pygame.K_a:
            self.ship.left = True

        elif event.key == pygame.K_d:
            self.ship.right = True

    def fire_bullets(self, event):
        """this function handle bullet movement and maintain bullet limite """
        if event.key == pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullet_limit:
                fire = mixer.Sound("music/gun_sound_1.mp3")
                fire.play()
                new_bullets = Bullet(self)
                self.bullets.add(new_bullets)

    def create_fleet(self):
        """ create alian fleet and chack the cullsion adjust the alian positon
        create row and collom of the alian 


        """

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avilable_space_x = self.settings.width - (2*alien_width)
        number_of_alian = avilable_space_x//(2*alien_width)
        Ship_height = self.ship.rect.height
        avilable_space_y = self.settings.height - \
            (3 * alien_height) - Ship_height
        number_row = avilable_space_y // (2*alien_height)

        for row_number in range(number_row-5):
            for alien in range(number_of_alian+4):
                self.row(alien, alien_width, row_number)

    def row(self, alien, alien_width, row_number):
        '''create a row of alian '''
        new_alien = Alien(self)
        alien_width, alien_height = new_alien.rect.size
        new_alien.rect.x = alien_width+2 * alien_width * alien
        new_alien.rect.y = new_alien.rect.height + 2*alien_height * row_number
        self.alien.add(new_alien)

    def update_alien(self):
        self.chk_fleet_edgs()
        self.alien.update()
        if pygame.sprite.spritecollideany(self.ship, self.alien):
            self.ship_hit()
        self.chack_alian_bottom()


# chak move metnt

    def chk_fleet_edgs(self):
        for alien in self.alien.sprites():
            if alien.chack_edgs():
                self.change_direction()
                break

    def change_direction(self):
        for alien in self.alien.sprites():
            alien.rect.y += self.settings.fleet_drop
        self.settings.fleet_direction *= -1

    def collision_and_new_alian(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.alien, True, True)

        if collisions:
            explosion = mixer.Sound("music/gun_sound_2.mp3")
            explosion.play()
            self.stats.score += self.settings.alian_point
            self.scoreboard._prep_score()
            self.scoreboard._prep_ships()
        if not self.alien:
            self.bullets.empty()
            self.create_fleet()
            self.settings.level_up()

    def ship_hit(self):
        """ handel ship hit  with alian  reduce life of the ship , reduce the ship """

        if self.settings.ship_limit > 0:
            self.settings.ship_limit -= 1
            self.scoreboard._prep_ships()

            self.alien.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def chack_alian_bottom(self):
        for alien in self.alien.sprites():
            if alien.rect.bottom > self.rect.bottom:
                self.ship_hit()
                break

    def click_play(self, mouse_pos):
        botton_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if botton_clicked and self.play_button.rect.collidepoint(mouse_pos):
            pygame.mouse.set_visible(False)
            self.settings.initialize_dynamic_setting()
            self.stats.reset_state()
            self.stats.game_active = True
            self.alien.empty()
            self.bullets.empty()
            self.create_fleet()
            self.ship.center_ship()


if __name__ == '__main__':
    A = Game()
    A.main()
