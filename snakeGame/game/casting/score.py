import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game by player1.
        _points1 (int): The points earned in the game by player2.
        _negative_points (int):
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self._points1 = 0
        self._negative_points = 10
        self.add_points_to_player_1(0)
        self.add_points_to_player_2(0)

    def add_points_to_player_1(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        # rounded_points = round(self._points)
        self.set_text(f"Player 1 Score: {self._points}")

    def add_points_to_player_2(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points1 += points
        # rounded_points = round(self._points1)
        self.set_text(f"Player 2 Score: {self._points1}")
        
    def set_score_2_position(self):
        """Sets the postion of the player 2 score to the right side of the screen.
        
        Args:
            points (int): The points to add.
        """
        x = int(constants.MAX_X - 150)
        y = int(constants.MAX_Y)
        position = Point(x,y)
        
        self.set_position(position)    

    #7. Eating food increases tail size, collision decreases tail size
    def lose_points(self):
        """Player1 loses the given points to the score's total points.
        
        """
        self._points -= self._negative_points

        self.set_text(f"Player 1 Score: {self._points}")
        
    def lose_points1(self):
        """Player2 loses the given points to the score's total points.
        
        """
        self._points1 -= self._negative_points
        
        self.set_text(f"Player 2 Score: {self._points1}")

    def get_points_player_2(self):
        """Returns total points for player 2.

        Return: 
            _points1 (int): points of player 2
        
        """
        return self._points1

    def get_points_player_1(self):
        """Returns total points for player 1.

        Return: 
            _points (int): points of player 1 
        
        """
        return self._points