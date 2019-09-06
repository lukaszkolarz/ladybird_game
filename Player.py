import pygame as pg
import os


class Player:
    def __init__(self, window, window_width, window_height):
        self.height = 28
        self.width = 14
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        self.image = pg.image.load(os.path.join('player.png'))
        self.empty = pg.image.load(os.path.join('player_empty.png'))
        self.x_start = (self.window_width - self.width)/2
        self.y_start = (self.window_height - self.height)/2
        self.x_dir = 0
        self.y_dir = 0
        self.shape = pg.Rect(self.x_start, self.y_start, self.width, self.height)

    def draw(self):
        self.window.blit(self.image, (self.x_start, self.y_start))
        self.shape = pg.Rect(self.x_start, self.y_start, self.width, self.height)

    def movement(self, pixels):
        self.error()
        self.window.blit(self.empty, (self.x_start, self.y_start))
        for i in range(pixels):
            self.x_start += self.x_dir
            self.y_start += self.y_dir
        self.draw()

    def error(self):
        if self.x_start < 0 or self.x_start > self.window_width:
            self.x_dir = (-self.x_dir)
        if self.y_start > self.window_height or self.y_start < 0:
            self.y_dir = (-self.y_dir)
