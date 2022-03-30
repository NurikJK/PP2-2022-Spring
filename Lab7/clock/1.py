import pygame, datetime
from math import sin,cos,pi

size = 800
center = (size/2,size/2)
clockRadius = 400
digits = {1: 'I', 2:'II',3:'III',4:'IV', 5:'V',6:'VI',7:'VII',8:'VII',9:'IX',10:'X',11:'XI',12:'XII'}
pygame.init()
screen = pygame.display.set_mode([size,size])
# rename
pygame.display.set_caption('Mickey Mouse Clock')
clock = pygame.time.Clock()

#import img from folder img
mickey = pygame.transform.scale(pygame.image.load('img\\mickey.png'), (int(574 * 1.25), int(485 * 1.25)))
righthand = pygame.transform.scale(pygame.image.load('img\\righthand.png'), (594 // 2, 322 // 2))
lefthand = pygame.transform.scale(pygame.image.load('img\\lefthand.png'), (770 // 2, 230 // 2))

# functions for clock
#convert numbers to roman numbers
def numbers(number, number_size, position):
    font = pygame.font.SysFont('Arial', number_size, bold=True)
    text = font.render(number, True, pygame.Color('white'))
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)
# 
def polar_to_cartesian(r, theta):
    x, y = r * sin(pi * theta / 180), r * cos(pi * theta / 180)
    return x + size / 2, -(y - size / 2)
# rotate img
def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0]- originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

while True:
    # draw
    screen.fill(pygame.Color('white'))
    pygame.draw.circle(screen, pygame.Color('black'), center, clockRadius-10,10) # draw black circle outside
    pygame.draw.circle(screen, pygame.Color('gray'), center, clockRadius-20)#draw gray circle inside
    pygame.draw.circle(screen, pygame.Color('black'), center, 10)#draw center dot   

    # roman numbers on the background
    [numbers(digits[i], 80, polar_to_cartesian(clockRadius - 70, i * 30)) for i in range(1,13)]

    # draw the second indicators on the clock
    for i in range(0,360,6):
        if i % 5 != 0:
            pygame.draw.line(screen, pygame.Color('black'), polar_to_cartesian(clockRadius - 15, i), polar_to_cartesian(clockRadius-30,i),2)
        else:
             pygame.draw.line(screen, pygame.Color('black'), polar_to_cartesian(clockRadius - 15, i), polar_to_cartesian(clockRadius-30,i),6)

    # mickey
    screen.blit(mickey,(40,70))
    # time
    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute

    # second
    theta = second * (360 / 60)
    blitRotate(screen, lefthand, center, (lefthand.get_width() / 2 - 145, lefthand.get_height() / 2), theta - 87)

    # minute
    theta = (minute + second / 60) * (360 / 60)
    blitRotate(screen, righthand, center, (righthand.get_width() / 2 + 110, righthand.get_height() / 2 + 75), theta + 75)

    # display
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

pygame.quit()
