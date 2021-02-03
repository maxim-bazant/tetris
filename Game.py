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
        self.x_index = 5
        self.y_index = 0
        self.falling_count = 0
        self.grid = Grid()
        self.change_x = 0
        self.change_y = 0

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

        ok = True
        self.falling_count += 1
        if self.falling_count % 100 == 0:  # falling count is for the pieces to slowly go down
            for double_ in reversed(self.grid.return_grid()[1]):
                print(double_[1])
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

    def add_shape(self):
        pass

    def blit(self):
        win.fill(bg_color)
        win.blit(self.edge, (0, 0))
        for movable_square in self.movable_squares:
            movable_square.blit_square()
        for square in self.squares:
            square.blit_square()


g = Game()

while g.running:
    g.events()
    g.run()

    g.clock.tick(FPS)
    pygame.display.update()

