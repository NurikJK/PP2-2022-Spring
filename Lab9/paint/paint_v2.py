import pygame
import random 

# basic elements
WIDTH, HEIGHT = 1200, 760   # base window size
FPS = 60
draw = False                # pressing, pinching - draw, pressed - do not draw 
lastPos = (0, 0)            # basic position
radius = 5                 # base radius for tools
color = 'red'              # basic color
mode = 'pen'                # basic mode
colorBG = 'white'           # background color

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white')) # we paint it in white so that it is not updated inside the cycle
fontRadius = pygame.font.SysFont('Arial', 66, bold=True)


#---------------------------------------------------------------------------------------------#


def drawLine(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)


def drawCircle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)


def drawRectangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr = abs(x1 - x2)
    heightr = abs(y1 - y2)
    pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, heightr), width)


def drawSquare(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widths = abs(x2-x1)
    heights = abs(y2-y1)
    mn = min(widths,heights)
    pygame.draw.rect(screen, pygame.Color(color), (x1,y2,mn,mn), width)


def drawRhombus(screen,start,end,width,color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    a = (x1,(y1+y2)/2)
    b = ((x1+x2)/2,y1)
    c = (x2,(y1+y2)/2)
    d = ((x1+x2)/2,y2)
    pygame.draw.polygon(screen, pygame.Color(color), (a,b,c,d),width)


def drawRightTriangle(screen,start,end,width,color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    z1 = x1
    z2 = y2
    pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1),(x2,y2),(z1,z2)),width)


def drawEquilateralTriangle(screen,start,end,width,color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    z1 = (abs(x1)+abs(x2))/2
    height_et = (3**0.5) * (abs(x2-x1))/2
    if y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1),(x2,y2),(z1,y2 - height_et)),width)
    else:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1,y1),(x2,y2),(z1,y1-height_et)),width)


#--------------------------------------------------------------------------------------------#


while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        # Keyboard press
        if event.type == pygame.KEYDOWN:
            # modes
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_RSHIFT:
                mode = 'globalerase'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_a:
                mode = 'rhombus'
            if event.key == pygame.K_t:
                mode = 'righttriangle'
            if event.key == pygame.K_d:
                mode = 'equilateraltriangle'
            if event.key == pygame.K_e:
                mode = 'erase'
            # colors
            if event.key == pygame.K_y:
                color = 'yellow'
            if event.key == pygame.K_b:
                color = 'blue'
            if event.key == pygame.K_l:
                color = 'red'
            if event.key == pygame.K_g:
                color = 'gray'
            # random color
            if event.key == pygame.K_z:
                color = (random.randrange(256), random.randrange(256), random.randrange(256))
            # radius limits
            if event.key == pygame.K_UP:
                radius = min(200, radius + 1)   # max limit of radius
            if event.key == pygame.K_DOWN:
                radius = max(1, radius - 1)     # min limit of radius


        # Mouse press
        if event.type == pygame.MOUSEBUTTONDOWN: 
            draw = True
            if mode == 'pen':
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos


        # Mouse release
        if event.type == pygame.MOUSEBUTTONUP: 
            if mode == 'rectangle':
                drawRectangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, prevPos, event.pos, radius, color)
            elif mode == 'globalerase':
                screen.fill(pygame.Color('white'))
            elif mode == 'square':
                drawSquare(screen, prevPos, event.pos, radius, color)
            elif mode == 'rhombus':
                drawRhombus(screen, prevPos, event.pos, radius, color)
            elif mode == 'righttriangle':
                drawRightTriangle(screen, prevPos, event.pos, radius, color)
            elif mode == 'equilateraltriangle':
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)
        
        # Mouse move
        if event.type == pygame.MOUSEMOTION: 
            if draw and mode == 'pen':
                drawLine(screen, lastPos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, lastPos, event.pos, radius, BGcolor)
            lastPos = event.pos
        

    # show radius and color
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = fontRadius.render(f'{radius}', True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))


    # display
    pygame.display.flip()
    clock.tick(FPS)
