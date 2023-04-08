import pygame, os, random
from sound import *
from sprite import *
pygame.init()
pygame.mixer.init()
randomsus = "#ffffff"
lvl = 1
def path(path): return os.path.join(os.path.abspath(__file__ + '/..'), path)

def sus():
    print('ви вийграли!')
    sp1.x, sp1.y = 100, 600
    vin.play()

theme = Sound('sprite/jungles.ogg', 0.1)
lose = Sound('sprite/kick.ogg')
vin = Sound('sprite/money.ogg')


win_size = 1000, 700
win = pygame.display.set_mode((win_size))
bg = pygame.transform.scale(pygame.image.load(path("sprite/background.jpg")), (win_size))
fps = pygame.time.Clock()

sp1 = Sprite(100, 600, 60, 60, 'sprite/hero.png', win, 1000, 700)
sp2 = Sprite(600, 400, 60, 60, 'sprite/cyborg.png', win, 1000, 640)

#wall = Wall(200, 300, 400, 100, "#11ad6b", win)

theme.play()


wall3 = Wall(0, 100, 200, 10, "#ffffff", win)
wall5 = Wall(550, 100, 200, 10, "#ffffff", win)
wall6 = Wall(750, 100, 500, 10, "#ffffff", win)
wall1 = Wall(200, 270, 10, 600, "#ffffff", win)
wall2 = Wall(200, 100, 350, 10, "#ffffff", win)
wall4 = Wall(800, 530, 10, 600, "#ffffff", win)
wall7 = Wall(560, 520, 250, 10, '#ffffff', win)
wall8 = Wall(560, 320, 250, 10, "#ffffff", win)
wall9 = Wall(550, 100, 10, 430, "#ffffff", win)
wall10 = Wall(350, 100, 10, 430, "#ffffff", win)

map = [wall1, wall2, wall4, wall6, wall7, wall8, wall9, wall10]

treasure = Sprite(830, 500, 150, 150, 'sprite/treasure.png', win, 1000, 700)

right = 2

pygame.display.set_icon(pygame.image.load(path('sprite/OIP.ico')))

while True:
    fps.tick(144)
    pygame.display.flip()
    win.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    treasure.show()
    wall3.show()
    wall5.show()
    for i in map:
        i.show()
    sp1.show()
    sp2.show()
    sp1.control(pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s, 2)
    for i in map:
        if sp1.r.colliderect(i) or sp1.r.colliderect(sp2.r):
            print('ні не так)')
            lose.play()
            sp1.x, sp1.y = 100, 600

    if right % 2 == False:
        #print("true", str(right))
        sp2.x += 1
        sp2.r.x += 1

    else:
        #print("False", str(right))
        sp2.x -= 1
        sp2.r.x -= 1

    if sp2.x == 900:
        right += 1

    if sp2.x == 600 or sp2.x > 901:
        right += 1

    if sp1.r.colliderect(treasure.r):
        sus()
        lvl += 1

    if sp2.x > 901:
        right = 2
        sp2.x, sp2.r.x = 600, 600
    if lvl == 3: break
    if lvl == 2:

        wall1 = Wall(0, 520, 800, 10, randomsus, win)
        wall2 = Wall(160, 380, 350, 10, randomsus, win)
        wall3 = Wall(500, 280, 500, 10, randomsus, win)
        wall4 = Wall(500, 280, 10, 100, randomsus, win)
        wall5 = Wall(0, 280, 400, 10, randomsus, win)
        wall6 = Wall(400, 150, 500, 10, randomsus, win)
        wall7 = Wall(400, 150, 10, 140, randomsus, win)
        wall8 = Wall(400, 0, 10, 150, randomsus, win)
        wall9 = Wall(250, 0, 10, 160, randomsus, win)
        wall10 = Wall(1000, 1000, 10, 430, randomsus, win)

        map = [wall1, wall2, wall3, wall4, wall5, wall6, wall9, wall10]
        wall7.show()
        treasure.x, treasure.r.x = 10, 10
        treasure.y, treasure.r.y = 10, 10
        for i in map:
            if sp1.r.colliderect(i) or sp1.r.colliderect(sp2.r) or sp1.r.colliderect(wall8.rect):
                print('ні не так)')
                lose.play()
                sp1.x, sp1.y = 100, 600