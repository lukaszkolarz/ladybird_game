import pygame as pg
import os
import Ladybird as Lb
import functions as f
import Player as Pl

pg.init()
display = "menu"

width = 900                     # wymiary okna
height = 800

direction = 0

screen = pg.display.set_mode((width, height))
ladybirds = []

for i in range(6):                                              # 2 pierwszych obiektow typu ladybird
    ladybirds.append(Lb.Ladybird(screen, width, height))
for l in ladybirds:                                             # wybranie poczatkowego kierunku
    l.direction()

steve = Pl.Player(screen, width, height)

while True:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                steve.x_dir = 0
                steve.y_dir = 1
            if event.key == pg.K_DOWN and event.key == pg.K_RIGHT:
                steve.x_dir = 1
                steve.y_dir = 1
            if event.key == pg.K_UP:
                steve.x_dir = 0
                steve.y_dir = -1
            if event.key == pg.K_DOWN and event.key == pg.K_LEFT:
                steve.x_dir = -1
                steve.y_dir = 1
            if event.key == pg.K_LEFT:
                steve.x_dir = -1
                steve.y_dir = 0
            if event.key == pg.K_UP and event.key == pg.K_RIGHT:
                steve.x_dir = 1
                steve.y_dir = 1
            if event.key == pg.K_RIGHT:
                steve.x_dir = 1
            if event.key == pg.K_UP and event.key == pg.K_LEFT:
                steve.x_dir = -1
                steve.y_dir = 1

    if display == "menu":
        f.write_in_window("BIEED(R)A", 80, (255, 0, 0), screen, 405, 128, False)
        f.write_in_window("Click SPACE to begin", 30, (255, 0, 0), screen, width, height)
        logo = pg.image.load(os.path.join('big.png'))
        screen.blit(logo, (20, 20))
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                display = "game"

    elif display == "game":
        steve.draw()
        for l in ladybirds:
            l.draw()
            l.movement(2)
            if l.smash(steve.shape):
                display = "game_over"
        steve.movement(2)

    elif display == "game_over":
        f.write_in_window("GAME OVER", 40, (0, 0, 0), screen, width, height)
        f.write_in_window("Click M to menu", 25, (255, 0, 0), screen, 340, 600, False)

    pg.display.update()
