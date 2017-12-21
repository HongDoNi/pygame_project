import sys
import pygame
from setting import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Allen Invasion")

	ship = Ship(ai_settings, screen)
	stats = GameStats(ai_settings)

	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	bullets = Group()

	while True:		
		gf.check_events(ai_settings, screen, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
