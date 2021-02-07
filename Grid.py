import pygame
from settings import *


class Grid(object):
    def __init__(self):
        self.square = (pygame.image.load(f"images/red_square.png").convert_alpha())

        self.grid = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],  # [y.position][x.position]
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "n"],
                     ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "n"]]

        self.square_doubles = []
        self.movable_square = []

    def return_squares(self):
        self.movable_square = []
        self.square_doubles = []
        for horizontal_number in range(len(self.grid) - 1):
            for vertical_number in range(len(self.grid[horizontal_number]) - 1):
                if self.grid[horizontal_number][vertical_number] == "1":
                    self.square_doubles.append([vertical_number, horizontal_number])
                if self.grid[horizontal_number][vertical_number] == "a":
                    self.movable_square.append([vertical_number, horizontal_number])

        return [self.square_doubles, self.movable_square]

    def shift_down(self):
        pass

