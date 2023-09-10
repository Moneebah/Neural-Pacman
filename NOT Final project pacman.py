import pygame
import math
import time

import pygame.event


# FUNCTION FOR SCALING IMAGES
def scale(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


# IMPORTING IMAGES NEEDED
F_MAZE = pygame.image.load('Assets/PACMAN MAZE 1.png')
F_MAZE_MASK = pygame.mask.from_surface(F_MAZE)
PACMAN = pygame.image.load('Assets/Pacman circle.png')
RED_GHOST = scale(pygame.image.load('Assets/red ghost.png'), 0.035)
BLUE_GHOST = scale(pygame.image.load('Assets/blue ghost.png'), 0.035)
YELLOW_GHOST = scale(pygame.image.load('Assets/Yellow ghost.png'), 0.04)
# TILE = pygame.image.load('Assets/Square2.png')
# TILE = pygame.transform.scale(TILE, (20, 20))
BLANK = pygame.image.load('Assets/black.png')
COIN = pygame.image.load('Assets/coin.png')
COIN = pygame.transform.scale(COIN, (5, 5))
PACMAN = pygame.transform.scale(PACMAN, (18, 18))
# SETTING UP MAIN WINDOW

WIDTH, HEIGHT = F_MAZE.get_width(), F_MAZE.get_height()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PACMAN - MUNEEBA SE-071')
icon = pygame.image.load('Assets/PACMAN ICON.png')
pygame.display.set_icon(icon)
score = 0
# FUNCTION FOR DRAWING

def draw(win, images):
    WIN.blit(F_MAZE, (0, 0))
    WIN.blit(PACMAN, (start_x, start_y))

    for img, pos in images:
        win.blit(img, pos)


def collide_maze(mask, x=0, y=0):
    global start_x, start_y
    Pacman_mask = pygame.mask.from_surface(PACMAN)
    offset = (int(start_x - x), int(start_y - y))
    poi = mask.overlap(Pacman_mask, offset)
    return poi


########################### MAIN PROGRAM ##########################
run = True
FPS = 60
clock = pygame.time.Clock()
start_x, start_y = 20, 20

images = [(RED_GHOST, (20, 450)), (BLUE_GHOST, (140, 60)), (YELLOW_GHOST, (520, 150))]
GRAY = (107, 107, 107)
CELL_WIDTH = WIDTH // 28
print(CELL_WIDTH)
CELL_HEIGHT = HEIGHT // 30
print(CELL_HEIGHT)

vel = 1
# SETTING MAZE
MAZE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 5, 5, 5, 5, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 5, 5, 5, 5, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 0],
    [5, 5, 5, 5, 5, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 5, 5, 5, 5, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 5, 5, 5, 5, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
TILESIZE = 17
# INFINITE EVENT LOOP
while run:
    clock.tick(FPS)

    # DRAW CHARACTERS ON BOARD
    WIN.fill((0, 0, 0))
    draw(WIN, images)
    pygame.display.update()

    # draw coins
    coin_rect = []
    for row_index, row in enumerate(MAZE):
        for col_index, col in enumerate(row):
            x = col_index * TILESIZE
            y = row_index * TILESIZE
            if col == 1:
                WIN.blit(COIN, (x, y))
                coin_rect.append(pygame.Rect(x, y, 5, 5))
    pygame.display.update()

    # check collision of maze
    if collide_maze(F_MAZE_MASK) is not None:
        print("collide")
        if direction == 'LEFT':
            start_x += 1

        if direction == 'RIGHT':
            start_x -= 1

        if direction == 'UP':
            start_y += 1

        if direction == 'DOWN':
            start_y -= 1

    # check coin collection
    Pacman_rect = pygame.Rect(start_x, start_y, 18, 18)
    for c in coin_rect:
        if c.colliderect(Pacman_rect):
            coin_x = c.left
            coin_y = c.top
            index_column = coin_x // TILESIZE
            index_row = coin_y // TILESIZE
            MAZE[index_row][index_column] = 0
            coin_rect.remove(c)
            score += 1
            print(score)

    # PACMAN movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        start_x -= vel

        direction = 'LEFT'

    elif keys[pygame.K_RIGHT]:
        start_x += vel
        direction = 'RIGHT'

    elif keys[pygame.K_UP]:
        start_y -= vel
        direction = 'UP'

    elif keys[pygame.K_DOWN]:
        start_y += vel
        direction = 'DOWN'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()

