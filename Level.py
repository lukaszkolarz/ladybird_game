import pygame as pg
import functions as f
import os
import Ladybird as Lb
import Player as Pl


class Level:
    def __init__(self, window, window_width, window_height):
        self.display = "menu"
        self.window = window
        self.menu_background = pg.image.load(os.path.join('menu.png'))
        self.window_width = window_width
        self.window_height = window_height
        self.level = 1
        self.ladybirds_amount = 0
        self.velocity = 0
        self.ladybirds = []
        self.steve = Pl.Player(self.window, self.window_width, self.window_height)
        self.score = 0
        self.state = 0

    def game(self):
        if self.state == 0:
            self.state = self.level_conf()
        self.steve.draw()
        self.steve.movement(2)
        f.write_in_window("SCORE: "+str(self.score), 30, (0, 255, 0), self.window, 10, 10, False)
        f.write_in_window("LEVEL "+str(self.level), 30, (0, 255, 0), self.window, self.window_width-120, 10, False)
        for l in self.ladybirds:
            l.draw()
            l.movement(self.velocity)
            if l.smash(self.steve.shape):
                self.display = "game_over"
            if self.score == 100:                                           # punkty do nastepego levela
                if self.level == 9:
                    self.display = "victory_out"
                else:
                    self.display = "victory_in"

    def choice(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.menu_background, ((self.window_width - 602)/2, (self.window_height - 602)/2))

    def victory_in(self):
        self.score = 0
        self.window.fill((255, 255, 255))
        f.write_in_window("Victory!", 50, (255, 0, 0), self.window, self.window_width, self.window_height)
        f.write_in_window("Next level > click SPACE, M > menu", 20, (255, 0, 100), self.window, 400, 750, False)
        if self.state == 1:
            self.res_construction()

    def victory_out(self):
        self.score = 0
        self.level = 1
        self.window.fill((255, 255, 255))
        f.write_in_window("YOU WON", 50, (255, 0, 0), self.window, self.window_width, self.window_height)
        f.write_in_window("Press M to mack to MENU", 20, (255, 0, 100), self.window, 400, 750, False)
        if self.state == 1:
            self.res_construction()

    def game_over(self):
        self.score = 0
        self.window.fill((255, 255, 255))
        f.write_in_window("GAME OVER", 50, (255, 0, 0), self.window, self.window_width, self.window_height)
        f.write_in_window("Press M to back to MENU", 20, (255, 0, 100), self.window, 400, 750, False)
        if self.state == 1:
            self.res_construction()

    def level_conf(self):
        if self.level == 1 or self.level == 4 or self.level == 7:
            self.ladybirds_amount = 3
        elif self.level == 2 or self.level == 5 or self.level == 8:
            self.ladybirds_amount = 4
        elif self.level == 3 or self.level == 6 or self.level == 9:
            self.ladybirds_amount = 5

        if self.level == 1 or self.level == 2 or self.level == 3:
            self.velocity = 2
        elif self.level == 4 or self.level == 5 or self.level <= 6:
            self.velocity = 3
        elif self.level == 7 or self.level == 8 or self.level == 9:
            self.velocity = 4
        self.construct()
        return 1

    def construct(self):
         for i in range(self.ladybirds_amount):
            self.ladybirds.append(Lb.Ladybird(self.window, self.window_width, self.window_height))
         for l in self.ladybirds:                   # wybranie poczatkowego kierunku
            l.direction()

    def res_construction(self):
        self.ladybirds.clear()
        self.steve.restart()
        self.state = 0
