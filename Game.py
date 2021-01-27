import pygame
from settings import *
from Grid import Grid
from Square import Square


class Game(object):
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.edge = pygame.image.load("images/bg.png").convert_alpha()
        self.win = win
        self.squares = []
        self.x = 0
        self.y = 100
        self.grid = Grid()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        for double in self.grid.draw_grid():
            self.squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))

        self.blit()

    def blit(self):
        win.blit(self.edge, (0, 0))
        for square in self.squares:
            square.blit_square()


g = Game()

while g.running:
    g.events()
    g.run()

    g.clock.tick(FPS)
    pygame.display.update()

