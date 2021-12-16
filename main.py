import random
import math
import pygame
from pygame import mixer


# Initialize the pygame

pygame.init()
# create the screen (900 width, 900 height)
screen = pygame.display.set_mode((900, 900))

# background
background = pygame.image.load('images/unterwasser1.png')

# Background Sound

mixer.music.load('sound/background_funny_puppies.wav')
# -1 plays on loop
mixer.music.play(-1)



# Title and

#Musiktitel Copyright: von Funny Puppies - GEMAfreie Musik von https://audiohub.de
#Musiktitel Copyright: Zombie Invasion (2015) - GEMAfreie Musik von https://audiohub.de
#Rough draft - GEMAfreie Musik von https://audiohub.de
#All over now - GEMAfreie Musik von https://audiohub.de
# Grafics -Peggy Kleinert
# tutorial: https://www.youtube.com/watch?v=FfWpgLFMI7w

pygame.display.set_caption("Mystery Invaders")
icon = pygame.image.load('images/ship_32.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('images/krebsmonster_100.png')
playerX = 420
playerY = 780
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/monster_80.png'))
    enemyImg.append(pygame.image.load('images/schaf_80.png'))
    enemyImg.append(pygame.image.load('images/feind_blau_80.png'))
    # randomly appended enemies at random coordinates
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(25, 250))
    enemyX_change.append(1)
    enemyY_change.append(80)

# Ready = you cant see the bullet on the screen
# Fire = bullet is currently moving - so two states motion versus non motion
bulletImg = pygame.image.load('images/wurfdonat_32.png')
bulletX = 0
bulletY = 780
bulletX_change = 4
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
# definition of the font
over_font = pygame.font.Font('freesansbold.ttf', 64)

# function to show the score and draw it on the screen with blit
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
#when game is over there has to show a text
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (250, 450))

# the blit() method is to draw things on the screen, here its definition ->call method in game loop!
#player needs also to be "blitted"
def player(x, y):
    screen.blit(playerImg, (x, y))

# the enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# the bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# for the collision i need a math formula to get the distance between bulltet and enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop - window does not close down, it closes when exit (x) (right top side of the window) has been pressed
running = True
while running:
    # R G B colours, and the window has to update always, so this and the init are always active
    screen.fill((0, 0, 0))
    # background Image has to be drawn
    screen.blit(background, (0, 0))

    # a collection of events when running the loop - what happens when right and left arrow keys will be pressed to move the ship
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if key is pressed, check if right or left
        if event.type == pygame.KEYDOWN:
            # print("A key has been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            #  print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
                # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('images/laser.wav')
                    bullet_Sound.play()
                    # Get the current x coordinate of the ship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Key has been released")
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game over if enemy hits the ship
        if enemyY[i] > 736:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('sound/explosion.wav')
            explosion_Sound.play()
            bulletY = 780
            bullet_state = "ready"
            score_value += 1
            # print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 780
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
