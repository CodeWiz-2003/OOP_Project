from game_scene import game_scene
import pygame
class game_over_scene(game_scene):
    """
    The game_over_scene class represents the game over scene. It displays the game over message and the final score.

    Attributes:
    -----------
    screen : pygame.Surface
        The main screen surface where the game over scene is displayed.
    score : int
        The final score of the game.
    font : pygame.font.Font
        The font used to render the text.
    running : bool
        A flag indicating whether the game is running.
    game_over : bool
        A flag indicating whether the game is over.
    """
    def __init__(self, screen):
        """
        Initializes the game over scene with the given screen.
        """
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 23)
        self.running = True
        self.game_over = True
    def update(self):
        """
        Updates the game over scene. It gets the user input and returns the running and game_over flags.
        """
        self.__get_input()
        return self.running, self.game_over

    def draw_scene(self):
        """
        Draws the game over scene. It displays the score and the game over message.
        """
        self.__display_score()
        self.__display_game_over()

    def __display_score(self):
        """
        Displays the final score.
        """
        #display score
        score = self.font.render('Score:' + str(self.score), True, (255,255,255), (0,0,0))
        score_rect = score.get_rect()
        score_rect.center = (500,500)
        self.screen.blit(score, score_rect)

    def __display_game_over(self):
        """
        Displays the game over message.
        """
        #display game over
        game_over = self.font.render('Game Over', True, (255,255,255), (0,0,0))
        game_over_rect = game_over.get_rect()
        game_over_rect.center = (500,550)

        anyKey = self.font.render('Press any key to restart', True, (255,255,255), (0,0,0))
        any_key_rect = anyKey.get_rect()
        any_key_rect.center = (500,600)
        self.screen.blit(game_over, game_over_rect)
        self.screen.blit(anyKey, any_key_rect)

    def __get_input(self):
        """
        Gets the user input. If the user quits the game or presses the escape key, it stops the game. If the user presses any other key, it restarts the game.
        """
        #get all the events
        for event in pygame.event.get():
            #if the event is quit, quit the game
            if event.type == pygame.QUIT:
                self.running = False
            #Get the keypresses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                else:
                    self.game_over = False
