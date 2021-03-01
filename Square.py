from settings import *
import pygame


class Square(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/red_square.png").convert()
        self.images = [pygame.image.load("images/red_square.png").convert(),
                       pygame.image.load("images/blue_square.png").convert(),
                       pygame.image.load("images/green_square.png").convert(),
                       pygame.image.load("images/yellow_square.png").convert()]

        self.width = self.image.get_rect().width
        self.height = self.image.get_rect().height

    def blit_square(self, index):
        win.blit(self.images[index], (self.x, self.y))
