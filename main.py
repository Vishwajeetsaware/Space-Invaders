import pygame
import math
import random
from pygame import mixer
# Initialize the pygame
pygame.init()
# create the screen
screen = pygame.display.set_mode((800, 600))
# Background
background = pygame.image.load('galaxy.jpg')
#Background Sound
mixer.music.load("background.wav")
mixer.music.play(5)
# Title and Icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('img.png')
pygame.display.set_icon(icon)
# Player
playerImg = pygame.image.load('arcade-game (2).png')
playerx = 370
playery = 480
playerx_change = 0

# Enemy

EnemyImg = pygame.image.load('alien (1).png')
Enemyx  = random.randint(0, 735)
Enemyy  = random.randint(50, 150)
Enemyx_change = 0.3
Enemyy_change = 0
# bullet
# Ready you can't see the bullet on the screen
bulletImg = pygame.image.load('bullet (3).png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = "ready"
# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf',62)
def show_score(x,y):
    score = font.render("Score :"+ str(score_value ),True, (255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (50,150))
def player(x, y):
    screen.blit(playerImg, (x, y))

def Enemy(x, y):
    screen.blit(EnemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))
def isCollision(EnemyX,Enemyy,bulletx,bullety):
    distance = math.sqrt(math.pow(Enemyx - bulletx, 2))+(math.pow(Enemyy - bullety, 2))
    if distance < 27:
         return True
    else:
        return False

# game loop
running = True
while running:
    # color - Red, yellow and Green
    screen.fill((0, 0, 0))
    #background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Keystroke is preserved check whether it is right or left  if event.type == pygame.KEYDOWN:
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
               playerx_change = -5
            if event.key == pygame.K_RIGHT:
               playerx_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound("laser.wav")
                    bullet_Sound.play()
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerx_change = 0

# 5 = 5= -0.1
    # checking for the boundaries of spaceship so itdoes'nt go out of boundaries
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
        if Enemyy > 200:
            Enemyy = 2000
            game_over-text()
            break

        # Enemy Movement

    Enemyx += Enemyx_change
    if Enemyx <= 0:
        Enemyx_change = 0.3
    elif Enemyx >= 736:
        Enemyx_change = -0.3

    # Bullet movement
    if bullety <=0:
        bullety=480
        bullet_state= "ready"
    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
    collision = isCollision(Enemyx, Enemyy, bulletx, bullety)
    if collision:
        explosion_Sound = mixer.Sound("explosion.wav")
        explosion_Sound.play()

        bullety = 480
        bullet_state = "ready"
        score_value += 1
        Enemyx = random.randint(0, 735)
        Enemyy = random.randint(50, 150)
    Enemy(Enemyx, Enemyy)
    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()
