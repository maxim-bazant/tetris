from settings import *
import pygame


class Shape(object):
    def __init__(self):
        self.grid = [["0", "a", "0", "0"],
                     ["a", "a", "a", "0"],
                     ["0", "0", "0", "0"],
                     ["0", "0", "0", "0"]]
