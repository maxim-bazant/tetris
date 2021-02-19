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
        self.full_line_list = []

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
        self.full_line_list = []
        self.line_full = False
        for row in reversed(range(len(self.grid) - 1)):
            if "0" not in self.grid[row]:
                self.line_full = True
                print(f"line {row} is full")
                self.full_line_list.append(row)

                for number in range(len(self.grid[row]) - 1):
                    self.grid[row][number] = "0"
                self.grid[row][-1] = "n"

        if self.line_full:
            self.shift_down(self.full_line_list)
            return True

    def shift_down(self, line_list):
        for i in reversed(range(len(line_list))):
            for row in reversed(range(0, line_list[i])):
                for char in range(len(self.grid[row]) - 1):
                    self.grid[row + 1][char] = self.grid[row][char]

            for i in range(len(self.grid[0]) - 1):
                self.grid[0][i] = "0"
            self.grid[0][-1] = "n"
            for i in range(len(self.grid[-1]) - 1):
                self.grid[-1][i] = "0"
            self.grid[-1][-1] = "n"

