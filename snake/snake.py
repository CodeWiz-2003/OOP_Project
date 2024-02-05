import pygame

class snake:
    """
    The snake class represents the snake in the game.

    Attributes:
    -----------
    __screen : pygame.Surface
        The main screen surface where the snake is displayed.
    __block_size : int
        The size of each block of the snake.
    positions : list
        A list of positions of the blocks of the snake. Each position is represented as a list of two integers.
    direction : str
        The current direction of the snake. It can be 'right', 'left', 'up', or 'down'.
    """
    def __init__(self, screen, block_size):

        self.__screen = screen
        self.__block_size = block_size
        self.positions = [[500,500],[490,500],[480,500]]
        self.direction = 'right'

    def update(self):
        """
        Updates the position of the snake based on its current direction.
        If the snake hits itself, it returns False. Otherwise, it returns True.
        """
        head = self.positions[0].copy()
        if self.direction == 'right':
            head[0] += self.__block_size
        if self.direction == 'left':
            head[0] -= self.__block_size
        if self.direction == 'up':
            head[1] -= self.__block_size
        if self.direction == 'down':
            head[1] += self.__block_size
        for position in self.positions[:-1]:
            if head[0] == position[0] and head[1] == position[1]:
                return False
            
        self.positions.insert(0, head)
        self.positions.pop()
        return True

    def add_block(self, position):
        """
        Adds a new block to the snake at the given position.
        """
        self.positions.insert(0, position)

    def draw(self):
        """
        Draws the snake on the screen.
        """
        for position in self.positions:
            pygame.draw.rect(self.__screen, (0,255,0), (*position, self.__block_size, self.__block_size))
