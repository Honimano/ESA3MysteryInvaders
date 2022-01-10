import pygame
import random
from enum import Enum

# class GameObject has a Player and an Enemy, and a Bullet, also we need a bullet state - > the bullets actually are donuts...so its more foodwars, then real shooting ;)
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
    img = None

    @staticmethod
    def load_prototype(img_name):
        Bullet.img = pygame.image.load(img_name)

    def __init__(self, bullet_speed):
        super().__init__(0, 780, 0, 0)
        self.state = BulletState.READY
        self.bullet_speed = bullet_speed
        self.img = Bullet.img

    def load(self, img_name):
        return

    def fire(self, screen, start_x, start_y):
        self.state = BulletState.FIRE
        self.x = start_x
        self.y = start_y
        self.y_change = self.bullet_speed
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
    def __init__(self, bullet_speed):
        super().__init__(420, 780, 0, 0)
        self.bullets = []
        self.bullet_speed = bullet_speed

    def fire_bullet(self, screen):
        bullet = Bullet(self.bullet_speed)
        self.bullets.append(bullet)
        bullet.fire(screen, self.x + 16, self.y + 10)

    def move(self):
        super().move()
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736

        for bullet in self.bullets:
            bullet.move()

        # remove used up bullets from list
        self.bullets = list(filter(lambda b: b.state == BulletState.FIRE, self.bullets))

    def show(self, screen):
        super().show(screen)
        for bullet in self.bullets:
            bullet.show(screen)


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
