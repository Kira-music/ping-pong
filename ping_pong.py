from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 595:
            self.rect.y += self.speed

    def update2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 595:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__(player_image, player_x, player_y, player_speed, w, h)
        self.speed_x = player_speed
        self.speed_y = player_speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y >= 459 or self.rect.y <= 1:
            self.speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            self.speed_x *= -1





window = display.set_mode((700, 500))
display.set_caption('Ping_pong')

background = transform.scale(image.load('images.jpg'), (700, 500))

clock = time.Clock()
FPS = 60

racket1 = Player('racket.png', 20, 250, 15, 100, 100)

racket2 = Player('racket.png', 590, 250, 15, 100, 100)

ball = Enemy('ball.png', 200, 300, 1, 40, 40)

game = True

while game:
    window.blit(background, (0, 0))

    racket1.update()
    racket1.reset()

    racket2.update2()
    racket2.reset()

    ball.update()
    ball.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
