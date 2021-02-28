import pygame
import platform
import random
import time
from settings import *
from Grid import Grid
from Square import Square
from Shapes import *


class Game(object):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.edge = pygame.image.load("images/bg.png").convert_alpha()
        self.win = win
        self.squares = []  # squares that can nt move anymore
        self.movable_squares = []
        self.next_shape_squares = []
        self.current_x_index = 3
        self.current_y_index = 0
        self.start_x_index = 3
        self.start_y_index = 0
        self.start_next_shape_x = 0
        self.start_next_shape_y = 0
        self.falling_count = 0
        self.grid = Grid()
        self.colors = ["a", "b", "c", "d"]
        self.numbers = ["1", "2", "3", "4"]
        self.shapes = [DotShape(self.colors[0]), TwoSquareShape(self.colors[0]), FourSquareShape(self.colors[0]),
                       ZShape(self.colors[0]), WShape(self.colors[0]), LShape(self.colors[0]), IShape(self.colors[0])]
        self.button_down = False
        self.moving_right = False
        self.moving_left = False
        if platform.uname().system == "Linux":
            self.speed = 20
            self.normal_speed = 20
            self.quick_down_speed = 2
        else:
            self.speed = 50
            self.normal_speed = 50
            self.quick_down_speed = 4

        self.next_shape_index = [random.randint(0, len(self.shapes) - 1), random.randint(0, len(self.shapes) - 1)]
        self.current_shape_index = 0
        self.game_over_ = False
        self.line_full = False

        self.rotate_count = 0
        self.space_down = False
        self.rotating = False

        self.num_to_char = {"1": "a",
                            "2": "b",
                            "3": "c",
                            "4": "d"}
        self.char_to_num = {"a": "1",
                            "b": "2",
                            "c": "3",
                            "d": "4"}

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.button_down = False
            elif event.type == pygame.KEYUP:
                self.space_down = False
                self.button_down = False
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.blit()

        if self.line_full:  # if line full it changes it into "0" instead of "1"
            self.squares = []

            for double in self.grid.return_squares():
                self.squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))
            self.line_full = False

        self.movable_squares = []
        for double in self.grid.return_movable_squares():
            self.movable_squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))

        keys = pygame.key.get_pressed()
        ok_down = True

        if not self.movable_squares:
            if not self.check_if_game_over():
                self.add_shape()
            else:
                self.game_over()
        else:
            if not self.speed == self.quick_down_speed:
                self.rotate_shape(keys)
                ok_right = True
                ok_left = True
                self.move(keys)

        self.falling_count += 1
        if self.falling_count % self.speed == 0:  # falling count is for the pieces to slowly go down
            self.fall_down(ok_down)

    def check_for_full_line(self):
        if self.grid.check_for_line():
            self.line_full = True

    def rotate_shape(self, keys):
        ok = None
        shape = self.shapes[self.current_shape_index]

        if keys[pygame.K_SPACE] and not self.space_down and shape != self.shapes[0] and shape != self.shapes[2]:
            self.space_down = True

            shape.rotate(self.rotate_count)  # sets the width to correct corresponding number

            # CONTROL IF THE SHAPE CAN ROTATE

            # edge
            if self.current_x_index == 8 + shape.edge_shift:
                ok = False
            else:
                ok = True

            # around the shape check
            for i in range(len(self.movable_squares)):
                current_x_index = self.movable_squares[0].x // 40 - 1
                start_x_index = current_x_index
                current_y_index = self.movable_squares[0].y // 40 - 1

                self.rotate_count += 1

                for row in shape.rotate(self.rotate_count):
                    for char in row:
                        if char != "0":
                            try:
                                if current_y_index != 20:
                                    if ok:
                                        ok = True
                                else:
                                    ok = False

                                if self.current_shape_index != 4 and self.current_shape_index != 5:
                                    if self.grid.grid[current_y_index][current_x_index] != "n":
                                        if ok:
                                            ok = True
                                    else:
                                        ok = False

                                if self.grid.grid[current_y_index][current_x_index] not in self.numbers:
                                    if ok:
                                        ok = True
                                else:
                                    ok = False
                            except IndexError:
                                ok = False

                            current_x_index += 1
                        else:
                            current_x_index += 1
                    current_y_index += 1
                    current_x_index = start_x_index
                self.rotate_count -= 1

            # deleting the previous shape (it has to be replaced with rotated version)
            if ok:
                self.rotate_count += 1
                for i in range(len(self.movable_squares)):
                    current_x_index = self.movable_squares[0].x // 40 - 1
                    start_x_index = current_x_index
                    current_y_index = self.movable_squares[0].y // 40 - 1
                    self.grid.grid[self.movable_squares[i].y // 40 - 1][self.movable_squares[i].x // 40 - 1] = "0"

                    for row in shape.rotate(self.rotate_count):
                        for char in row:
                            if char != "0":
                                self.grid.grid[current_y_index][current_x_index - shape.shift] = char
                                current_x_index += 1
                            else:
                                current_x_index += 1
                        current_y_index += 1
                        current_x_index = start_x_index

        shape.rotate(self.rotate_count)  # sets the width to correct corresponding number

    def update_next_shape_grid(self):
        self.grid.reset_next_shape_grid()

        current_y_index = self.start_next_shape_y
        for row in self.shapes[self.next_shape_index[-1]].grid:
            current_x_index = self.start_next_shape_x
            for char in row:
                if char == self.shapes[self.next_shape_index[-1]].color:
                    self.grid.next_shape_grid[current_y_index][current_x_index] = char
                    current_x_index += 1
                else:
                    current_x_index += 1
            current_y_index += 1
            current_x_index = self.start_next_shape_x

    def add_shape(self):
        self.check_for_full_line()

        if len(self.next_shape_index) == 1:
            self.next_shape_index.append(random.randint(0, len(self.shapes) - 1))

        self.next_shape_squares = []
        self.update_next_shape_grid()

        for double in self.grid.return_next_shape_squares():
            self.next_shape_squares.append(Square((double[0] + 15) * 40, (double[1] + 5) * 40))

        self.current_shape_index = self.next_shape_index[0]
        self.next_shape_index.pop(0)

        self.speed = self.normal_speed
        self.falling_count = 0
        self.current_y_index = self.start_y_index
        for row in self.shapes[self.current_shape_index].grid:
            self.current_x_index = self.start_x_index
            for char in row:
                if char == self.shapes[self.current_shape_index].color:
                    self.grid.grid[self.current_y_index][self.current_x_index] = char
                    self.current_x_index += 1
                else:
                    self.current_x_index += 1
            self.current_y_index += 1
            self.current_x_index = self.start_x_index

    def fall_down(self, ok):
        movable_square_list = self.grid.return_movable_squares()
        for double_ in reversed(movable_square_list):
            if self.grid.grid[double_[1] + 1][double_[0]] != self.char_to_num[self.shapes[self.current_shape_index].color] and double_[1] != 19:
                pass
            else:
                ok = False

        for double_ in reversed(movable_square_list):
            if ok:
                self.grid.grid[double_[1]][double_[0]] = "0"
                self.grid.grid[double_[1] + 1][double_[0]] = self.shapes[self.current_shape_index].color
            else:
                for double in movable_square_list:
                    self.grid.grid[double[1]][double[0]] = self.char_to_num[self.shapes[self.current_shape_index].color]
                    self.squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))

                self.rotate_count = 0

                # here - shape is down and new is being added. Time for full_line_check()

    def move(self, keys):
        # button down handling
        if self.moving_right or self.moving_left:
            self.button_down = True

        # movement handling
        # control
        if self.current_x_index < 10 - self.shapes[self.current_shape_index].width:
            ok_right = True
        else:
            ok_right = False
        if self.current_x_index > 0:
            ok_left = True
        else:
            ok_left = False

        movable_squares = self.grid.return_movable_squares()
        for double_ in reversed(movable_squares):
            if self.grid.grid[double_[1]][double_[0] + 1] not in self.numbers:
                pass
            else:
                ok_right = False
        for double_ in reversed(movable_squares):
            if self.grid.grid[double_[1]][double_[0] - 1] not in self.numbers:
                pass
            else:
                ok_left = False
        # end of control
        if keys[pygame.K_RIGHT] and not self.button_down and not self.moving_left and ok_right:
            self.moving_right = True
            for double_ in reversed(self.grid.return_movable_squares()):
                if ok_right:
                    self.grid.grid[double_[1]][double_[0]] = "0"
                    self.grid.grid[double_[1]][double_[0] + 1] = self.shapes[self.current_shape_index].color
                else:
                    for double in self.grid.return_movable_squares():
                        self.grid.grid[double[1]][double[0]] = self.char_to_num[self.shapes[self.current_shape_index].color]
            if ok_right:
                self.current_x_index += 1
        else:
            self.moving_right = False

        if keys[pygame.K_LEFT] and not self.button_down and not self.moving_right and ok_left:
            self.moving_left = True
            movable_squares = self.grid.return_movable_squares()
            for double_ in movable_squares:
                if ok_left:
                    self.grid.grid[double_[1]][double_[0]] = "0"
                    self.grid.grid[double_[1]][double_[0] - 1] = self.shapes[self.current_shape_index].color
                else:
                    for double in movable_squares:
                        self.grid.grid[double[1]][double[0]] = self.char_to_num[self.shapes[self.current_shape_index].color]
            if ok_left:
                self.current_x_index -= 1
        else:
            self.moving_left = False

        if keys[pygame.K_DOWN]:
            self.speed = self.quick_down_speed

    def check_if_game_over(self):
        game_over = None
        for height in range(4 - self.shapes[self.current_shape_index].height):
            for width in range(self.shapes[self.current_shape_index].width):
                if self.grid.grid[self.start_y_index + height][self.start_x_index + width] in self.numbers:
                    game_over = True
                else:
                    if not game_over:
                        game_over = False

        return game_over

    def game_over(self):
        print("game over")
        self.squares = []
        self.movable_squares = []
        time.sleep(2)
        self.game_over_ = False
        self.grid.reset_grid()

    def blit(self):
        win.fill(bg_color)
        win.blit(self.edge, (0, 0))
        for movable_square in self.movable_squares:
            movable_square.blit_square()
        for square in self.squares:
            square.blit_square()
        for square in self.next_shape_squares:
            square.blit_square()


g = Game()

while g.running:
    g.run()
    g.events()

    g.clock.tick(FPS)
    pygame.display.update()
