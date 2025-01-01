import constants
import random
from game.casting.cast import Cast
from game.scripting.script import Script
from game.scripting.control_player1_action import ControlPlayer1Action
from game.scripting.control_player2_action import ControlPlayer2Action
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.player1 import Player1
from game.casting.player2 import Player2
from game.casting.score import Score
from game.casting.food import Food
from game.casting.powerup import PowerUp
from game.casting.obstacle import Obstacle



def main():

    # create the cast
    cast = Cast()
    

    cast.add_actor("player1", Player1())
    cast.add_actor("player2", Player2())
    cast.add_actor("score1", Score())
    cast.add_actor("score2", Score())
    cast.add_actor("powerups", PowerUp())




    for n in range(constants.AMOUNT_OF_FOOD):

        food_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', ']']
        food1 = random.choice(food_list)

        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        # x = x * constants.CELL_SIZE
        # y = y * constants.CELL_SIZE
        position = Point(x, y)
        print(f"{position.get_x()}, {position.get_y()}")
        # print(position.get_x)

        position = position.scale(constants.CELL_SIZE)
        print(f"{position.get_x()}, {position.get_y()}")
        # r = random.randint(0, 255)wwa
        # g = random.randint(0, 255)
        # b = random.randint(0, 255)
        color = Color(255, 255, 0)

        food = Food()
        food.set_text(food1)
        food.set_font_size(constants.FONT_SIZE)
        food.set_position(position)

        food.set_color(color)
        cast.add_actor("foods", food)

    for n in range(constants.AMOUNT_OF_OBSTACLES):

        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        o_position = Point(x, y)
        o_position = o_position.scale(constants.CELL_SIZE)

        obstacle = Obstacle()
        obstacle.set_text(obstacle._text)
        obstacle.set_font_size(constants.FONT_SIZE)
        obstacle.set_position(o_position)

        obstacle.set_color(obstacle._color)
        cast.add_actor("obstacles", obstacle)

        
        
    # for n in range(constants.AMOUNT_OF_FOOD):

    #     x = random.randint(1, constants.COLUMNS - 1)
    #     y = random.randint(1, constants.ROWS - 1)
    #     position = Point(x, y)
    #     position = position.scale(constants.CELL_SIZE)

    #     r = random.randint(30, 255)
    #     g = random.randint(30, 255)
    #     b = random.randint(30, 255)
    #     while r <= 50 and g <= 50 and b <= 50:
    #         r = random.randint(30, 255)
    #         g = random.randint(30, 255)
    #         b = random.randint(30, 255)

    #     color = Color(r, g, b)
    #     radius = 20
        
    #     # THE FOOD
    #     food = Player1()
    #     food.set_color(color)
    #     food.set_position(position)
    #     food.set_radius(radius)
    #     cast.add_actor("foods", food)
    #     food = Player2()
    #     food.set_color(color)
    #     food.set_position(position)
    #     food.set_radius(radius)
    #     cast.add_actor("foods", food)


    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlPlayer1Action(keyboard_service))
    script.add_action("input", ControlPlayer2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()