import pygame
import time
from control import Control
from Snake_class import Snake
from gui import Gui
from food import Food


pygame.mixer.init()

window = pygame.display.set_mode((441, 441))
pygame.display.set_caption("Snake")
control = Control()
snake = Snake()
gui = Gui()
food = Food()

gui.init_field()
food.get_food_position(gui)
#gui.create_image()

while control.flag_game:
    gui.check_win_lose()
    control.control()



#    head = [x_coord, y_coord]
    window.fill(pygame.Color("Black"))
    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
        gui.draw_indicator(window)
        gui.draw_level(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)



    if control.flag_pause and gui.game == "GAME":
        snake.move(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.check_end_window()
        snake.animation()
    time.sleep(0.1)



    pygame.display.flip()