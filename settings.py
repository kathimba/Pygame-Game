import pygame

class Settings():
    def __init__(self):
        """Initialize the game's static settings"""
        #Screen settings
        self.screen_width = 1348
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.background = pygame.image.load('C:/Users/USER/GAME_PROJECT/images/background2.jpg')
        
        #bullet settings
        self.bullet_width = 10
        self.bullet_height = 25
        self.bullet_color = 229, 244, 244
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 3
        
        #ship settings
        self.ship_limit = 3

        #how quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()



    def initialize_dynamic_settings(self):
        """initialize settings that change througout teh game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50


    def increase_speed(self):
         """increase speed settings and alien point values."""
         self.ship_speed_factor *= self.speedup_scale
         self.bullet_speed_factor *= self.speedup_scale
         self.alien_speed_factor *= self.speedup_scale
 
         self.alien_points = int(self.alien_points * self.score_scale)







        
        