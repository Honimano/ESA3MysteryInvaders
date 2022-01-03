import math
from gameobject import *


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


class Level:
    def __init__(self, background_image_name, background_music_name, num_of_enemies, enemy_img_one, enemy_img_two,
                 enemy_img_three, hero, bullet_speed):
        self.background_image_name = background_image_name
        self.background_music_name = background_music_name
        self.num_of_enemies = num_of_enemies
        self.enemy_images = [enemy_img_one, enemy_img_two, enemy_img_three]
        self.player_image = hero
        self.background_img = None
        self.game_over_font = None
        self.enemies = []
        self.running = False
        self.player = Player(bullet_speed)
        self.score = Score()

    def load(self):
        Bullet.load_prototype('images/laser/wurfdonat_32.png')

        # player
        self.player.load(self.player_image)

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
    @staticmethod
    def has_collision_with_bullet(bullet, enemy):
        distance = math.sqrt(
            (math.pow(enemy.x - bullet.x, 2)) + (math.pow(enemy.y - bullet.y, 2)))
        return distance < 27

    # Game Loop - window does not close down, it closes when exit (x) (right top side of the window) has been pressed
    def game_loop(self, screen):
        self.running = True
        while self.running:
            # R G B colours, and the window has to update always, so this and the init are always active
            screen.fill((0, 0, 0))
            # background image has to be drawn
            screen.blit(self.background_img, (0, 0))

            # a collection of events when running the loop -
            # what happens when right and left arrow keys will be pressed to move the ship
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
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
                for bullet in self.player.bullets:
                    if Level.has_collision_with_bullet(bullet, enemy):
                        pygame.mixer.Sound('sound/explosion.wav').play()
                        bullet.reset()
                        enemy.reset()
                        self.score.increase()

            self.player.show(screen)
            for enemy in self.enemies:
                enemy.show(screen)
            self.score.show(screen)

            pygame.display.update()

    def handle_keyboard_movement(self, screen, event):
        if event.type == pygame.QUIT:
            self.running = False
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
                pygame.mixer.Sound('sound/laser.wav').play()
                # Get the current x coordinate of the ship
                self.player.fire_bullet(screen)
            if event.key == pygame.K_ESCAPE:
                self.running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pressed_keys = pygame.key.get_pressed()
                if not (pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_RIGHT]):
                    self.player.x_change = 0
