import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Player2(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _segments(array): The length of the snake's body part per part.
        _prepare_body()(function): Construct the snake's body add all parts of the snake.
    """
    def __init__(self):
        """Constructs a new Actor."""
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """ Get the segments of snake's body.
        
        Returns:
            Array: The list of segments.
        """
        return self._segments

    def move_next(self):
        """Move all segments and update velocities"""
        #move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Get the snake's head.
        
        Returns:
            Array: The first element on the list.
        """
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """Add a new segment to make the tail grow
        
            Args:
                number_of_segments(int): Segment's length.
        """
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.GREEN)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """Turn the snake's head.
        
            Args:
                velocity(float): Move speed.
        """
        self._segments[0].set_velocity(velocity)

    #4. Eating food increases tail size, collision decreases tail size
    def lose_tail(self):
        """Lose the last piece of tail
        
        """
        self._segments.pop()
    
    def _prepare_body(self):
        """Contruct the snake's body"""
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)