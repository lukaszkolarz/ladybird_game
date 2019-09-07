import pygame as pg
import os
import functions as f
import Level as Lv

pg.init()
display = "menu"

width = 900                     # wymiary okna
height = 800

direction = 0

screen = pg.display.set_mode((width, height))
level = Lv.Level(screen, width, height)


while True:
    screen.fill((255, 255, 255))
    display = level.display
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            if event.type == pg.KEYDOWN:
                if display == "victory_in":
                    if event.key == pg.K_SPACE:
                        level.display = "game"
                        level.level += 1
                    if event.key == pg.K_m:
                        level.display = "menu"

                if display == "victory_out" or display == "game_over":
                    if event.key == pg.K_m:
                        level.display = "menu"

                if display == "game":
                    level.score += 1
                    if event.key == pg.K_DOWN:
                        level.steve.x_dir = 0
                        level.steve.y_dir = 1
                    if event.key == pg.K_DOWN and event.key == pg.K_RIGHT:
                        level.steve.x_dir = 1
                        level.steve.y_dir = 1
                    if event.key == pg.K_UP:
                        level.steve.x_dir = 0
                        level.steve.y_dir = -1
                    if event.key == pg.K_DOWN and event.key == pg.K_LEFT:
                        level.steve.x_dir = -1
                        level.steve.y_dir = 1
                    if event.key == pg.K_LEFT:
                        level.steve.x_dir = -1
                    if event.key == pg.K_UP and event.key == pg.K_RIGHT:
                        level.steve.x_dir = 1
                        level.steve.y_dir = 1
                    if event.key == pg.K_RIGHT:
                        level.steve.x_dir = 1
                    if event.key == pg.K_UP and event.key == pg.K_LEFT:
                        level.steve.x_dir = -1
                        level.steve.y_dir = 1

                if display == "menu":
                    if event.key == pg.K_SPACE:
                        level.display = "choice"

                if display == "choice":
                    if event.key == pg.K_1:
                        level.display = "game"
                        level.level = 1
                    if event.key == pg.K_2:
                        level.display = "game"
                        level.level = 2
                    if event.key == pg.K_3:
                        level.display = "game"
                        level.level = 3
                    if event.key == pg.K_4:
                        level.display = "game"
                        level.level = 4
                    if event.key == pg.K_5:
                        level.display = "game"
                        level.level = 5
                    if event.key == pg.K_6:
                        level.display = "game"
                        level.level = 6
                    if event.key == pg.K_7:
                        level.display = "game"
                        level.level = 7
                    if event.key == pg.K_8:
                        level.display = "game"
                        level.level = 8
                    if event.key == pg.K_9:
                        level.display = "game"
                        level.level = 9
                    if event.key == pg.K_m:
                        level.display = "menu"

    if display == "menu":
        f.write_in_window("BIEED(R)A", 80, (255, 0, 0), screen, 405, 128, False)
        f.write_in_window("Click SPACE to begin", 30, (255, 0, 0), screen, width, height)
        logo = pg.image.load(os.path.join('big.png'))
        screen.blit(logo, (20, 20))
        level.level = 1

    elif display == "choice":
        level.choice()

    elif display == "game":
        level.game()

    elif display == "victory_in":
        level.victory_in()

    elif display == "victory_out":
        level.victory_out()

    elif display == "game_over":
        level.game_over()

    pg.display.update()
