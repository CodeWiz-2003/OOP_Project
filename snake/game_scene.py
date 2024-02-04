from abc import ABC, abstractmethod

class game_scene(ABC):
    """
    The game_scene class is an abstract base class that represents a game scene.
    It provides the basic structure for different game scenes like the main menu scene,
    the snake game scene, and the game over scene.
    """
    @abstractmethod
    def draw_scene(self):
        """
        An abstract method that should be implemented in the subclasses to draw the game scene.
        """
        pass

    @abstractmethod
    def update(self):
        """
        An abstract method that should be implemented in the subclasses to update the game scene.
        """
        pass
