import pygame, sys
import random 
import time

pygame.init()
height, width = 600, 400
speed, score = 5, 0
FPS = 90
clock = pygame.time.Clock()

# label
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('GAME OVER', True, (0, 0, 0))

# img
bg = pygame.image.load('img\\AnimatedStreet.png')

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Street Racer')
# music
pygame.mixer.music.load('sound\\background.wav')
pygame.mixer.music.play(-1)

# class for enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img\\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score, bonus, all_sprites
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            self.rect.top = 0 
            self.rect.center = (random.randint(40, width - 40), 0)

            bonus.add(Co)
            all_sprites.add(Co)


    def draw(self, surface):
        surface.blit(self.image, self.rect) 

# class for coins
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img\\coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(60, width - 60), 0)

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            self.rect.top = 0 
            self.rect.center = (random.randint(50, 350), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)                     


# class for Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img\\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 40:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.right < width-40:
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(7, 0) 
        if self.rect.bottom < height:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0, 7)                
        if self.rect.bottom > 0:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0, -7)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  

# introduce
P1 = Player()
E1 = Enemy()
Co = Coins()

# Creating Spritese Group
enemies = pygame.sprite.Group()
enemies.add(E1)
bonus = pygame.sprite.Group()
bonus.add(Co)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(Co)

# New event during the game
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 5000)


while True:
    # events
    for event in pygame.event.get():
        if event.type == inc_speed: 
            speed+=1 # speed increas
        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  

    # screen hints
    screen.blit(bg, (0, 0))
    scores = font_small.render(str(score), True, (0, 0, 0))
    screen.blit(scores, (10,10))


    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # collision
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('sound\\crash.wav').play()              
        time.sleep(0.5)
        screen.fill((255, 0, 0))
        screen.blit(game_over, (30, 250)) 
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)    
        pygame.quit()
        sys.exit()

    # take a coin
    if pygame.sprite.spritecollideany(P1, bonus):
        pygame.mixer.Sound('sound\\coin.mp3').play(0)
        for entity in bonus:
            entity.kill()
            Co = Coins()
            score+=1

    pygame.display.update()
    clock.tick(60)      
