import pygame as pygame
class Settings():
    def __init__(self):
        #game window 
        self.height = 1200
        self.width = 800
        self.black= (230,230,230)
        self.bullet_color= (230,0,0)
        #ship 
        self.ship_height = 120
        self.ship_width = 120
        self.ship_limit = 3 
        #bullet 
        self.bullet_height= 20
        self.bullet_width = 10
        self.bullet_holder =[]
        self.fleet_drop= 100
        #botton 
        self.botton_width= 200
        self.botton_height= 50 
        self.botton_color = (0,255,0)
        self.botton_textc =(255,255,255)
        self.bullet_limit= 4
        self.spree_up = 1
        self.alian_point = 50

        self.initialize_dynamic_setting()


        # self.display = "Alian invator "
    def initialize_dynamic_setting(self):
        self.alien_spreed = 1
        self.fleet_direction = 1
        self.ship_spreed= 2
        self.bullet_spreed = 4

    def level_up(self):
        self.alien_spreed += self.spree_up
        self.ship_spreed += self.spree_up
        self.bullet_spreed  += self.spree_up
        





    
        
 