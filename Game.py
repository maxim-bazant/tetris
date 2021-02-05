import pygame
from settings import *
from Grid import Grid
from Square import Square
from Shape import Shape


class Game(object):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.edge = pygame.image.load("images/bg.png").convert_alpha()
        self.win = win
        self.squares = []  # squares that can nt move anymore
        self.movable_squares = []
        self.x_index = 3
        self.y_index = 0
        self.start_x_index = 3
        self.start_y_index = 0
        self.falling_count = 0
        self.grid = Grid()
        self.shapes = [Shape()]
        self.button_down = False
        self.moving_right = False
        self.moving_left = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.blit()

        if not self.movable_squares:
            self.add_shape()

        self.movable_squares = []
        for double in self.grid.return_grid()[0]:
            self.squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))
        for double in self.grid.return_grid()[1]:
            self.movable_squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))

        keys = pygame.key.get_pressed()
        ok = True

        self.move(keys, ok)

        self.falling_count += 1
        if self.falling_count % 100 == 0:  # falling count is for the pieces to slowly go down
            self.fall_down(ok)

    def add_shape(self):
        self.y_index = self.start_y_index
        for row in self.shapes[0].grid:
            self.x_index = self.start_x_index
            for char in row:
                if char == "a":
                    self.grid.grid[self.y_index][self.x_index] = char
                    self.x_index += 1
                else:
                    self.x_index += 1
            self.y_index += 1

    def fall_down(self, ok):
        for double_ in reversed(self.grid.return_grid()[1]):
            if self.grid.grid[double_[1] + 1][double_[0]] != "1" and double_[1] != 19:
                pass
            else:
                ok = False

        for double_ in reversed(self.grid.return_grid()[1]):
            if ok:
                self.grid.grid[double_[1]][double_[0]] = "0"
                self.grid.grid[double_[1] + 1][double_[0]] = "a"
            else:
                for double in self.grid.return_grid()[1]:
                    self.grid.grid[double[1]][double[0]] = "1"

    def move(self, keys, ok):
        # button down handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.button_down = True
            elif event.type == pygame.KEYUP:
                self.button_down = False
            if event.type == pygame.QUIT:
                self.running = False

        if self.moving_right or self.moving_left:
            self.button_down = True

        # movement handling
        if keys[pygame.K_RIGHT] and not self.button_down and not self.moving_left:
            self.moving_right = True
            for double_ in reversed(self.grid.return_grid()[1]):
                if ok:
                    self.grid.grid[double_[1]][double_[0]] = "0"
                    self.grid.grid[double_[1]][double_[0] + 1] = "a"
                else:
                    for double in self.grid.return_grid()[1]:
                        self.grid.grid[double[1]][double[0]] = "1"
        else:
            self.moving_right = False

        if keys[pygame.K_LEFT] and not self.button_down and not self.moving_right:
            self.moving_left = True
            for double_ in self.grid.return_grid()[1]:
                if ok:
                    self.grid.grid[double_[1]][double_[0]] = "0"
                    self.grid.grid[double_[1]][double_[0] - 1] = "a"
                else:
                    for double in self.grid.return_grid()[1]:
                        self.grid.grid[double[1]][double[0]] = "1"
        else:
            self.moving_left = False

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
