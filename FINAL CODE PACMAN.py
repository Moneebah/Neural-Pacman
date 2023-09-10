import pygame
import pygame.event
pygame.font.init()

# IMPORTING IMAGES NEEDED
F_MAZE = pygame.image.load('Assets/PACMAN MAZE 1.png')
F_MAZE_MASK = pygame.mask.from_surface(F_MAZE)
PACMAN = pygame.image.load('Assets/Pacman circle.png')
LIVES = pygame.image.load('Assets/PACMAN.png')
LIVES = pygame.transform.scale(LIVES, (18, 18))
RED_GHOST = pygame.image.load('Assets/red ghost.png')
RED_GHOST = pygame.transform.scale(RED_GHOST, (15, 15))
BLUE_GHOST = pygame.image.load('Assets/blue ghost.png')
BLUE_GHOST = pygame.transform.scale(BLUE_GHOST, (15, 15))

YELLOW_GHOST = pygame.image.load('Assets/Yellow ghost.png')
YELLOW_GHOST = pygame.transform.scale(YELLOW_GHOST, (15, 15))

BLANK = pygame.image.load('Assets/black.png')
COIN = pygame.image.load('Assets/coin.png')
COIN = pygame.transform.scale(COIN, (5, 5))
PACMAN = pygame.transform.scale(PACMAN, (16, 16))

# SETTING UP MAIN WINDOW
WIDTH, HEIGHT = F_MAZE.get_width(), F_MAZE.get_height() + 80
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('PACMAN - MUNEEBA SE-071')
icon = pygame.image.load('Assets/PACMAN ICON.png')
pygame.display.set_icon(icon)

# FONTS
white = (255, 255, 255)
font = pygame.font.Font("Assets/Emulogic-zrEw (1).ttf", 16)
font2 = pygame.font.Font("Assets/Emulogic-zrEw (1).ttf", 32)
text = font.render('HIGH SCORE:', True, white)
text2 = font.render('SCORE:', True, white)
# old high score
file = open("High_Scores.txt", "r")
data = file.readline()
high_score_list = data.split()
high_score_list.sort(key=int)
old_high_score = high_score_list[-1]
text3 = font.render(old_high_score, True, white)


# FUNCTION FOR DRAWING
def draw():
    WIN.blit(F_MAZE, (0, 0))
    WIN.blit(PACMAN, (start_x, start_y))
    WIN.blit(RED_GHOST, (red_x, red_y))
    WIN.blit(BLUE_GHOST, (blue_x, blue_y))
    WIN.blit(YELLOW_GHOST, (ylow_x, ylow_y))


# FUNCTION FOR MAZE COLLISION
def collide_maze(mask, x=0, y=0):
    global start_x, start_y
    Pacman_mask = pygame.mask.from_surface(PACMAN)
    offset = (int(start_x - x), int(start_y - y))
    poi = mask.overlap(Pacman_mask, offset)
    return poi


# FUNCTION FOR CHANGING POINTS OF GHOSTS
def change_point_red(strtx, strty, path):
    global red_current_point
    if red_current_point < len(path) - 1:
        target = path[red_current_point]
        rect = pygame.Rect(strtx, strty, 15, 15)
        if rect.collidepoint(*target):
            red_current_point += 1
            target = path[red_current_point]
    else:
        red_current_point = 1
        target = path[red_current_point]
    return target


def change_point_blue(strtx, strty, path):
    global blue_current_point
    if blue_current_point < len(path) - 1:
        target = path[blue_current_point]
        rect = pygame.Rect(strtx, strty, 15, 15)
        if rect.collidepoint(*target):
            blue_current_point += 1
            target = path[blue_current_point]
    else:
        blue_current_point = 1
        target = path[blue_current_point]
    return target


def change_point_ylow(strtx, strty, path):
    global ylow_current_point
    if ylow_current_point < len(path) - 1:
        target = path[ylow_current_point]
        rect = pygame.Rect(strtx, strty, 15, 15)
        if rect.collidepoint(*target):
            ylow_current_point += 1
            target = path[ylow_current_point]
    else:
        ylow_current_point = 1
        target = path[ylow_current_point]
    return target


########################### MAIN PROGRAM ##########################
# INITIALISING VARIABLES + SETTING CLOCK SPEED
run = True
FPS = 60
clock = pygame.time.Clock()

start_x, start_y = 15, 15
red_x, red_y = 170, 187
blue_x, blue_y = 220, 187
ylow_x, ylow_y = 255, 187

vel = 1
ghost_vel = 1
lives_count = 3
score = 0
red_current_point = 0
blue_current_point = 0
ylow_current_point = 0

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
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]

]
TILESIZE = 17

red_path = [(170, 187), (153, 187), (153, 238), (102, 238), (102, 136), (17, 136), (17, 17),
            (204, 17), (204, 85), (238, 85), (238, 51), (238, 17), (340, 17), (340, 85), (425, 85), (425, 17),
            (340, 17), (340, 85), (289, 85), (289, 136), (238, 136), (238, 187), (170, 187)]

blue_path = [(289, 187), (289, 187), (289, 238), (340, 238), (340, 323), (425, 323), (425, 374),
             (391, 376), (391, 425), (425, 425), (425, 476), (238, 476), (17, 476), (17, 425), (51, 425),
             (102, 425), (102, 323), (153, 323), (153, 187), (289, 187)]

