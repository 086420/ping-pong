from pygame import *
win_width = 700   
win_height = 500
window = display.set_mode((700, 500))

display.set_caption("ping")
background = transform.scale(image.load("low-poly-texture.jpg"),(700, 500))
game = True
finish = False
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y ))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height -150:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y  < win_height -150:
            self.rect.y += self.speed
player1 = Player('ракеткалев.png', 5, 400,100, 100, 4)
player2 = Player('ракеткаправ.png', 600, 400,100, 100, 4)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        player1.update_l()
        player2.update_r()
        player1.reset()
        player2.reset()
    display.update()
    clock.tick(FPS)