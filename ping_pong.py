from pygame import*

font.init()

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
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

    def update2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

lost1 = 0
lost2 = 0

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

background = transform.scale(image.load('background.png'), (700, 500))

clock = time.Clock()
FPS = 60

font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 25)

racket1 = Player('fork.png', 20, 250, 15, 30, 120)

racket2 = Player('fork.png', 630, 250, 15, 30, 120)

ball = Enemy('donut.png', 200, 300, 5, 60, 50)

game = True

finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))

        racket2.update()
        racket2.reset()

        racket1.update2()
        racket1.reset()

        ball.update()
        ball.reset()

        text_1lose = font1.render('Gamer 1 lose', 1, (231, 84, 128))
        text_2lose = font1.render('Gamer 2 lose', 1, (231, 84, 128))

        gamer1 = font2.render('Gamer 1:'+ str(lost1), 1, (205, 0, 205))
        window.blit(gamer1, (20, 30))

        gamer2 = font2.render('Gamer 2:'+ str(lost2), 1, (205, 0, 205))
        window.blit(gamer2, (560, 30))

        if ball.rect.x < 5:
            lost2 += 1
            ball.rect.x = 200
            ball.rect.y = 300

        if ball.rect.x > 680:
            lost1 += 1
            ball.rect.x = 200
            ball.rect.y = 300

        if lost1 == 3:
            window.blit(text_2lose, (250, 185))
            finish = True

        if lost2 ==3:
            window.blit(text_1lose, (250, 185))
            finish = True

    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
