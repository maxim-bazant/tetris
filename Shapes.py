from settings import *
import pygame


class DotShape(object):
    def __init__(self, color):
        self.color = color
        self.edge = 1
        self.grid = [[self.color, "0", "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self):
        pass


class TwoSquareShape(object):
    def __init__(self, color):
        self.color = color
        self.edge = 1
        self.grid = [[self.color, "0", "0", "0"],
                     [self.color, "0", "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self):
        pass


class FourSquareShape(object):
    def __init__(self, color):
        self.color = color
        self.edge = 2
        self.grid = [[self.color, self.color, "0", "0"],
                     [self.color, self.color, "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self):
        pass


class ZShape(object):
    def __init__(self, color):
        self.color = color
        self.edge = 3
        self.grid = [["0", self.color, self.color, "0"],
                     [self.color, self.color, "0", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self):
        pass


class WShape(object):
    def __init__(self, color):
        self.color = color
        self.edge = 3
        self.grid = [["0", self.color, "0", "0"],
                     [self.color, self.color, self.color, "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self):
        pass


class LShape(object):
    def __init__(self, color):
        self.color = color
        self.edge = 3
        self.grid = [[self.color, "0", "0", "0"],
                     [self.color, self.color, self.color, "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]

    def rotate(self):
        pass


class IShape(object):
    def __init__(self, color):
        self.color = color
        self.edge = 1
        self.grid = [[self.color, "0", "0", "0"],
                     [self.color, "0", "0", "0"],
                     [self.color, "0", "0", "0"],
                     [self.color, "0", "0", "0"]]

    def rotate(self):
        pass







