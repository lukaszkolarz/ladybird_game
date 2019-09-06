import pygame as pg


def write_in_window(text, size, color, window, width, height, middle=True, ):
    font = pg.font.SysFont('Arial', size)                   # w zależnosci od wybranej opcji  oraz y stanowią albo
    render = font.render(text, 1, color)                    # wspolrzedne tekstu, albo rozmiary okna (dla middle=True)

    if middle:
        x = (width - render.get_rect().width) / 2
        y = (height - render.get_rect().height) / 2
    else:
        x = width
        y = height

    window.blit(render, (x, y))


