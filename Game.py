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
        self.falling_count = 0
        self.grid = Grid()
        self.change_x = 0
        self.change_y = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        self.squares = []
        for double in self.grid.return_grid():
            self.squares.append(Square((double[0] + 1) * 40, (double[1] + 1) * 40))

        self.blit()

        self.falling_count += 1
        if self.falling_count % 100 == 0:  # falling count is for the pieces to slowly go down
            for square in reversed(self.squares):
                self.change_x = square.x // 40 - 1
                self.change_y = square.y // 40 - 1
                self.grid.grid[self.change_y][self.change_x] = "0"
                self.grid.grid[self.change_y + 1][self.change_x] = "1"

    def blit(self):
        win.fill(bg_color)
        win.blit(self.edge, (0, 0))
        for square in self.squares:
            square.blit_square()


g = Game()

while g.running:
    g.events()
    g.run()

    g.clock.tick(FPS)
    pygame.display.update()

