import pygame
import datetime
from random import randrange


size = width, height = 1050, 650
block = 25

x, y = randrange(0, width, block), randrange(0, height, block)
apple = randrange(0, width, block), randrange(0, height, block)
orange = randrange(0, width, block), randrange(0, height, block)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
lastTime = 0
score = 0
level = 0
snake = [(x, y)]
dx, dy = 0, 0
fps = 10
walls = []

pygame.init()
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)
font_menu = pygame.font.SysFont('Arial', 85,bold=True)
game_background = pygame.image.load('img\\game_background.jpg').convert()
menu_background = pygame.image.load('img\\menu_background.jpg').convert()


def main_menu():
    menu = True
    while menu:
        screen.blit(menu_background, (0, 0))
        
        # menu text
        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))
        screen.blit(render_menu, (430, 550))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and 430 <= mx <= 550 and 570 <= my <= 600:
                menu = False

        pygame.display.flip()

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]: # K_RETURN - нажатие на Enter
            break

def appleSpawn(apple):
    while apple in snake or apple in walls:
        apple = randrange(0, width, block), randrange(0, height, block)
    return apple


main_menu()

# add walls
# mode 1
for i in range(50):
    wall = randrange(0, width, block), randrange(0, width, block)
    walls.append(wall)

while True:
    screen.blit(game_background, (0, 0))

    # time
    current_time = datetime.datetime.now()
    if current_time.second >= lastTime + 5:
        lastTime = current_time.second
        apple = randrange(0, width, block), randrange(0, height, block)
        while apple in snake or apple in walls:
            apple = randrange(0, width, block), randrange(0, height, block)

    # drawing snake, apple, walls
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))
    if score % 3 == 0 and score > 0:
        pygame.draw.rect(screen, pygame.Color('orange'), (*orange,block,block))
    for i, j in walls:
        pygame.draw.rect(screen, pygame.Color('black'), (i, j, block - 1, block - 1))

    # show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))    
    render_level = font_level.render(f'LEVEL: {level}', True, pygame.Color('aqua'))
    screen.blit(render_level, (880,5))
    
    # snake movement
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]

    # game over
    if x < 0 or x > width - block or y < 0 or y > height - block\
    or len(snake) > len(set(snake)) or snake[-1] in walls:
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            screen.blit(render_end, (335, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    # eating food
    if snake[-1] == apple:
        lastTime = current_time.second
        while apple in snake or apple in walls:
            apple = randrange(0, width, block), randrange(0, height, block)
        length += 1
        score += 1
        fps += 0.5
        if score % 3 == 0 and score > 0:
            level += 1
        if level > 3:
            score += 3
            length += 2 

    if snake[-1] == orange:
        while orange in snake or orange in walls:
            orange = randrange(0, width, block), randrange(0, height, block)
        length += 2
        score += 2
        fps += 1
        if score % 3 == 0 and score > 0:
            level += 1
        if level > 3:
            score += 3
            length += 2 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}