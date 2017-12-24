class Settings():

	def __init__(self):

		# screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# ship settings
		self.ship_limit = 1

		# alien settings
		self.fleet_drop_speed = 30
		

		# bullet settings
		self.bullet_width =3000
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3

		# how qiuckly the game speeds up
		self.speed_up_scale = 1.1

		# how quickly the score inscreases
		self.score_scale = 1.5

	def initialize_dynamic_settings(self):
		# init the setting which will be changed during the game
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 10
		self.alien_speed_factor = 5
		self.alien_points = 50

		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speed_up_scale
		self.bullet_speed_factor *= self.speed_up_scale
		self.alien_speed_factor *= self.speed_up_scale
		self.alien_points = int(self.alien_points * self.score_scale)

		print self.alien_points

