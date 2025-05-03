import pygame

W = 700
H = 500

window = pygame.display.set_mode((W, H))
pygame.display.set_caption('Камень, ножницы, бумага')
background = (114, 165, 247)
window.fill(background)

clock = pygame.time.Clock()
FPS = 60

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_img), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < H - 100:
            self.rect.y += self.speed
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < H - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            pass

racket1 = Player('racket.png', 10, H // 2, 25, 100, 10)
racket2 = Player('racket.png', W - 35, H // 2, 25, 100, 10)
ball = GameSprite('ball.png', W // 2, H // 2, 50, 50, 0)

pygame.font.init()
font = pygame.font.Font(None, 35)
lose1 = font.render('Игрок 2 выйграл!', True, (180, 0, 0))
lose2 = font.render('Игрок 1 выйграл!', True, (180, 0, 0))
restart_game = font.render('Ражмите кнопку пробел для рестарта', True, (0, 0, 0))

#музыка

pygame.mixer.init()
pygame.mixer.music.load('MUSIC.ogg')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)

speed_x = 5
speed_y = 5

game = True
finish = False
while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    if finish != True:
        window.fill(background)

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()

        #if ball.rect.y > H-50 or ball.rect.y < 0:
            #speed_y *= -1

        #if pygame.sprite.collide_rect(racket1, ball) and speed_x < 0:
         #   speed_x *= -1
          #  speed_y *= -1

        #if pygame.sprite.collide_rect(racket2, ball) and speed_x > 0:
         #   speed_x *= -1
          #  speed_y *= -1

        #if ball.rect.x < 0:
         #   finish = True
          #  window.blit(lose1, (200, 200))

        #if ball.rect.x > W:
         #   finish = True
          #  window.blit(lose2, (200, 200))
    #else:
        window.blit(restart_game, (150, H-40))
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]:
            ball.rect.y = H//2
            ball.rect.x = W//2
            finish = False

    pygame.display.update()
    clock.tick(FPS)