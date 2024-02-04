from game_scene import game_scene
from snake import snake
import pygame
import random
class snake_scene(game_scene):
    """
    The snake_scene class represents the snake game scene. It inherits from the game_scene class and implements the draw_scene and update methods.

    Attributes:
    -----------
    screen : pygame.Surface
        The main screen surface where the game is displayed.
    block_size : int
        The size of each block of the snake.
    snake : Snake
        The snake object.
    font : pygame.font.Font
        The font used to render the text.
    game_over : bool
        A flag indicating whether the game is over.
    apple_location : list
        The location of the apple. It is represented as a list of two integers.
    score : int
        The current score of the game.
    running : bool
        A flag indicating whether the game is running.
    """

    def __init__(self, screen):
        self.screen = screen
        self.block_size = 10
        self.snake = snake(self.screen, self.block_size)
        self.font = pygame.font.Font('freesansbold.ttf', 23)
        self.game_over = False
        self.apple_location = [900,900]
        self.score = 0
        self.running = True

    def update(self):
        """
        Gets the user input, updates the snake and the apple, and returns the running and game_over flags.
        """
        self.__get_input()
        self.game_over = not self.snake.update()
        if self.snake.positions[0][0] == self.apple_location[0] and self.snake.positions[0][1] == self.apple_location[1]:
            self.score += 1
            self.snake.addBlock(self.apple_location)
            while(self.apple_location in self.snake.positions):
                self.apple_location = [random.randint(self.block_size + 10,self.block_size*10 - 10)*self.block_size, random.randint(self.block_size + 10,self.block_size*10 - 10)*self.block_size]
        self.game_over = self.snake.positions[0][0] < 0 or \
            self.snake.positions[0][0] > 1000 or \
            self.snake.positions[0][1] < 0 or \
            self.snake.positions[0][1] > 1000
            
        return self.running, self.game_over

    def draw_scene(self):
        """
        Draws the snake scene. It displays the snake, the apple, and the score.
        """
        self.snake.draw()
        self.__draw_apple()
        self.__display_score()

    def __draw_apple(self):
        """
        Draws the apple on the screen.
        """
        pygame.draw.rect(self.screen, (255,0,0), (*self.apple_location, self.block_size, self.block_size))

    def __display_score(self):
        """
        Displays the current score.
        """
        #display score
        score = self.font.render('Score:' + str(self.score), True, (255,255,255), (0,0,0))
        scoreRect = score.get_rect()
        scoreRect.center = (50,30)
        self.screen.blit(score, scoreRect)

    def __get_input(self):
        """
        Gets the user input. If the user presses the arrow keys, it changes the direction of the snake. If the user presses the escape key or closes the window, it stops the game.
        """
        #get all the events
        for event in pygame.event.get():
            #if the event is quit, quit the game
            if event.type == pygame.QUIT:
                self.running = False
            #Get the keypresses and assign the directions
            if not self.game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d and self.snake.direction != 'left':
                        self.snake.direction = 'right'
                    if event.key == pygame.K_a and self.snake.direction != 'right':
                        self.snake.direction = 'left'
                    if event.key == pygame.K_s and self.snake.direction != 'up':
                        self.snake.direction = 'down'                       	 
                    if event.key == pygame.K_w and self.snake.direction != 'down':
                        self.snake.direction = 'up'
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
