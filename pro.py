import pygame

pygame.init()

w = 1024
la = 720
true = True
ima = 0
key = pygame.key.get_pressed()
i1 = pygame.image.load("img/1.jpg")
i1 = pygame.transform.scale(i1, (1920, 1080))
winfll = False
font = pygame.font.Font("img/PixelifySans-VariableFont_wght.ttf", 64)
txt1 = font.render("no image avalible ", True, (0, 255, 255))
# i2 = pygame.image.load("img/i2)
# i3 = pygame.image.load("img/i3234)
# i4 = pygame.image.load("img/i4)




window = pygame.display.set_mode((w, la))

while true:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            true = False

            pygame.key.get_pressed()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            true = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            window = pygame.display.set_mode()

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
        print("no image found")
        window.blit(txt1, (0, 100))
    if ima == 2:
        window.blit(txt1, (0, 100))
    if ima == 3:
        window.blit(txt1, (0, 100))
    if ima == 4:
        window.blit(txt1, (0, 100))



    pygame.display.update()
