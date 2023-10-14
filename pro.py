import pygame
from time import sleep

pygame.init()

w = 1024
la = 720
true = True
ima = 0
key = pygame.key.get_pressed()
i1 = pygame.image.load("img/i1.jpg")
i1 = pygame.transform.scale(i1, (1920, 1080))
winfll = False
font = pygame.font.Font("img/t2.ttf", 64)
txt1 = font.render("Ricordati che ", True, (0, 255, 255))
txt2 = font.render("Primma ", True, (0, 255, 255))
txt3 = font.render("Durante e dopo in un edificio", True, (0, 255, 255))
txt4 = font.render("Durante e dopo all'aperto", True, (0, 255, 255))
bgw = False
ax = 0
ay = 0
at = 10

i2 = pygame.image.load("img/i2.jpg")
i2 = pygame.transform.scale(i2, (1920, 1080))
i3 = pygame.image.load("img/ii3.jpg")
i4 = pygame.image.load("img/ii4.jpg")
i3 = pygame.transform.scale(i3, (1920, 1080))
i4 = pygame.transform.scale(i4, (1920, 1080))
b = pygame.image.load("img/Black.png")
b = pygame.transform.scale(b, (1920, 1080))

window = pygame.display.set_mode((w, la))

while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False

            pygame.key.get_pressed()


        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            true = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            window = pygame.display.set_mode()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            window = pygame.display.set_mode((1024, 720))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            ima = 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            ima = 2

        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            ima = 3

        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            ima = 4

    print(ima)

    if ima == 1:
        window.blit(b, (0, 0))
        print("no image found")
        window.blit(txt1, (ax, 0))
        pygame.display.update()
        if ax == 20:
            at = 9
            ax = ax + at

        if ax == 40:
            at = 8
            ax = ax + at

        if ax == 60:
            at = 7

        if ax == 80:
            at = 6

        if ax == 100:
            at = 5

        if ax == 120:
            at = 4

        if ax == 140:
            at = 3

        if ax == 160:
            at = 2

        if ax == 180:
            at = 1

        if ax == 200:
            at = 0


        #sleep(1)
        #window.blit(i1, (0, 0))
        ima = 1

    if ima == 2:
        window.blit(b, (0, 0))
        window.blit(txt2, (0, 0))
        pygame.display.update()
        sleep(1)
        window.blit(i2, (0, 0))
        ima = 10

    if ima == 3:
        window.blit(b, (0, 0))
        window.blit(txt3, (0, 0))
        pygame.display.update()
        sleep(1)
        window.blit(i3, (0, 0))
        ima = 10
    if ima == 4:
        window.blit(b, (0, 0))
        window.blit(txt4, (0, 0))
        pygame.display.update()
        sleep(1)
        window.blit(i4, (0, 0))
        ima = 10


    pygame.display.update()
