import pygame,os

size = 800
musics = []
pygame.init()
screen = pygame.display.set_mode([size,size])
clock = pygame.time.Clock()
player_icon = pygame.transform.scale(pygame.image.load('img\\player_mp3.jpg'), (800,800))
paused = True
left = right = mid = False
current = 0
for i in os.listdir("C:\\pygame\\player\\playlist"):
    music = pygame.mixer.Sound("C:\\pygame\\player\\playlist\\" + str(i))
    musics.append(music)

while True:
    key = pygame.key.get_pressed()

    # start play music
    if key[pygame.K_UP]:
        musics[current].play()
        paused = False
    #pause and unpause
    if key[pygame.K_DOWN]:
        if paused == True:
            pygame.mixer.unpause()
            paused = False
        elif paused == False:
            pygame.mixer.pause()
            paused = True
    #next music
    if key[pygame.K_RIGHT]:
        musics[current].stop()
        current += 1
        if current == len(musics) :
            current = 0
        musics[current].play()
    #prev music
    if key[pygame.K_LEFT]:
        musics[current].stop()
        current -= 1
        if current <= -1:
            current = len(musics) - 1
        musics[current].play()

    # draw screen
    screen.blit(player_icon, (0,0))

    # display
    pygame.display.flip()
    clock.tick(60)
    #close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


pygame.quit()
