#Создай собственный Шутер!
from pygame import *
from random import *

mixer.init()
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

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 15, 20)
        bullets.add(bullet)

lost = 0

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.rect.x = randint(0, 620)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):    
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        
     

window = display.set_mode((700, 500))
display.set_caption('Shooter')

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

mixer.music.load('space.ogg')
mixer.music.play()

rocket = Player('rocket.png', 325, 400, 10, 80, 100)

monsters = sprite.Group()
for i in range(6):
    monster = Enemy('ufo.png',  randint(0, 620), 0, randint(1, 3), 80, 50)
    monsters.add(monster)

bullets = sprite.Group()

asteroids = sprite.Group()
for i in range(3):
    asteroid = Enemy('asteroid.png', randint(0, 620), 0, 1, 80, 50)
    asteroids.add(asteroid)



clock = time.Clock()
FPS = 60

game = True

font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 90)

win = 0

while game:
    window.blit(background, (0, 0))

    rocket.update()
    rocket.reset()

    monsters.update()
    monsters.draw(window)

    asteroids.update()
    asteroids.draw(window)

    bullets.update()
    bullets.draw(window)

    text_lost = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
    window.blit(text_lost, (10, 30))

    text_win = font1.render('Счёт: ' + str(win), 1, (255, 255, 255))
    window.blit(text_win, (10, 10))

    text_youlose = font2.render('you lose',  1, (255, 0, 0))

    text_youwin = font2.render('you win',  1, (0, 255, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
    
    sprite_list = sprite.groupcollide(monsters, bullets, True, True)
    for _ in sprite_list:
        win += 1
        monster = Enemy('ufo.png',  randint(0, 620), 0, randint(1, 5), 80, 50)
        monsters.add(monster)

    if lost == 15:
        window.blit(text_youlose, (250, 175))
        game = False

    if win >= 10:
        window.blit(text_youwin, (250, 175))
        game = False

    sprite_list = sprite.spritecollide(rocket, asteroids, True)
    if len(sprite_list):
        window.blit(text_youlose, (250, 175))
        game = False

    

    clock.tick(FPS)
    display.update()






# from pygame import *
# from random import randint
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup, QTextEdit
# from random import shuffle

# mixer.init()
# font.init()

# class Question():
#     def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
#         self.question = question
#         self.right_answer = right_answer
#         self.wrong1 = wrong1
#         self.wrong2 = wrong2
#         self.wrong3 = wrong3

# class Text(sprite.Sprite):
#     def __init__(self, text, x, y, colour1, colour2, colour3):
#         super().__init__()
#         self.text = text
#         self.colour1 = colour1
#         self.colour2 = colour2
#         self.colour3 = colour3
#         self.font_ = font.Font(None, 40)
#         self.label = self.font_.render(self.text, True, (self.colour1,self.colour2,self.colour3))
#         self.rect = self.label.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#     def reset(self):
#         window.blit(self.label, (self.rect.x, self.rect.y))

# class GameSprite(sprite.Sprite):
#     def __init__(self, game_image, speed, x, y, w, h):
#         super().__init__()
#         self.image = transform.scale(image.load(game_image), (w,h))
#         self.speed = speed
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#     def reset(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))

# class Player(GameSprite):
#     def update(self):
#         keys_pressed = key.get_pressed()
#         if keys_pressed[K_a] and self.rect.x > 5:
#             self.rect.x -= self.speed
#         if keys_pressed[K_d] and self.rect.x < 635:
#             self.rect.x += self.speed
#         if keys_pressed[K_w] and self.rect.y > 5:
#             self.rect.y -= self.speed
#         if keys_pressed[K_s] and self.rect.y < 435:
#             self.rect.y += self.speed

# class Enemy_up(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         if self.rect.y >= 540:
#             self.rect.x = randint(0, 640)
#             self.rect.y = 0

# class Enemy_left(GameSprite):
#     def update(self):
#         self.rect.x += self.speed
#         if self.rect.x >= 740:
#             self.rect.y = randint(0, 460)
#             self.rect.x = 0

# class Enemy_right(GameSprite):
#     def update(self):
#         self.rect.x -= self.speed
#         if self.rect.x <= -40:
#             self.rect.y = randint(0, 460)
#             self.rect.x = 740

# class Enemy_down(GameSprite):
#     def update(self):
#         self.rect.y -= self.speed
#         if self.rect.y <= 0:
#             self.rect.x = randint(0, 640)
#             self.rect.y = 540

# def choice():
#     if pbt_glav.text() == 'Ответить':
#         check_answer()
#     elif pbt_glav.text() == 'Перейти к тесту':
#         next_question()
#     elif pbt_glav.text() == 'Закрыть програму':
#         app.quit()

# def show_question():
#         Group_right.hide()
#         Group_question.show()
#         pbt_glav.setText('Ответить')

# def show_right():
#     qlist.append(Question('Назовите спутник Юпитера?', 'Европа', 'Азия', 'Промитей',   'Антарктида'))
#     qlist.append(Question('Диаметр колец Сатурна?', '250000', '7000', '5000', '230000'))
#     qlist.append(Question('Какой бог не связан с планетами', 'Борей', 'Зевс', 'Гермес', 'Афрадита'))
#     qlist.append(Question('Какого цвета Солнце?','Белое',  'жёлтое', 'Casa Blanca',  'Красное'))
#     shuffle(qlist)

# app = QApplication([])
# main_win = QWidget()
# main_win.setWindowTitle('Инфотест')
# main_win.right = 0
# main_win.total = 0
# main_win.wrong = 0
# main_win.score = -1
# pbt_glav = QPushButton('Перейти к тесту')
# text_question = QLabel('Вопрос')
# rbt1 = QRadioButton('1')
# rbt2 = QRadioButton('2')
# rbt3 = QRadioButton('3')
# rbt4 = QRadioButton('4')
# Group_question = QGroupBox('Вопросы')
# right_answer = QLabel(f'Всего вопросов {len(qlist)}')
# your_right = QLabel('Всего правильных')
# your_wrong = QLabel('Всего неправильных')
# Group_right = QGroupBox('Результаты')

# Group = QGroupBox()

# answers = [rbt1, rbt2, rbt3, rbt4]

# vline_glav_text = QVBoxLayout()
# hline_text = QHBoxLayout()
# vline_text = QVBoxLayout()
# vline = QVBoxLayout()


# hline1_group_question = QHBoxLayout()
# hline2_group_question = QHBoxLayout()
# vline_group_question = QVBoxLayout()
# vline_minigrup = QVBoxLayout()

# hline1_group_question.addWidget(rbt1)
# hline1_group_question.addWidget(rbt2)
# hline2_group_question.addWidget(rbt3)
# hline2_group_question.addWidget(rbt4)
# vline_minigrup.addLayout(hline1_group_question)
# vline_minigrup.addLayout(hline2_group_question)
# Group.setLayout(vline_minigrup)
# vline_group_question.addWidget(text_question, alignment = Qt.AlignCenter)
# vline_group_question.addWidget(Group, alignment = Qt.AlignCenter)
# Group_question.hide()
# Group_question.setLayout(vline_group_question)

# vline_group_right = QVBoxLayout()

# vline_group_right.addWidget(right_answer, alignment = Qt.AlignCenter)
# vline_group_right.addWidget(your_right, alignment = Qt.AlignCenter)
# vline_group_right.addWidget(your_wrong, alignment = Qt.AlignCenter)
# Group_right.hide()
# Group_right.setLayout(vline_group_right)

# vline.addWidget(Group_question)
# vline.addWidget(Group_right)
# vline.addWidget(pbt_glav)

# main_win.setLayout(vline)

# RadioGroup = QButtonGroup()
# RadioGroup.addButton(rbt1)
# RadioGroup.addButton(rbt2)
# RadioGroup.addButton(rbt3)
# RadioGroup.addButton(rbt4)




# pbt_glav.clicked.connect(choice)


# main_win.show()
# app.exec_()

# window = display.set_mode((700,500))
# display.set_caption('Смертельный полёт')
# background = transform.scale(image.load('space.png'),(700,500))
# bg_y = 0

# player = Player('rocket.png', 10, 350, 400, 60, 50)

# meteors_up = sprite.Group()
# meteors_left = sprite.Group()
# meteors_right = sprite.Group()
# meteors_down = sprite.Group()

# answer_ = ['asd','sdsdfa','ASD','ARGDF','`1']


# for i in range(4):
#     random = randint(1,3)
#     image_rocket = 0
#     if random == 1:
#         image_rocket = 'астеройд.png'
#     if random == 2:
#         image_rocket = 'астеройд2.png'
#     if random == 3:
#         image_rocket = 'пришельцы.png'
#     meteor = Enemy_up(image_rocket, randint(1, 3), randint(0, 620),-50, 40, 40)
#     meteor.add(meteors_up)

# for i in range(4):
#     random = randint(1,3)
#     image_rocket = 0
#     if random == 1:
#         image_rocket = 'астеройд.png'
#     if random == 2:
#         image_rocket = 'астеройд2.png'
#     if random == 3:
#         image_rocket = 'пришельцы.png'
#     meteor = Enemy_left(image_rocket, randint(1, 3), -50, randint(0, 420), 40, 40)
#     meteor.add(meteors_left)

# for i in range(4):
#     random = randint(1,3)
#     image_rocket = 0
#     if random == 1:
#         image_rocket = 'астеройд.png'
#     if random == 2:
#         image_rocket = 'астеройд2.png'
#     if random == 3:
#         image_rocket = 'пришельцы.png'
#     meteor = Enemy_right(image_rocket, randint(1, 3), 750, randint(0, 420), 40, 40)
#     meteor.add(meteors_right)


# for i in range(4):
#     random = randint(1,3)
#     image_rocket = 0
#     if random == 1:
#         image_rocket = 'астеройд.png'
#     if random == 2:
#         image_rocket = 'астеройд2.png'
#     if random == 3:
#         image_rocket = 'пришельцы.png'
#     meteor = Enemy_down(image_rocket, randint(1, 3), randint(0, 620),550, 40, 40)
#     meteor.add(meteors_down)



# game = True
# gameplay = True
# question_game = True
# hp = main_win.right
# clock = time.Clock()

# lose = Text('Вы проиграли', 250, 200, 115, 132, 148)
# win = Text('Вы победили', 250, 200, 115, 132, 148)
# restart = Text('Играть заново', 250, 300, 166, 225, 223)
# hp_text = Text(str(hp), 10, 10, 255, 0, 0)

# question_text = Text('Название спутника Юпитера', 250, 150, 115, 132, 220)
# answer1 = Text('Европа', 250, 200, 115, 132, 148)
# answer2 = Text('Европа', 250, 250, 115, 132, 148)
# answer3 = Text('Европа', 250, 300, 115, 132, 148)
# answer4 = Text('Европа', 250, 350, 115, 132, 148)

# question1_ = 0
# question2_ = 0
# question3_ = 0
# question4_ = 0

# while game:

#     for i in event.get():
#             if i.type == QUIT:
#                 game = False
#                 pause = False

#     if question_game:
#         if gameplay:
#             bg_y +=1
#             if bg_y == 500:
#                 bg_y = 0

#             if sprite.spritecollide(player, meteors_up, True):
#                 hp -= 1
#                 random = randint(1,3)
#                 image_rocket = 0
#                 if random == 1:
#                     image_rocket = 'астеройд.png'
#                 if random == 2:
#                     image_rocket = 'астеройд2.png'
#                 if random == 3:
#                     image_rocket = 'пришельцы.png'
#                 meteor = Enemy_up(image_rocket, randint(1, 3), randint(0, 620),-50, 40, 40)
#                 meteor.add(meteors_up)       
#             if sprite.spritecollide(player, meteors_left, True):
#                 hp -= 1
#                 random = randint(1,3)
#                 image_rocket = 0
#                 if random == 1:
#                     image_rocket = 'астеройд.png'
#                 if random == 2:
#                     image_rocket = 'астеройд2.png'
#                 if random == 3:
#                     image_rocket = 'пришельцы.png'
#                 meteor = Enemy_left(image_rocket, randint(1, 3), -50, randint(0, 420), 40, 40)
#                 meteor.add(meteors_left)
#             if sprite.spritecollide(player, meteors_right, True):
#                 hp -= 1
#                 random = randint(1,3)
#                 image_rocket = 0
#                 if random == 1:
#                     image_rocket = 'астеройд.png'
#                 if random == 2:
#                     image_rocket = 'астеройд2.png'
#                 if random == 3:
#                     image_rocket = 'пришельцы.png'
#                 meteor = Enemy_right(image_rocket, randint(1, 3), 750, randint(0, 420), 40, 40)
#                 meteor.add(meteors_right)
#             if sprite.spritecollide(player, meteors_down, True):
#                 hp -= 1
#                 random = randint(1,3)
#                 image_rocket = 0
#                 if random == 1:
#                     image_rocket = 'астеройд.png'
#                 if random == 2:
#                     image_rocket = 'астеройд2.png'
#                 if random == 3:
#                     image_rocket = 'пришельцы.png'
#                 meteor = Enemy_down(image_rocket, randint(1, 3), randint(0, 620),550, 40, 40)
#                 meteor.add(meteors_down)

            
            
#             if hp == 0:
#                 gameplay = False
            
                    
#             window.blit(background,(0,bg_y))
#             window.blit(background,(0,bg_y - 500))
#             player.update()
#             meteors_up.update()
#             meteors_left.update()
#             meteors_right.update()
#             meteors_down.update()
#             player.reset()
#             meteors_up.draw(window)
#             meteors_left.draw(window)
#             meteors_right.draw(window)
#             meteors_down.draw(window)
#             hp_text.label = hp_text.font_.render('hp:' + str(hp), True, (hp_text.colour1,hp_text.colour2,hp_text.colour3))
#             hp_text.reset()

#         else:
#             window.fill((87, 88, 89))
#             lose.reset()
#             restart.reset()
            
#             mouse_ = mouse.get_pos()
#             if restart.rect.collidepoint(mouse_) and mouse.get_pressed()[0]:
#                 gameplay = True
#                 hp = 2
#     else:
#         window.fill((0, 0, 0))


            



        

#     clock.tick(60)
#     display.update()