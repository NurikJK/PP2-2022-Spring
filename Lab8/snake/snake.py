import pygame
from random import randrange

# elementary thing
size = width, height = 1050, 650
block = 25

x, y = randrange(0, width, block), randrange(0, height, block) # coordinate for snake
apple = randrange(0, width, block), randrange(0, height, block) # coordinate for apple
orange = randrange(0, width, block), randrange(0, height, block) # coordinate for orange
dirs = {'W': True, 'S': True, 'A': True, 'D': True} 
length = 1 # snake lenght
score = 0
level = 0
snake = [(x, y)] # append x,y to snake
dx, dy = 0, 0 # coordinate to move
fps = 10


pygame.init()
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
# for labels in the menu
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)
font_menu = pygame.font.Font('font.ttf', 85)
# img
game_background = pygame.image.load('game_background.jpg').convert()
menu_background = pygame.image.load('menu_background.jpg').convert()

# function for main menu
def main_menu():
    menu = True
    while menu:
        screen.blit(menu_background, (0, 0))
        
        # menu text
        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))
        screen.blit(render_menu, (430, 550))

        # menu event
        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()
            # exit
            if event.type == pygame.QUIT:
                exit()
            # press button to start
            if event.type == pygame.MOUSEBUTTONDOWN and 430 <= mx <= 550 and 570 <= my <= 600:
                menu = False

        pygame.display.flip()
        # to start
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]: 
            break

main_menu()

# game 
while True:
    screen.blit(game_background, (0, 0))

    # drawing snake, apple, orange
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))
    if score % 3 == 0 and score > 0:
        pygame.draw.rect(screen, pygame.Color('orange'), (*orange,block,block))

    # show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))  
    # show level  
    render_level = font_level.render(f'LEVEL: {level}', True, pygame.Color('aqua'))
    screen.blit(render_level, (880,5))
    
    # snake movement
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]

    # game over
    if x < 0 or x > width - block or y < 0 or y > height - block\
    or len(snake) > len(set(snake)) or snake in walls:
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            screen.blit(render_end, (335, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()


    # eating food
    # apple 
    if snake[-1] == apple:
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
    # orange
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
    # event
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
