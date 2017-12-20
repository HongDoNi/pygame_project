import sys
import pygame
from setting import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Allen Invasion")

	ship = Ship(ai_settings, screen)
	alien = Alien(ai_settings, screen)
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	bullets = Group()

	while True:		
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()