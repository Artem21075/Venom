import pygame

screen = pygame.display.set_mode((800, 600))

x = 400
y = 300
r = 50
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
color = YELLOW
speed = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), r)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] == True:
        y = y - speed
    if pressed[pygame.K_DOWN] == True:
        y = y + speed
    if pressed[pygame.K_LEFT] == True:
        x = x - speed
    if pressed[pygame.K_RIGHT] == True:
        x = x + speed

    if x > 800:
        x = 0
    elif x < 0:
        x = 800
    if y < 0:
        y = 600
    elif y > 600:
        y = 0

    if x > 650 or x < 150 or y > 450 or y < 150:
        color = RED
        speed = 0.5
    else:
        color = YELLOW
        speed = 1
        
    pygame.display.update()