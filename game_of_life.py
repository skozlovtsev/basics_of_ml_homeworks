import pygame as pg
from time import sleep
import random
from pygame.locals import *


def near(pos: list, system=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
    count = 0
    for i in system:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
size_of_cell = 5
sl = 0
live = (2, 3)
born = (3,)


root = pg.display.set_mode((1200, 600))

cells = [[random.choice([0, 1]) for j in range(root.get_width() // size_of_cell)] for i in
         range(root.get_height() // size_of_cell * 2)]

if __name__ == '__main__':
    while True:
        # Заполняем экран белым цветом
        root.fill(WHITE)

        for i in pg.event.get():
            if i.type == QUIT:
                quit()

        cells2 = [[0 for j in range(len(cells[0]))] for i in range(len(cells))]

        for i in range(0, len(cells)):
            for j in range(0, len(cells[i])):
                pg.draw.rect(root, (255 * cells[i][j], 255 * cells[i][j], 255 * cells[i][j]),
                             [i * size_of_cell, j * size_of_cell, size_of_cell, size_of_cell])
                # Если клетка жива
                if cells[i][j]:
                    # Если у соседей не 2 или 3 соседа
                    if near([i, j]) not in live:
                        cells2[i][j] = 0
                        continue
                    # В ином случае
                    cells2[i][j] = 1
                    continue
                # Если клетка мертва и у неё 3 соседа
                if near([i, j]) in born:
                    cells2[i][j] = 1
                    continue
                # В противном случае
                cells2[i][j] = 0
        pg.display.update()

        cells = cells2
        sleep(sl * 0.1)
