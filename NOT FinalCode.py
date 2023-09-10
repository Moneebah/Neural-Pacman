import pygame
import math
import time

import pygame.event


# FUNCTION FOR SCALING IMAGES
def scale(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


# IMPORTING IMAGES NEEDED
F_MAZE = pygame.image.load('Assets/PACMAN MAZE PROJECT 2.png')
PACMAN = pygame.image.load('Assets/PACMAN.png')
RED_GHOST = scale(pygame.image.load('Assets/red ghost.png'), 0.035)
BLUE_GHOST = scale(pygame.image.load('Assets/blue ghost.png'), 0.035)
YELLOW_GHOST = scale(pygame.image.load('Assets/Yellow ghost.png'), 0.04)
TILE = pygame.image.load('Assets/Square2.png')
TILE = pygame.transform.scale(TILE, (20, 20))
PACMAN = pygame.transform.scale(PACMAN, (15, 15))
Pacman_rect = PACMAN.get_rect()

# SETTING UP MAIN WINDOW

WIDTH, HEIGHT = 20 * 28, 20 * 31

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PACMAN - MUNEEBA SE-071')
icon = pygame.image.load('Assets/PACMAN ICON.png')
pygame.display.set_icon(icon)

# SETTING MAZE
MAZE = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 1, 1, 7, 8, 9, 1, 1, 1, 1, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [5, 5, 5, 5, 5, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
TILESIZE = 20


# FUNCTION FOR DRAWING

def draw(win, images):
    # WIN.blit(F_MAZE, (0, 40))
    WIN.blit(PACMAN, (start_x, start_y))

    for img, pos in images:
        win.blit(img, pos)


def hit_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def collision_test(rect, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    collisions = hit_test(Pacman_rect,tiles)
    for tile in collisions:
        if direction == 'RIGHT':
            rect.right = tile.left
            collision_types['right'] = True
        elif direction == 'LEFT':
            rect.left = tile.right
            collision_types['left'] = True
    collisions = hit_test(Pacman_rect,tiles)
    for tile in collisions:
        if direction == 'UP':
            rect.top = tile.bottom
            collision_types['top'] = True
        elif direction == 'DOWM':
            rect.bottom = tile.top
            collision_types['bottom'] = True


################### MAIN PROGRAM ##################
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

# INFINITE EVENT LOOP
while run:
    clock.tick(FPS)

    # DRAW CHARACTERS ON BOARD
    WIN.fill((0, 0, 0))

    TILE_rect = []

    for row_index, row in enumerate(MAZE):
        for col_index, col in enumerate(row):
            x = col_index * TILESIZE
            y = row_index * TILESIZE
            if col == 0:
                WIN.blit(TILE, (x, y))
                TILE_rect.append(pygame.Rect(x * TILESIZE, y * TILESIZE, TILESIZE, TILESIZE))
    print(TILE_rect)
    draw(WIN, images)
    pygame.display.update()

    # draw grid
    # for x in range(int(WIDTH // (WIDTH // 28))):
    # pygame.draw.line(WIN, GRAY, (x * 20, 40), (x * 20, 40 + HEIGHT))
    # for y in range(int(HEIGHT // (HEIGHT // 30))):
    # pygame.draw.line(WIN, GRAY, (0, 40 + y * 20), (WIDTH, 40 + y * 20))
    # pygame.display.update()
    # PACMAN MOVEMENT
    Px = Pacman_rect.x
    Py = Pacman_rect.y
    Px = Px // 20
    Py = Py // 20
    print(MAZE[Py][Px])
    print(Px, Py)

    keys = pygame.key.get_pressed()
    for i in TILE_rect:
        if Pacman_rect.colliderect(i):
            print('collision')
    if keys[pygame.K_LEFT]:
        start_x -= vel
        Pacman_rect.x -= vel

        direction = 'LEFT'

    if keys[pygame.K_RIGHT]:
        start_x += vel
        Pacman_rect.x += vel
        direction = 'RIGHT'

    if keys[pygame.K_UP]:
        start_y -= vel
        Pacman_rect.y -= vel
        direction = 'UP'

    if keys[pygame.K_DOWN]:
        start_y += vel
        Pacman_rect.y += vel
        direction = 'DOWN'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
