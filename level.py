import random
import math
import pygame
from enum import Enum


class Score:
    def __init__(self):
        self.value = 0
        self.font = None
        self.text_x = 10
        self.text_y = 10

    def show(self, screen):
        score = self.font.render("Score : " + str(self.value), True, (255, 255, 255))
        screen.blit(score, (self.text_x, self.text_y))

    def increase(self):
        self.value += 1


class GameObject:
    def __init__(self, x, y, x_change, y_change):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.img = None

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

    def load(self, img_name):
        self.img = pygame.image.load(img_name)

    def show(self, screen):
        screen.blit(self.img, (self.x, self.y))


class BulletState(Enum):
    READY = 1
    FIRE = 2


class Bullet(GameObject):
    def __init__(self):
        super().__init__(0, 780, 0, 0)
        self.state = BulletState.READY

    def fire(self, screen, start_x, start_y):
        self.state = BulletState.FIRE
        self.x = start_x
        self.y = start_y
        self.y_change = -10
        self.show(screen)

    def reset(self):
        self.y = 780
        self.y_change = 0
        self.state = BulletState.READY

    def move(self):
        super().move()

        if self.y <= 0:
            self.reset()

    def show(self, screen):
        if self.state == BulletState.FIRE:
            super().show(screen)


class Player(GameObject):
    def __init__(self):
        super().__init__(420, 780, 0, 0)
        self.bullet = Bullet()

    def fire_bullet(self, screen):
        self.bullet.fire(screen, self.x + 16, self.y + 10)

    def move(self):
        super().move()
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

    def show(self, screen):
        super().show(screen)
        self.bullet.show(screen)


class Enemy(GameObject):
    def __init__(self, x, y, x_change, y_change):
        super().__init__(x, y, x_change, y_change)

    def move(self):
        self.x += self.x_change
        if self.x <= 0:
            self.x_change = 1
            self.y += self.y_change
        elif self.x >= 736:
            self.x_change = -1
            self.y += self.y_change

    def reset(self):
        self.x = random.randint(0, 735)
        self.y = random.randint(50, 150)


class Level:
    def __init__(self, background_image_name, background_music_name, num_of_enemies):
        self.background_image_name = background_image_name
        self.background_music_name = background_music_name
        self.num_of_enemies = num_of_enemies
        self.enemy_images = ['images/foes/monster_80.png', 'images/foes/schaf_80.png', 'images/foes/feind_blau_80.png']

        self.background_img = None
        self.game_over_font = None
        self.enemies = []

        self.player = Player()
        self.score = Score()

    def load(self):
        # player
        self.player.load('images/heroes/krebsmonster_100.png')
        self.player.bullet.load('images/laser/wurfdonat_32.png')

        # enemies
        for i in range(self.num_of_enemies):
            enemy = Enemy(random.randint(0, 750), random.randint(25, 250), 1, 80)
            enemy.load(self.enemy_images[i % len(self.enemy_images)])
            self.enemies.append(enemy)

        # fonts
        self.score.font = pygame.font.Font('freesansbold.ttf', 32)
        self.game_over_font = pygame.font.Font('freesansbold.ttf', 64)

        # background image
        self.background_img = pygame.image.load(self.background_image_name)

        # load and start music
        pygame.mixer.music.load(self.background_music_name)
        pygame.mixer.music.play(-1)

    def game_over_text(self, screen):
        over_text = self.game_over_font.render("GAME OVER", True, (255, 255, 255))
        screen.blit(over_text, (250, 450))

    def show_enemies(self, screen):
        for enemy in self.enemies:
            enemy.show(screen)

    # for the collision i need a math formula to get the distance between bullet and enemy
    def has_collision_with_bullet(self, enemy):
        distance = math.sqrt(
            (math.pow(enemy.x - self.player.bullet.x, 2)) + (math.pow(enemy.y - self.player.bullet.y, 2)))
        return distance < 27

    # Game Loop - window does not close down, it closes when exit (x) (right top side of the window) has been pressed
    def game_loop(self, screen):
        running = True
        while running:
            # R G B colours, and the window has to update always, so this and the init are always active
            screen.fill((0, 0, 0))
            # background image has to be drawn
            screen.blit(self.background_img, (0, 0))

            # a collection of events when running the loop -
            # what happens when right and left arrow keys will be pressed to move the ship
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_keyboard_movement(screen, event)

            self.player.move()

            # Enemy Movement
            for enemy in self.enemies:
                # Game over if enemy hits the ship
                if enemy.y > 736:
                    for enemy2 in self.enemies:
                        enemy2.y = 2000
                    self.game_over_text(screen)
                    break

                enemy.move()

                # Collision
                if self.has_collision_with_bullet(enemy):
                    pygame.mixer.Sound('sound/explosion.wav').play()
                    self.player.bullet.reset()
                    enemy.reset()
                    self.score.increase()

            self.player.bullet.move()

            self.player.show(screen)
            for enemy in self.enemies:
                enemy.show(screen)
            self.score.show(screen)

            pygame.display.update()

    def handle_keyboard_movement(self, screen, event):
        # if key is pressed, check if right or left
        if event.type == pygame.KEYDOWN:
            # print("A key has been pressed")
            if event.key == pygame.K_LEFT:
                self.player.x_change = -0.3
            #  print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                self.player.x_change = 0.3
                # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if self.player.bullet.state == BulletState.READY:
                    pygame.mixer.Sound('sound/laser.wav').play()
                    # Get the current x coordinate of the ship
                    self.player.fire_bullet(screen)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                # print("Key has been released")
                self.player.x_change = 0