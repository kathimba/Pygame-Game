# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:17:06 2024

@author: USER
"""

import pygame
from pygame import mixer
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    #Initialize pygamem settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #make the play button
    play_button = Button(ai_settings, screen, "PLAY")

    #create an instance to store game statistics and create scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    #make a ship, bullets and alien group
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #background music
    mixer.music.load('C:/Users/USER/GAME_PROJECT/sounds/backtrack.wav')
    mixer.music.play()
    


    


    #start the main loop for the game
    while True:
         
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
                        aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()