import pygame as pg
import os


class Menu:
    def __init__(self, window, window_width, window_height):
        self.dimension = 602
        self.window_width = window_width
        self.window_height = window_height
        self.window = window
        self.background = pg.image.load(os.path.join('menu.png'))
