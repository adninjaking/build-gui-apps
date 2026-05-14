import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

font = pygame.font.SysFont('bahnschrift', 60)
white = (255, 255, 255)

# Game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False

# Load images
bg = pygame.image.load('flappy bird/img/bg.png')
ground_img = pygame.image.load('flappy bird/img/ground.png')
button_img = pygame.image.load('flappy bird/img/restartbutton.png')


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_game():
    pipe_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = screen_height // 2
    return 0


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        self.index = 0
        self.counter = 0

        for num in range(1, 4):
            img = pygame.image.load(f"flappy bird/img/flappybird{num}.png")
            self.images.append(img)

        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x, y))
        self.vel = 0
        self.clicked = False

    def update(self):
        global flying, game_over

        if flying:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if not game_over:
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            flap_cooldown = 5
            self.counter += 1

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index = (self.index + 1) % len(self.images)

            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        super().__init__()
        self.image = pygame.image.load("flappy bird/img/pipe.png")
        self.rect = self.image.get_rect()

        if position == 1:  # top pipe
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = (x, y - pipe_gap // 2)
        else:  # bottom pipe
            self.rect.topleft = (x, y + pipe_gap // 2)

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image, self.rect)
        return action


pipe_group = pygame.sprite.Group()
bird_group = pygame.sprite.Group()

flappy = Bird(100, screen_height // 2)
bird_group.add(flappy)

button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)

run = True
while run:

    clock.tick(fps)
    screen.blit(bg, (0, 0))

    pipe_group.draw(screen)
    bird_group.draw(screen)
    bird_group.update()

    screen.blit(ground_img, (ground_scroll, 768))

    # Score
    if len(pipe_group) > 0:
        bird = bird_group.sprites()[0]
        first_pipe = pipe_group.sprites()[0]

        if bird.rect.left > first_pipe.rect.left and bird.rect.right < first_pipe.rect.right and not pass_pipe:
            pass_pipe = True

        if pass_pipe and bird.rect.left > first_pipe.rect.right:
            score += 1
            pass_pipe = False

    draw_text(str(score), font, white, screen_width // 2, 20)

    # Collision
    if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top <= 0:
        game_over = True

    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False

    # New pipes
    if not game_over and flying:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, -1)
            top_pipe = Pipe(screen_width, screen_height // 2 + pipe_height, 1)
            pipe_group.add(bottom_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now

    # Ground scroll
    if not game_over:
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0

    # Restart
    if game_over:
        if button.draw():
            game_over = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not flying and not game_over:
            flying = True







    pygame.display.update()

pygame.quit()

           












    







        










        
    


         


                 

