import pygame
# Quellen: https://www.youtube.com/watch?v=bmRFi7-gy5Y
# https://www.youtube.com/watch?v=a5JWrd7Y_14
# https://docs.python.org/3/library/
from level import Level


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        # keeps menu running
        self.run_display = True
        # cursor
        self.cursor_rect = pygame.Rect(0, 0, 60, 60)
        self.offset = -250

    # helper functions
    # draw a cursor
    def draw_cursor(self):
        self.game.draw_text('*', 40, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        # shows physically the image on the screen
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start Game Level 1"
        self.level1_x, self.level1_y = self.mid_w, self.mid_h + 60
        self.level2_x, self.level2_y = self.mid_w, self.mid_h + 120
        self.level3_x, self.level3_y = self.mid_w, self.mid_h + 180
        self.options_x, self.options_y = self.mid_w, self.mid_h + 240
        self.credit_x, self.credit_y = self.mid_w, self.mid_h + 300
        self.cursor_rect.midtop = (self.level1_x + self.offset, self.level1_y)

    # function to display the menu

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            # to move the cursor around check of events is needed - check player input
            self.game.check_events()
            self.check_input()
            # background
            self.game.display.fill(self.game.BACKGROUND)
            # draw texts on screen
            self.game.draw_text('Main Menu', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Start Game Level 1", 30, self.level1_x, self.level1_y)
            self.game.draw_text("Start Game Level 2", 30, self.level2_x, self.level2_y)
            self.game.draw_text("Start Game Level 3", 30, self.level3_x, self.level3_y)
            self.game.draw_text("Options", 30, self.options_x, self.options_y)
            self.game.draw_text("Credits", 30, self.credit_x, self.credit_y)
            # show cursor
            self.draw_cursor()
            # after finishing a loop blit screen again
            self.blit_screen()

    # function to move the cursor up and down the different options
    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start Game Level 1':
                self.cursor_rect.midtop = (self.level2_x + self.offset, self.level2_y)
                self.state = 'Start Game Level 2'
            elif self.state == 'Start Game Level 2':
                self.cursor_rect.midtop = (self.level3_x + self.offset, self.level3_y)
                self.state = 'Start Game Level 3'
            elif self.state == 'Start Game Level 3':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.credit_x + self.offset, self.credit_y)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.level1_x + self.offset, self.level1_y)
                self.state = 'Start Game Level 1'
        if self.game.UP_KEY:
            if self.state == 'Start Game Level 1':
                self.cursor_rect.midtop = (self.credit_x + self.offset, self.credit_y)
                self.state = 'Credits'
            elif self.state == 'Start Game Level 2':
                self.cursor_rect.midtop = (self.level1_x + self.offset, self.level1_y)
                self.state = 'Start Game Level 1'
            elif self.state == 'Start Game Level 3':
                self.cursor_rect.midtop = (self.level2_x + self.offset, self.level2_y)
                self.state = 'Start Game Level 2'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.level3_x + self.offset, self.level3_y)
                self.state = 'Start Game Level 3'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = 'Options'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start Game Level 1':
                self.game.playing = True
                self.game.current_level = Level(
                    'images/backgrounds/unterwasser1.png',
                    'sound/background_funny_puppies.wav',
                    5)
            elif self.state == 'Start Game Level 2':
                self.game.playing = True
                self.game.current_level = Level(
                    'images/backgrounds/schafwiese_900.png',
                    'sound/background_zombie.wav',
                    8)
            elif self.state == 'Start Game Level 3':
                self.game.playing = True
                self.game.current_level = Level(
                    'images/backgrounds/hoehle_900.png',
                    'sound/background_rough.wav',
                    12)
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            # tell main menu to stop displaying
            self.run_display = False

# options menu -> Volume ->Controls
class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.vol_x, self.vol_y = self.mid_w, self.mid_h + 20
        self.controls_x, self.controls_y = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((25, 25, 25))
            self.game.draw_text("Options", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text("Volume", 20, self.vol_x, self.vol_y)
            self.game.draw_text("Controls", 20, self.controls_x, self.controls_y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controls_x + self.offset, self.controls_y)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)
        elif self.game.START_KEY:
            # todo: create a Volume Menu and a Controls Menu
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BACKGROUND)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 50)
            self.game.draw_text('Mysteryinvaders', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.blit_screen()


