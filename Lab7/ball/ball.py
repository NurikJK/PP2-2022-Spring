import pygame 
from random import randrange
size = 600
radius,step = 30,20
x, y = randrange(0, size, radius), randrange(0, size, radius)

pygame.init()
screen = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()

while True:
    # close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
    # control keyboard
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y-=step
    if pressed[pygame.K_s]: y+=step
    if pressed[pygame.K_a]: x-=step
    if pressed[pygame.K_d]: x+=step
    # draw background and ball   
    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('red'), (x,y), radius)
    # the boarders
    if x < 15 : x+=step
    elif x > size - 10: x -= step
    elif y < 15: y += step
    elif y > size - 10: y -= step
    # display
    pygame.display.flip()
    clock.tick(60)
