import pygame
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)

win = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
win.fill(WHITE)
# kvadrat = pygame.Rect(0,0,100,100)




finish = False
run = True
image = pygame.image.load("asset_level/bush_1.png")

image = pygame.transform.scale(image,(200,200))
image1 = pygame.image.load("asset_level/big_stick.png")
image1 = pygame.transform.scale(image1,(200,200))
image2 = pygame.image.load("asset_level/big_rock.png")
image2 = pygame.transform.scale(image2,(200,200))
image3 = pygame.image.load("asset_level/one_block.png")
image3 = pygame.transform.scale(image3,(200,200))
image4 = pygame.image.load("asset_level/sprout_1.png")
image4 = pygame.transform.scale(image4,(200,200))
spisok = [image,image1,image2,image3,image4]
x=0
y=0

while run:
    for i in range(len(spisok)):
        win.blit(spisok[i],(x,y))
        x+=100
        y+=100
    # win.blit(image,(0,0))
    # win.blit(image1,(100,0))
    # win.blit(image2,(200,0))
    # win.blit(image3,(300,0))
    # win.blit(image4,(400,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    # pygame.draw.rect(win,RED,kvadrat)
    pygame.time.delay(50)
    pygame.display.update()