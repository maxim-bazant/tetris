import pygame
import time
from settings import *


class Grid(object):
    def __init__(self):
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
                     ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "0"]]

        self.square_doubles = []
        self.movable_square = []
        self.line_full = False
        self.latest_row_index = None
        self.last_row_index = None

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

    def reset_grid(self):
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
                     ["n", "n", "n", "n", "n", "n", "n", "n", "n", "n", "0"]]

    def check_for_line(self):
        for row in self.grid:
            if "0" not in row:
                self.line_full = True

                if self.latest_row_index is None:
                    self.latest_row_index = self.grid.index(row)
                self.last_row_index = self.grid.index(row)
                print(self.last_row_index)
                print(f"line {self.grid.index(row)} is full")
                for number in range(len(row) - 1):
                    self.grid[self.grid.index(row)][number] = "0"

                self.shift_down(self.latest_row_index)

        if self.line_full:
            return True

    def shift_down(self, row_index):
        for row in reversed(range(0, row_index)):
            print(row)

