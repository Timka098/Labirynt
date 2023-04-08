import pygame, os
pygame.init()


def path(path): return os.path.join(os.path.abspath(__file__ + '/..'), path)

class Sprite:
    def __init__(self, pos_x, pos_y, width, heidth, image, global_win, win_width, win_height):
        self.winw = win_width
        self.winh = win_height
        self.x = pos_x
        self.y = pos_y
        self.image = image
        self.win = global_win
        self.width = width
        self.height = heidth
        self.r = pygame.Rect(self.x, self.y, self.width, self.height)
        
        self.main = pygame.transform.scale(pygame.image.load(path(self.image)), (self.width, self.height))

    def show(self):
        self.win.blit(self.main, (self.x, self.y))
        #pygame.draw.rect(self.win, (255, 255, 255), self.r, 5)

    def control(self, x, xx, y, yy, speed):
        pressed_keys = pygame.key.get_pressed()
        self.r.x = self.x
        self.r.y = self.y
        if pressed_keys[x] and self.x < self.winw-5-self.width:
            self.x += speed
            #self.r.x += speed
        if pressed_keys[xx] and self.x > 5:
            self.x -= speed
        if pressed_keys[y] and self.y > 5:
            self.y -= speed
        if pressed_keys[yy] and self.y < self.winh-self.height:
            self.y += speed



class Wall:
    def __init__(self, x, y, width, height, color, win):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.win = win
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def show(self):
        pygame.draw.rect(self.win, self.color, self.rect, 99999999)