import pygame
import platform
import random
import time
from settings import *
from Grid import Grid
from Square import Square
from Shapes import *

print(platform.uname()[0])


class Game(object):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.edge = pygame.image.load("images/bg.png").convert_alpha()
        self.win = win
        self.squares = []  # squares that can nt move anymore
        self.movable_squares = []
        self.current_x_index = 3
        self.current_y_index = 0
        self.start_x_index = 3
        self.start_y_index = 0
        self.falling_count = 0
        self.grid = Grid()
        self.colors = ["a", "b", "c", "d", "e", "f"]
        self.shapes = [DotShape(self.colors[0]), TwoSquareShape(self.colors[0]), FourSquareShape(self.colors[0]),
                       ZShape(self.colors[0]), WShape(self.colors[0]), LShape(self.colors[0]), IShape(self.colors[0])]
        self.button_down = False
        self.moving_right = False
        self.moving_left = False
        if platform.uname().system == "Linux":
            print("linux")
            self.speed = 20
            self.normal_speed = 20
            self.quick_down_speed = 2
        else:
            self.speed = 50
            self.normal_speed = 50
            self.quick_down_speed = 4
        self.current_shape_index = 0
        self.game_over_ = False
        self.line_full = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.button_down = False
            elif event.type == pygame.KEYUP:
                self.button_down = True
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.blit()

        if not self.movable_squares:
            self.add_shape()

        if self.line_full:  # if line full it changes it into "0" instead of "1"
            self.squares = []

            for double in self.grid.return_squares()[0]:
                self.squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))
            self.line_full = False

        self.movable_squares = []
        for double in self.grid.return_squares()[1]:
            self.movable_squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))

        keys = pygame.key.get_pressed()
        ok_down = True

        self.falling_count += 1
        if self.falling_count % self.speed == 0:  # falling count is for the pieces to slowly go down
            self.fall_down(ok_down)

        ok_right = True
        ok_left = True
        self.move(keys)

    def check_for_full_line(self):
        if self.grid.check_for_line():
            self.line_full = True

    def add_shape(self):
        self.check_for_full_line()

        self.current_shape_index = random.randint(0, len(self.shapes) - 1)
        self.speed = self.normal_speed
        self.falling_count = 0
        self.current_y_index = self.start_y_index
        for row in self.shapes[self.current_shape_index].grid:
            self.current_x_index = self.start_x_index
            for char in row:
                if char == "a":
                    self.grid.grid[self.current_y_index][self.current_x_index] = char
                    self.current_x_index += 1
                else:
                    pass

                    self.current_x_index += 1
            self.current_y_index += 1
        self.current_x_index = self.start_x_index

    def fall_down(self, ok):
        movable_square_list = self.grid.return_squares()[1]
        for double_ in reversed(movable_square_list):
            if self.grid.grid[double_[1] + 1][double_[0]] != "1" and double_[1] != 19:
                pass
            else:
                ok = False

        for double_ in reversed(movable_square_list):
            if ok:
                self.grid.grid[double_[1]][double_[0]] = "0"
                self.grid.grid[double_[1] + 1][double_[0]] = "a"
            else:
                for double in movable_square_list:
                    self.grid.grid[double[1]][double[0]] = "1"
                    self.squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))

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

        movable_squares = self.grid.return_squares()[1]
        for double_ in reversed(movable_squares):
            if self.grid.grid[double_[1]][double_[0] + 1] != "1":
                pass
            else:
                ok_right = False
        for double_ in reversed(movable_squares):
            if self.grid.grid[double_[1]][double_[0] - 1] != "1":
                pass
            else:
                ok_left = False
        # end of control

        if not self.speed == self.quick_down_speed:
            if keys[pygame.K_RIGHT] and not self.button_down and not self.moving_left and ok_right:
                self.moving_right = True
                for double_ in reversed(self.grid.return_squares()[1]):
                    if ok_right:
                        self.grid.grid[double_[1]][double_[0]] = "0"
                        self.grid.grid[double_[1]][double_[0] + 1] = "a"
                    else:
                        for double in self.grid.return_squares()[1]:
                            self.grid.grid[double[1]][double[0]] = "1"
                if ok_right:
                    self.current_x_index += 1
            else:
                self.moving_right = False

            if keys[pygame.K_LEFT] and not self.button_down and not self.moving_right and ok_left:
                self.moving_left = True
                movable_squares = self.grid.return_squares()[1]
                for double_ in movable_squares:
                    if ok_left:
                        self.grid.grid[double_[1]][double_[0]] = "0"
                        self.grid.grid[double_[1]][double_[0] - 1] = "a"
                    else:
                        for double in movable_squares:
                            self.grid.grid[double[1]][double[0]] = "1"
                if ok_left:
                    self.current_x_index -= 1
            else:
                self.moving_left = False

        if keys[pygame.K_DOWN]:
            self.speed = self.quick_down_speed

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


g = Game()

while g.running:
    g.run()
    g.events()

    g.clock.tick(FPS)
    pygame.display.update()
