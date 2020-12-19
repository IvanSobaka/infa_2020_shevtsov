import numpy
from pygame import *
import pygame

pygame.init()

#constants
len_of_display = 600 * 2
wid_of_display = 402 * 2
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (137, 74, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (209, 255, 255)
LIGHT_BEIGE = (255, 255, 203)

screen = pygame.display.set_mode((len_of_display, wid_of_display))
screen.fill(WHITE)

#draws a circle with an outline

def d_cir(y, x, s):
   draw.circle(screen, WHITE, (y, x), 15 * s)
   draw.circle(screen, BLACK, (y, x), 15 * s, 1)

#drawing background

def background():
    draw.rect(screen, YELLOW, (0, 282 * 2, 600 * 2, 120 * 2))
    draw.rect(screen, BLUE, (0, 202 * 2, 600 * 2, 80 * 2))
    draw.rect(screen, LIGHT_BLUE, (0, 0, 600 * 2, 202 * 2))
    for i in range(10):
        draw.ellipse(screen, BLUE, (-50 + 200 * i, 404 + 160 - 40, 100, 80))
        draw.ellipse(screen, YELLOW, (49 + 200 * i, 404 + 160 - 30, 101, 80))

#drawing clouds

def cloud(y, x, s):
    d_cir(y, x, s)
    d_cir(y + 15 * s, x + 1 * s, s)
    d_cir(y + 29 * s, x - 3 * s, s)
    d_cir(y - 10 * s, x + 15 * s, s)
    d_cir(y + 5 * s, x + 16 * s, s)
    d_cir(y + 25 * s, x + 14 * s, s)
    d_cir(y + 40 * s, x + 17 * s, s)

#drawing sun and accounting

def sun(a):
    return draw.polygon(screen, YELLOW, a)

def AccountingSun(y, x, s):
    r = 50 * s
    r1 = 60 * s
    a = []
    ang = 60
    for i in range(ang):
        if i % 2 == 1:
            a.append((y + r * numpy.cos((360 / ang) * i * numpy.pi / 180),
                      x + r * numpy.sin((360 / ang) * i * numpy.pi / 180)))
        else:
            a.append((y + r1 * numpy.cos((360 / ang) * i * numpy.pi / 180),
                      x + r1 * numpy.sin((360/ang) * i * numpy.pi / 180)))
    return a

#drawing umbrella

def umbrella(y, x, s):
    draw.rect(screen, BROWN, (y, x, 6 * s, 120 * s))
    draw.polygon(screen, RED, ((y + 3 * s, x - 30 * s),
                 (y - 47 * s, x), (y+ 53 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y - 37 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y - 27 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y - 17 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y - 7 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y + 3 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y + 13 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y + 23 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y + 33 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 3 * s, x - 30 * s),
                                          (y + 43 * s, x)))

#drawing ship

def ship(y, x, s):

    draw.rect(screen, BROWN, (y, x, 200 * s, 30 * s))
    draw.polygon(screen, BROWN, ((y + 200 * s, x),
                 (y + 200 * s, x + 30 * s), (y + 270 * s, x)))
    draw.aalines(screen, BLACK, False, ((y + 200 * s, x),
                                          (y + 200 * s, x + 30 * s)))
    r = 30 * s
    for i in range(90):
        draw.aalines(screen, BROWN, False, ((y, x),
                                                    (y - r * numpy.cos(i * numpy.pi / 180),
                                                     x + r * numpy.sin(i * numpy.pi / 180))
                                                   ))


    draw.aalines(screen, BLACK, False, ((y, x),
                                          (y, x + 30 * s)))
    draw.rect(screen, BLACK, (y + 80 * s, x - 120 * s, 7 * s, 120 * s))

    #sail
    draw.polygon(screen, LIGHT_BEIGE, ((y + (400 + 7 - 320) * s, x + (100 - 220) * s),
                                           (y + (400 + 20-320) * s, x + (160 - 220) * s),
                                           (y + (400 + 80 - 320) * s, x + (160 - 220) * s)))
    draw.polygon(screen, LIGHT_BEIGE, ((y + (400 + 7 - 320) * s, x),
                                           (y + (400 + 20 - 320) * s, x + (160 - 220) * s),
                                           (y +(400 + 80 - 320) * s, x + (160 - 220) * s)))
    draw.aalines(screen, BLACK, False, ((y + (400 + 20 - 320) * s, x + (160 - 220) * s),
                                           (y + (400 + 80 - 320) * s, x + (160 - 220) * s)))

    #hole in the ship
    draw.circle(screen, BLACK, (y + (540 - 320) * s, x + (231 - 220) * s), 10 * s)
    draw.circle(screen, BLACK, (y + (540 - 320) * s, x + (231 - 220) * s), 7 * s)



#drawing all

def picture():

    array_for_sun = AccountingSun(1000, 100, 1)  # heavy accountig for the sun

    #backg
    background()

    #clouds
    cloud(250, 25, 1)
    cloud(600, 75, 3)
    cloud(80, 150, 2)

    #ships
    ship(220, 430, 1)
    ship(620, 420, 2)

    #umbrellas
    umbrella(150, 400, 2)
    umbrella(250, 500, 1)

    #sun
    sun(array_for_sun)

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

picture()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()