yellow_path = [(255, 187), (170, 187), (153, 187), (153, 238), (102, 238), (102, 323), (204, 323), (204, 374),
               (238, 374), (238, 323), (289, 323), (289, 187), (255, 187)]

# INFINITE EVENT LOOP
while run:
    clock.tick(FPS)

    # DRAWING
    WIN.fill((0, 0, 0))
    # draw coins, lives, score
    coin_rect = []
    y_score = font.render(str(score), True, white)
    for row_index, row in enumerate(MAZE):
        for col_index, col in enumerate(row):
            x = col_index * TILESIZE
            y = row_index * TILESIZE
            if col == 1:
                WIN.blit(COIN, (x, y))
                coin_rect.append(pygame.Rect(x, y, 5, 5))
            if col == 3:
                WIN.blit(LIVES, (x, y))
            if col == 4:
                WIN.blit(text, (x, y))
            if col == 7:
                WIN.blit(text2, (x, y))
            if col == 8:
                WIN.blit(text3, (x, y))
            if col == 9:
                WIN.blit(y_score, (x, y))
    # draw characters, maze
    draw()
    pygame.display.update()

    # GHOST MOVEMENT
    # red ghost
    newx, newy = change_point_red(red_x, red_y, red_path)
    if newx > red_x:
        # going right
        red_x += ghost_vel
    elif newx < red_x:
        # going right
        red_x -= ghost_vel
    if newy > red_y:
        # going down
        red_y += ghost_vel
    elif newy < red_y:
        # going up
        red_y -= ghost_vel

    # blue ghost
    blue_newx, blue_newy = change_point_blue(blue_x, blue_y, blue_path)
    if blue_newx > blue_x:
        # going right
        blue_x += ghost_vel
    elif blue_newx < blue_x:
        # going right
        blue_x -= ghost_vel
    if blue_newy > blue_y:
        # going down
        blue_y += ghost_vel
    elif blue_newy < blue_y:
        # going up
        blue_y -= ghost_vel

    # yellow ghost
    ylow_newx, ylow_newy = change_point_ylow(ylow_x, ylow_y, yellow_path)
    if ylow_newx > ylow_x:
        # going right
        ylow_x += ghost_vel
    elif ylow_newx < ylow_x:
        # going right
        ylow_x -= ghost_vel
    if ylow_newy > ylow_y:
        # going down
        ylow_y += ghost_vel
    elif ylow_newy < ylow_y:
        # going up
        ylow_y -= ghost_vel

    # MAZE COLLISION
    if collide_maze(F_MAZE_MASK) is not None:
        if direction == 'LEFT':
            start_x += 1
        if direction == 'RIGHT':
            start_x -= 1
        if direction == 'UP':
            start_y += 1
        if direction == 'DOWN':
            start_y -= 1

    # COIN COLLECTION + SCORE
    Pacman_rect = pygame.Rect(start_x, start_y, 16, 16)
    for c in coin_rect:
        if c.colliderect(Pacman_rect):
            coin_x = c.left
            coin_y = c.top
            index_column = coin_x // TILESIZE
            index_row = coin_y // TILESIZE
            MAZE[index_row][index_column] = 0
            coin_rect.remove(c)
            score += 1
            if score == 279:
                file = open("High_Scores.txt", "a")
                your_score = str(score)
                file.write(" " + your_score)
                file.close()
                text3 = font.render(your_score, True, white)
                
    # GHOST COLLISION + LIVES ADJUSTMENT + HIGHSCORE ADJUSTMENT
    Red_rect = pygame.Rect(red_x, red_y, 15, 15)
    Blue_rect = pygame.Rect(blue_x, blue_y, 15, 15)
    Yellow_rect = pygame.Rect(ylow_x, ylow_y, 15, 15)
    Ghost_rect = [Red_rect, Blue_rect, Yellow_rect]
    for g in Ghost_rect:
        if g.colliderect(Pacman_rect):
            score -= 10
            lives_count -= 1
            for i in MAZE[31]:
                if MAZE[31][3] == 3 and lives_count == 2:
                    MAZE[31][3] = 0
                elif MAZE[31][2] == 3 and lives_count == 1:
                    MAZE[31][2] = 0
                elif MAZE[31][1] == 3 and lives_count == 0:
                    MAZE[31][1] = 0
                    # inserting to file
                    file = open("High_Scores.txt", "a")
                    your_score = str(score)
                    file.write(" " + your_score)
                    file.close()
                    # check if u beat high score
                    file2 = open("High_Scores.txt", "r")
                    data = file2.readline()
                    high_score_list = data.split()
                    high_score_list.sort(key=int)
                    new_high_score = high_score_list[-1]
                    text3 = font.render(new_high_score, True, white)
                    file2.close()
                    # reset everything
                    score = 0
                    lives_count = 3
                    MAZE[31][3] = 3
                    MAZE[31][2] = 3
                    MAZE[31][1] = 3
                # reset player/enemies
                start_x, start_y = 15, 15
                red_current_point = 0
                ylow_current_point = 0
                blue_current_point = 0
                red_x, red_y = 170, 187
                blue_x, blue_y = 210, 175
                ylow_x, ylow_y = 240, 175

    # PACMAN MOVEMENT
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

    # EXIT GAME
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
