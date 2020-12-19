import pygame
from pygame.draw import *
from random import randint
pygame.init()

#collors

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


#constants

WIDTH = 800

fl = 0

Score = 0
current_balls = 10

FPS = 60
screen = pygame.display.set_mode((1000, 700))

#Make Balls

def create_balls():
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    vx = randint(2, 6)
    vy = randint(2, 6)
    color = COLORS[randint(0, 5)]

    return {
        'x' : x,
        'y' : y,
        'r' : r,
        'vx' : vx,
        'vy' : vy,
        'color' : color,
        'type' : 1
    }

#Make Special Target

def create_newtarget():
    return {
        'x' : 0,
        'y' : 350,
        'r' : 25,
        'vx' : 6,
        'vy' : randint(2,10),
        'color' : RED,
        'type' : 2
    }



def draw_target(object):
    if object['type'] == 1:
        circle(screen, object['color'], (object['x'], object['y']), object['r'])
    elif object['type'] == 2:
        rect(screen, object['color'], (object['x'], object['y'], object['r'], object['r']))


def move_target(object):
    if object['type'] == 1:
        if object['x'] < 0 or object['x'] > 700:
            object['vx'] = -1 * object['vx']
        if object['y'] < 0 or object['y'] > 500:
            object['vy'] = -1 * object['vy']
    elif object['type'] == 2:
        if object['x'] < 0 or object['x'] > 700:
            object['vx'] = -1.1 * object['vx']
        if object['y'] < 0 or object['y'] > 500:
            object['vy'] = -1.1 * object['vy']

    if abs(object['vx']) > 25 or abs(object['vy']) > 25:
        global fl
        fl = 0

    object['x'] += object['vx']
    object['y'] += object['vy']


#Cheking if the player hits the ball

def check_click(object, position):
    mx, my = position
    if object['type'] == 1:
        if (mx - int(object['x'])) ** 2 + (my - int(object['y'])) ** 2 <= int(object['r']) ** 2:
            return 1
        else:
            return 0
    elif object['type'] == 2:
        if abs(mx - object['x']) <= object['r'] and abs(my - object['y']) <= object['r']:
            return 1
        else:
            return 0


#Reading leaderboard

def leaderboard():
    file = open('venv\\leaderboard.txt', 'r')
    board = file.readlines()
    file.close()
    n = len(board)
    font1 = pygame.font.Font(None, 30)
    text = [font1.render('LEADERBOARD:', 1, YELLOW)]
    font1 = pygame.font.Font(None, 24)
    for i in range(min(n, 10)):
        text.append(font1.render(board[i][:-1], 1, BLUE))
    screen.blit(text[0], (WIDTH + 10, 10))
    for i in range(min(n, 10)):
        screen.blit(text[i + 1], (WIDTH + 10, i * 20 + 30))

#update leaderboard

def update_leaderboard(name, score):
    file = open('venv\\leaderboard.txt', 'r')
    board = file.readlines()
    file.close()
    board.append(str(score) + ' ' + name + '\n')
    n = len(board)
    board = [board[i].split() for i in range(n)]
    board = [[int(board[i][0]), board[i][1]] for i in range(n)]
    board.sort(reverse=True)
    board = [str(board[i][0]) + ' ' + str(board[i][1]) + '\n' for i in range(n)]
    board = board[:min(10, n)]
    file = open('venv\\leaderboard.txt', 'w')
    file.writelines(board)
    file.close()


#name of player

name = str(input('Name your fighter(No more than 15 symbols): \n'))
name = name[:15]

#Creating balls

Balls = [create_balls() for i in range(current_balls)]
new_target = []

#Creating window of game

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    leaderboard()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i in range(current_balls):
                    if check_click(Balls[i], event.pos) == 1:
                        Balls[i] = create_balls()
                        Score += 1
                if (fl == 1):
                    if check_click(new_target, event.pos) == 1:
                        Score += 100
                        fl = 0

    if fl == 1:
        draw_target(new_target)
        move_target(new_target)

    #Special target

    if (Score % 50 == 0 and Score != 0 and fl == 0):
        fl = 1
        new_target = create_newtarget();

    #drawing and moving target


    for i in range(current_balls):
        draw_target(Balls[i])
        move_target(Balls[i])

    pygame.display.set_caption('Score = ' + str(Score))
    pygame.display.update()
    screen.fill(BLACK)

#update learderboard

update_leaderboard(name, Score)

pygame.quit()