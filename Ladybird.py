import pygame as pg
import random
import os


class Ladybird:
    def __init__(self, window, window_width, window_height):
        self.dimension = 32
        self.window_width = window_width
        self.window_height = window_height
        self.x_start = random.randint(0, (window_width-self.dimension))
        self.y_start = random.randint(0, (window_height-self.dimension))
        self.image = pg.image.load(os.path.join('ladybird.png'))
        self.empty = pg.image.load(os.path.join('ladybird_empty.png'))
        self.window = window
        self.x_dir = 0
        self.y_dir = 0
        self.dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        self.shape = pg.Rect(self.x_start, self.y_start, self.dimension, self.dimension)

    def draw(self):
        self.window.blit(self.image, (self.x_start, self.y_start))
        self.shape = pg.Rect(self.x_start, self.y_start, self.dimension, self.dimension)

    def direction(self):
        temp = random.randint(0, 7)
        new_d = self.dir[temp]
        self.x_dir = new_d[0]
        self.y_dir = new_d[1]

    def error(self):
        if self.x_start == 0 or self.x_start == self.window_width:
            self.x_dir = (-self.x_dir)
            self.y_dir = random.randint(-1, 1)
        elif self.y_start == self.window_height or self.y_start == 0:
            self.x_dir = random.randint(-1, 1)
            self.y_dir = (-self.y_dir)

    def movement(self, pixels):
        for p in range(pixels):
            self.error()
            self.window.blit(self.empty, (self.x_start, self.y_start))
            self.x_start += self.x_dir
            self.y_start += self.y_dir
            self.draw()

    def smash(self, player):
        if self.shape.colliderect(player):
            return True
        else:
            return False
