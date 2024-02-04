import pygame
from snake_scene import snake_scene
from game_over_scene import game_over_scene
from main_menu_scene import main_menu_scene
class game:
    """
    The game class represents the main game loop. It initializes the game window,
    manages the game scenes and controls the game flow.

    Attributes:
    -----------
    screen : pygame.Surface
        The main screen surface where the game is displayed.
    clock : pygame.time.Clock
        A clock object that can be used to track the amount of time.
    snake_scene : snake_scene
        The scene for the snake game.
    gameOver : bool
        A flag indicating whether the game is over.
    game_over_scene : game_over_scene
        The scene displayed when the game is over.
    main_menu_scene : main_menu_scene
        The main menu scene.

    Methods:
    --------
    __init__() -> None:
        Initializes pygame, sets the game window and initializes the game scenes.

    run() -> None:
        The main game loop. It controls the game flow and updates the game scenes.
    """
    def __init__(self):
        #initalize pygame and set caption, icon and window size
        pygame.init()
        pygame.display.set_caption("Snake game")
        # logo = pygame.image.load('../snake.png')
        # pygame.display.set_icon(logo)
        self.screen = pygame.display.set_mode((1000,1000))

        #clock initalization
        self.clock = pygame.time.Clock()

        self.snake_scene = snake_scene(self.screen)
        self.gameOver = False
        self.game_over_scene = game_over_scene(self.screen)
        self.main_menu_scene = main_menu_scene(self.screen)

    def run(self):
        """
        The main game loop. It controls the game flow and updates the game scenes.

        The game starts with the main menu scene. When the player starts the game,
        it switches to the snake scene. If the player loses, it switches to the game over scene.
        The player can restart the game from the game over scene.
        """
        running = True
        start = False
        while running:
            if not start:
                running, start = self.main_menu_scene.update()
                self.screen.fill((0,0,0))

                self.main_menu_scene.draw_scene()
                #update display
                pygame.display.update()
                
                #set framerate
                self.clock.tick(60)
            else:
                break
        while running:
            if not self.gameOver:
                running, self.gameOver = self.snake_scene.update()
                if self.gameOver:
                    self.game_over_scene.score = self.snake_scene.score
            else:
                running, self.gameOver = self.game_over_scene.update()
                if not self.gameOver:
                    self.snake_scene = snake_scene(self.screen)
            self.screen.fill((0,0,0))
            if not self.gameOver:
                self.snake_scene.draw_scene()
            else:
                self.game_over_scene.draw_scene()
            #update display
            pygame.display.update()
            
            #set framerate
            self.clock.tick(10)
