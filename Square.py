from settings import *
import pygame


class Square(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/red_square.png").convert_alpha()
        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def blit_square(self):
        win.blit(self.image, (self.x, self.y))
