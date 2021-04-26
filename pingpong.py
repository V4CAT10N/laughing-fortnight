from pygame import *

#Window and BG + speed

win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("Ping Pong")
speed = 10
background = transform.scale(image.load("table.png"),(win_width, win_height))

#Classes

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

#Sprites

racket = Player('racket.png', 10, 200, 25, 100, 5)
rackett = Enemy('racket.png', win_width-35, 200, 25, 100, 5)
ball = GameSprite('ball.png', 325,225,50,50,10)

clock = time.Clock()
FPS = 60
game = True
finish = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0,0))
        ball.update()
        racket.update()
        rackett.update()

    rackett.reset()
    ball.reset()
    racket.reset()
    display.update()
    clock.tick(FPS)