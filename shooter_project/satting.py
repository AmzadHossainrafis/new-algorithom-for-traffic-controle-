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
        self.ship_spreed= 2
        #bullet 
        self.bullet_height= 20
        self.bullet_width = 10
        self.bullet_spreed = 4
        self.bullet_holder =[]
        self.bullet_limit= 4
        self.alien_spreed = 1
        self.fleet_direction = 1
        self.fleet_drop= 10
        # self.display = "Alian invator "
        
 