from game_scene import game_scene
import pygame

class main_menu_scene(game_scene):
	"""
	The main_menu_scene class represents the main menu scene of the game.
	It inherits from the game_scene class and implements the draw_scene and update methods.

	Attributes:
	-----------
	screen : pygame.Surface
		The main screen surface where the game is displayed.
	font : pygame.font.Font
		The font used to render the text.
	running : bool
		A flag indicating whether the game is running.
	start : bool
		A flag indicating whether the game should start.
	"""
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.Font('freesansbold.ttf', 23)
		self.running = True
		self.start = False

	def update(self):   
		"""
		Gets the user input and returns the running and start flags.
		"""
		self.__get_input()
		return self.running, self.start

	def draw_scene(self):
		"""
		Draws the main menu scene. It displays the title and the instructions.
		"""
		self.__display_title()
		self.__display_instructions()

	def __display_title(self):
		"""
		Displays the game title.
		"""
		#display title
		title = self.font.render('Snake Game', True, (255,255,255), (0,0,0))
		title_rect = title.get_rect()
		title_rect.center = (500,500)
		self.screen.blit(title, title_rect)

	def __display_instructions(self):
		"""
		Displays the game instructions.
		"""
		#display instructions
		instructions = self.font.render('Press any key to start', True, (255,255,255), (0,0,0))
		instructions_rect = instructions.get_rect()
		instructions_rect.center = (500,550)
		self.screen.blit(instructions, instructions_rect)

	def __get_input(self):
		"""
		Gets the user input. If the user presses any key, the game starts.
		If the user presses the escape key or closes the window, the game quits.
		"""
		#get all the events
		for event in pygame.event.get():
			#if the event is quit, quit the game
			if event.type == pygame.QUIT:
				self.running = False
			#Get the keypresses and assign the directions
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.running = False
				else:
					self.start = True
