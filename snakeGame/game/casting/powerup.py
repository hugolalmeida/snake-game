import random
import constants
from game.shared.point import Point
from game.casting.actor import Actor

class PowerUp(Actor):
    """A unique power-up to keep the game interesting.
    
    PowerUps enable one player to become stronger for a short time."""

    def __init__(self):
        """Constructs a new instance of PowerUp.
        
        Attributes:
            Atts go here"""
        super().__init__()
        self.set_text('P')
        self.set_color(constants.ORANGE)
        self.is_on = False
        self.reset()

    def reset(self):
        """Selects a random position for the powerup.
        
        Args:
            Args go here
            
        Returns:
            Return goes here lol"""
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)

    def invulnerable(self):
        """The invulnerable powerup disables collision with the other snake. A method meant to keep track of a powerup that exists."""
        
        pass

    def change_color(self, color):
        """Changes the powerup's color to black to make it invisible."""

        self.set_color(color)