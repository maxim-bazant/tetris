from settings import *
import pygame


class DotShape(object):
    def __init__(self, color):
        self.edge_shift = 0
        self.color = color
        self.width = 1
        self.height = 3
        self.grid = [[self.color, "0", "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self, rotate_count):
        pass


class TwoSquareShape(object):
    def __init__(self, color):
        self.edge_shift = 1
        self.shift = 0
        self.color = color
        self.width = 1
        self.height = 2
        self.grid = [[self.color, "0", "0", "0"],
                     [self.color, "0", "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self, rotate_count):
        if rotate_count % 2 == 1:
            self.width = 2
            self.height = 3
            return [[self.color, self.color, "0", "0"],
                    ["0", "0", "0", "0"],
                    ["0", "0", "0", "0"],
                    ["0", "0", "0", "0"]]
        if rotate_count % 2 == 0:
            self.width = 1
            self.height = 2
            return self.grid


class FourSquareShape(object):
    def __init__(self, color):
        self.edge_shift = 0
        self.color = color
        self.width = 2
        self.height = 2
        self.grid = [[self.color, self.color, "0", "0"],
                     [self.color, self.color, "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self, rotate_count):
        pass


class ZShape(object):
    def __init__(self, color):
        self.edge_shift = 0
        self.shift = 0
        self.color = color
        self.width = 3
        self.height = 2
        self.grid = [["0", self.color, self.color, "0"],
                     [self.color, self.color, "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self, rotate_count):
        if rotate_count % 2 == 1:
            self.width = 2
            self.height = 1
            self.shift = 1
            return [[self.color, "0", "0", "0", "0"],
                    [self.color, self.color, "0", "0", "0"],
                    ["0", self.color, "0", "0", "0"],
                    ["0", "0", "0", "0", "0"]]
        if rotate_count % 2 == 0:
            self.shift = 0
            self.width = 3
            self.height = 2
            return self.grid


class WShape(object):
    def __init__(self, color):
        self.edge_shift = 0
        self.shift = 0
        self.color = color
        self.width = 3
        self.height = 2
        self.grid = [["0", self.color, "0", "0"],
                     [self.color, self.color, self.color, "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self, rotate_count):
        if rotate_count % 4 == 1:
            self.width = 2
            self.height = 1
            self.shift = 1
            return [[self.color, "0", "0", "0"],
                    [self.color, self.color, "0", "0"],
                    [self.color, "0", "0", "0"],
                    ["0", "0", "0", "0"]]
        elif rotate_count % 4 == 2:
            self.shift = 0
            self.width = 3
            self.height = 2
            return [[self.color, self.color, self.color, "0"],
                    ["0", self.color, "0", "0"],
                    ["0", "0", "0", "0"],
                    ["0", "0", "0", "0"]]
        elif rotate_count % 4 == 3:
            self.width = 2
            self.height = 1
            self.shift = 0
            return [["0", self.color, "0", "0"],
                    [self.color, self.color, "0", "0"],
                    ["0", self.color, "0", "0"],
                    ["0", "0", "0", "0"]]
        elif rotate_count % 4 == 0:
            self.shift = 1
            self.width = 3
            self.height = 2
            return self.grid


class LShape(object):
    def __init__(self, color):
        self.edge_shift = 0
        self.color = color
        self.width = 3
        self.height = 2
        self.grid = [[self.color, "0", "0", "0"],
                     [self.color, self.color, self.color, "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self, rotate_count):
        if rotate_count % 4 == 1:
            self.width = 2
            self.height = 1
            self.shift = 0
            return [[self.color, self.color, "0", "0"],
                    [self.color, "0", "0", "0"],
                    [self.color, "0", "0", "0"],
                    ["0", "0", "0", "0"]]
        elif rotate_count % 4 == 2:
            self.shift = 0
            self.width = 3
            self.height = 2
            return [[self.color, self.color, self.color, "0"],
                    ["0", "0", self.color, "0"],
                    ["0", "0", "0", "0"],
                    ["0", "0", "0", "0"]]
        elif rotate_count % 4 == 3:
            self.width = 2
            self.height = 1
            self.shift = 0
            return [["0", self.color, "0", "0"],
                    ["0", self.color, "0", "0"],
                    [self.color, self.color, "0", "0"],
                    ["0", "0", "0", "0"]]
        elif rotate_count % 4 == 0:
            self.shift = 1
            self.width = 3
            self.height = 2
            return self.grid


class IShape(object):
    def __init__(self, color):
        self.edge_shift = 1
        self.shift = 0
        self.color = color
        self.width = 4
        self.height = 3
        self.grid = [[self.color, self.color, self.color, self.color],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self, rotate_count):
        if rotate_count % 2 == 1:
            self.width = 1
            self.height = 0
            return [[self.color, "0", "0", "0"],
                    [self.color, "0", "0", "0"],
                    [self.color, "0", "0", "0"],
                    [self.color, "0", "0", "0"]]
        if rotate_count % 2 == 0:
            self.width = 4
            self.height = 3
            return self.grid







