import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
        _grow_counter (int): 
        _powerup_counter (int):
        _powered_up (boolean):
        _winner (string): Wiiner message.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._grow_counter = 0
        self._powerup_counter = 0
        self._powered_up = False
        self._winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        powerup = cast.get_first_actor("powerups")
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")

        if not self._is_game_over:

            if self._powered_up == True:
                powerup.change_color(constants.BLACK)
                self._powerup_timer()
                if self._powerup_timer() == True:
                    self._powered_up = False
                    powerup.change_color(constants.ORANGE)
                    self._change_segment_color(player1, constants.RED)
                    self._change_segment_color(player2, constants.GREEN)
                    powerup.reset()
            
            self._handle_food_collision(cast)
            self._handle_obstacle_collision(cast)
            self._handle_powerup_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            # self._increase_scores(cast)
            # self._grow_snake(cast)
            

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_1_score = cast.get_first_actor("score1")
        player_2_score = cast.get_first_actor("score2")
        foods = cast.get_actors('foods')


        player1 = cast.get_first_actor("player1")
        player2 = cast.get_second_actor("player2")
        head1 = player1.get_head()
        head2 = player2.get_head()
        for food in foods:            
                if head1.get_position().equals(food.get_position()):
                    points = food.get_points()
                    #grow tail 1 by 1
                    player1.grow_tail(1)
                    player_1_score.add_points_to_player_1(points)
                    if player_1_score.get_points_player_1() == constants.WINNING_POINTS:
                        self._is_game_over = True
                        self._winner = "Congratulations!! Player 1 Wins!"
                    food.reset()
                if head2.get_position().equals(food.get_position()):
                    points = food.get_points()
                    #grow tail 1 by 1
                    player2.grow_tail(1)
                    player_2_score.add_points_to_player_2(points)
                    if player_2_score.get_points_player_2() == constants.WINNING_POINTS:
                        self._is_game_over = True
                        self._winner = "Congratulations!! Player 2 Wins!"
                    food.reset()

    def _handle_obstacle_collision(self, cast):
        """Updates the score and changes the obstacle color if the snake collides with the obstacle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_1_score = cast.get_first_actor("score1")
        player_2_score = cast.get_first_actor("score2")
        obstacle_list = cast.get_actors("obstacles")

        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        head1 = player1.get_head()
        head2 = player2.get_head()

        for obstacle in obstacle_list:
            if self._p1_invuln_on(self._powered_up) == False:
                if head1.get_position().equals(obstacle.get_position()):
                    points = obstacle.get_points()
                    player1.lose_tail()
                    player_1_score.add_points_to_player_1(points)
            if self._p2_invuln_on(self._powered_up) == False:
                if head2.get_position().equals(obstacle.get_position()):
                    points = obstacle.get_points()
                    player2.lose_tail()
                    player_2_score.add_points_to_player_2(points)


    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player_1_score = cast.get_first_actor("player1")
        player_2_score = cast.get_second_actor("player2")
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")

        head = player_1_score.get_segments()[0]
        segments = player_1_score.get_segments()[1:]

        head1 = player_2_score.get_segments()[0]
        segments1 = player_2_score.get_segments()[1:]

#4. Food is worth +5 points, collision is -10 points (can be changed later if needed)
#7. Eating food increases tail size, collision decreases tail size
        if self._p1_invuln_on(self._powered_up) == False:
            for segment in segments:
                # if head.get_position().equals(segment.get_position()):
                #     player1.lose_tail()
            #     score1.lose_points()
                if head1.get_position().equals(segment.get_position()):
                    player_2_score.lose_tail()
                    score2.lose_points1()
                

        if self._p2_invuln_on(self._powered_up) == False:        
            for segment1 in segments1:
                # if head1.get_position().equals(segment1.get_position()):
                #     player2.lose_tail()
            #     score2.lose_points1()
                if head.get_position().equals(segment1.get_position()):
                    player_1_score.lose_tail()
                    score1.lose_points()

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("player1")
            segments = player1.get_segments()

            player2 = cast.get_first_actor("player2")
            segments1 = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(self._winner)
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)

            for segment1 in segments1:
                segment1.set_color(constants.WHITE)

    
        
    def _handle_powerup_collision(self, cast):
        """If the snake collides with a powerup, enables it.
        
        Args:
            cast (Cast): The cast of Actors in the game.

        Returns:

        """
        player1 = cast.get_first_actor("player1")
        powerup = cast.get_first_actor("powerups")
        player2 = cast.get_first_actor("player2")
        head1 = player1.get_head()
        head2 = player2.get_head()

        if head1.get_position().equals(powerup.get_position()):
            self._powered_up = True
            self._change_segment_color(player1, constants.WHITE)
            self._p1_invuln_on(self._powered_up)

        if head2.get_position().equals(powerup.get_position()):
            self._powered_up = True
            self._change_segment_color(player2, constants.WHITE)
            self._p2_invuln_on(self._powered_up)


    def _powerup_timer(self):
        """Times the powerup for 500 cycles.
        
        Returns:
            is_done (bool): Whether or not the timer has completed. True if it is done, false if not.
        """
        self._powerup_counter += 1
        if self._powerup_counter < 500:
            is_done = False
        else:
            self._powerup_counter = 0
            is_done = True

        return is_done

    def _p1_invuln_on(self, powered):
        """Enables the p1 invulnerable powerup.
        
        Args:
            powered (boolean)
            
        Returns:
            enabled (bool): Whether or not the power up is enabled."""
        if powered == True: 
            return True 
        else: 
            return False

    def _p2_invuln_on(self, powered):
        """Enables the p2 invulnerable powerup.
        
        Args:
            powered (boolean)
            
        Returns:
            enabled (bool): Whether or not the power up is enabled."""
        if powered == True: 
            return True 
        else: 
            return False

    def _change_segment_color(self, player, color):
        """Changes the color of the given player's snake segments.

         Args:
            player (Actor): Player 1 or Player 2.
            color (RGB value): A color from the Constants file.
        """
        segments = player.get_segments()
        for segment in segments:
            if segment is not segments[0]:
                segment.set_color(color) 
