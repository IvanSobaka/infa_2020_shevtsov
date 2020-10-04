import numpy
import pygame
import random

from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

rect(screen, (251, 241, 177), (0, 0, 800, 600))

circle(screen, (0, 0, 0), (400, 300), 203)
circle(screen, (212, 218, 0), (400, 300), 200)

rect(screen, (0, 0, 0), (300, 400, 200, 30))

circle(screen, (0, 0, 0), (300, 250), 52)
circle(screen, (255, 0, 0), (300, 250), 50)
circle(screen, (0, 0, 0), (300, 250), 20)

circle(screen, (0, 0, 0), (500, 250), 42)
circle(screen, (255, 0, 0), (500, 250), 40)
circle(screen, (0, 0, 0), (500, 250), 17)

line(screen, (0, 0, 0), (200, 145), (370, 215), 20)

line(screen, (0, 0, 0), (450, 215), (600, 160), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
