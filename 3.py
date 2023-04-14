import pygame


pygame.init()
width = 490
lenght = 490
screen = pygame.display.set_mode((width, lenght))

done = False

x = lenght / 2
y = width / 2
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    pressed = pygame.key.get_pressed()

    
    if pressed[pygame.K_UP] and y >= 30:
        y -= 20
    if pressed[pygame.K_DOWN] and y <= width - 30:
        y += 20
    if pressed[pygame.K_LEFT] and x >= 30:
        x -= 20
    if pressed[pygame.K_RIGHT] and x < lenght - 30:
        x +=20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0),(x, y), 25, 0)
    
    pygame.display.flip()
    clock.tick(60)




