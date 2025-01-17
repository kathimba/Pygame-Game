import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in a fleet"""

    def __init__(self, ai_settings, screen):
        """initialize the alien and set its starting position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('C:/Users/USER/GAME_PROJECT/images/alien1.bmp')
        self.rect = self.image.get_rect()

        #start each new alient near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact position
        self.x = float(self.rect.x)


    def blitme(self):
        """draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        """move the alien right or left"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    
    def check_edges(self):
        """return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        


