from game.casting.food import Food
import constants

class Obstacle(Food):
    """A damaging obstacle. The evil twin of Food.
    
    The responsibility of Obstacle is to select a random position and points that it lowers.
    
    Attributes:
        _points (int): The amount of points the player loses upon colliding with the obstacle.
    """

    def __init__(self):
        super().__init__()
        self._points = -5
        self._color = constants.WHITE
        self._text = 'O'

    def change_color(self, color):
        """Changes the color of the obstacle. Currently unused, but could be a feature.
        
        Args:
            color (RGB value): A color from the constants file.
        """
        self._color = color