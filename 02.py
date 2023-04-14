
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("adele is the best")
image = pygame.image.load('adeele.jpg')
picture = pygame.transform.scale(image, (700, 400))
imageX = 50
imageY = 75
def adele():
    screen.blit(picture, (imageX, imageY))

play = pygame.image.load('play.png')
pause = pygame.image.load('pause.png')
back = pygame.image.load('back.png')
nextt = pygame.image.load('nextt.png')

play1 = pygame.transform.scale(play, (60, 60))
pause1 = pygame.transform.scale(pause, (60, 60))
back1 = pygame.transform.scale(back, (60, 60))
nextt1 = pygame.transform.scale(nextt, (60, 60))


playX = 150
playY = 515
pauseX = 300
pauseY = 515
backX = 600
backY = 515
nexttX = 450
nexttY = 515


def buttons():
    screen.blit(play1, (playX, playY))
    screen.blit(pause1, (pauseX, pauseY))
    screen.blit(back1, (backX, backY))
    screen.blit(nextt1, (nexttX, nexttY))
    


songs = ["adele1.mp3", "dele2.mp3", "adele3.mp3", "adele4.mp3"]
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            songs = songs[1:] + [songs[0]]
            pygame.mixer.music.load(songs[0])
            pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            songs = [songs[-1]] + songs[:-1]
            pygame.mixer.music.load(songs[0])
            pygame.mixer.music.play(0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pygame.mixer.music.unpause()


    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(20, 50, 760, 450)) 
    adele()
    buttons()
    pygame.display.flip()



