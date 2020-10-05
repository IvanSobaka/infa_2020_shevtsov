import numpy
import pygame
import random

from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))



rect(screen, (240, 79, 70), (0, 0, 800, 600))



def panda (x, y, size):

    ellipse(screen, (255, 255, 255), (x + int(20 * size), y + int(size * 30), int(size * 300), int(size * 150)))

    for i in range(70):
        circle(screen, (0, 0, 0), (x + int((125 - i // 2) * size), y + int((175 + i) * size)), int(25 * size))

    for i in range(70):
        circle(screen, (0, 0, 0), (x + int((40 - i // 2) * size), y + int((148 + i) * size)), int(25 * size))

    line(screen, (0, 0, 0), (x + 110 * size, y + size * 170), (x + size * 85, y + size * 245), int(size * 40))

    ellipse(screen, (255, 255, 255), (x, y, int(135 * size), int(200 * size)))

    circle(screen, (0, 0, 0), (x + int(90 * size), y + int(130 * size)), int(size * 25))

    ellipse(screen, (0, 0, 0), (x, y + int(size * 100), int(size * 44), int(size * 60)))

    ellipse(screen, (0, 0, 0), (x + int(size * 33), y + int(size * 163), int(size * 64), int(size * 40)))

    ellipse(screen, (0, 0, 0), (x - int(size * 25), y - int(10 * size), int(80 * size), int(50 * size)))

    ellipse(screen, (0, 0, 0), (x + int(size * 70), y, int(size * 80), int(size * 50)))

    line(screen, (0, 0, 0), (x + int(size * 140), y + int(size * 20)), (x + int(size * 133), y + int(size * 195)), int(size * 20))

    ellipse(screen, (0, 0, 0), (x + int(size * 54), y + int(size * 228), int(size * 70), int(size * 50)))

    ellipse(screen, (0, 0, 0), (x - int(26 * size), y + int(size * 207), int(size * 60), int(size * 40)))

    for i in range(110):
        circle(screen, (0, 0, 0), (x + int((260 - i // 7) * size), y + int((130 + i)* size)), int(size * 30))

    ellipse(screen, (0, 0, 0), (x + int(size * 205), y + int(size * 220), int(size * 80), int(size * 60)))





def palm(x, y, size):
    line(screen, (0, 102, 0), (x, y), (x, y - int(100 * size)), int(30 * size))
    line(screen, (0, 102, 0), (x, y - int(120 * size)), (x, y - int(220 * size)), int(size * 30))
    line(screen, (0, 102, 0), (x - int(5 * size), y - int(240 * size)), (x + int(25 * size), y - int(320 * size)), int(size * 27))
    line(screen, (0, 102, 0), (x + int(25 * size), y - int(335 * size)), (x + int(75 * size), y - int(440 * size)), int(size * 14))

    arc(screen, (0, 102, 0), (x - int(390 * size), y - int(360 * size), int(size * 400), int(size * 250)), 0.5, 1.7, 3)

    arc(screen, (0, 102, 0), (x - int(310 * size), y - int(260 * size), int(size * 300), int(size * 400)), 0.5, 2, 3)

    arc(screen, (0, 102, 0), (x + int(20 * size), y - int(300 * size), int(size * 700), int(size * 300)), 2.2, 3, 3)

    arc(screen, (0, 102, 0), (x + int(10 * size), y - int(440 * size), int(size * 700), int(size * 400)), 1.8, 2.6, 3)

    ellipse(screen, (0, 102, 0), (x - int(200 * size), y - int(353 * size), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x - int(170 * size), y - int(355 * size), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x - int(140 * size), y - int(345 * size), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x - int(110 * size), y - int(342 * size), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x - int(70 * size),  y - int(323 * size), int(size * 20), int(size * 60)))

    ellipse(screen, (0, 102, 0), (x - int(size * 200), y - int(size * 253), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x - int(size * 140), y - int(size * 245), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x - int(size * 80), y - int(size * 210), int(size * 20), int(size * 60)))

    ellipse(screen, (0, 102, 0), (x + int(size * 80), y - int(size * 360), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x + int(size * 120), y - int(size * 375), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x + int(size * 160), y - int(size * 395), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x + int(size * 200), y - int(size * 410), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x + int(size * 240), y - int(size * 420), int(size * 20), int(size * 60)))

    ellipse(screen, (0, 102, 0), (x + int(size * 40), y - int(size * 190), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x + int(size * 80), y - int(size * 230), int(size * 20), int(size * 60)))
    ellipse(screen, (0, 102, 0), (x + int(size * 130), y - int(size * 260), int(size * 20), int(size * 60)))

palm(130, 350, 0.52)
palm(330, 350, 0.52)
palm(480, 350, 0.75)
palm(640, 350, 0.56)

panda(400, 300, 0.8)
panda(200, 400, 0.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
