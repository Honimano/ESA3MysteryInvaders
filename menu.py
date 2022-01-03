import pygame

from level import Level


class Menu:
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
        self.game.draw_text_menu('*', 40, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        self.game.window.blit(self.game.background_img, (350, 670))
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
        # self.game_instructions_x, self.game_instructions_y = self.mid_w, self.mid_h + 240
        # self.credit_x, self.credit_y = self.mid_w, self.mid_h + 300
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
            self.game.draw_text_main_line('Welcome to Mysteryinvaders', 32, self.game.DISPLAY_W / 2,
                                          self.game.DISPLAY_H / 2 - 350)
            self.game.draw_text_menu('Game Instructions', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 290)
            self.game.draw_text_explain('The Hero can move left:  push <, left arrow',
                                        15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 240)
            self.game.draw_text_explain('The Hero can move right: push >, right arrow',
                                        15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 210)
            self.game.draw_text_explain('The Hero can shoot a bullet: push space',
                                        15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 180)
            self.game.draw_text_menu('Main Menu', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)
            self.game.draw_text_explain('You can move through the menu with up arrow and down arrow.',
                                        15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 70)
            self.game.draw_text_explain('Push "return" to start gamelevel.',
                                        15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text_explain(
                'Use the cross at the game window to close window and go back to menu when game is over.',
                15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 10)
            self.game.draw_text_menu("Start Game Level 1", 30, self.level1_x, self.level1_y)
            self.game.draw_text_menu("Start Game Level 2", 30, self.level2_x, self.level2_y)
            self.game.draw_text_menu("Start Game Level 3", 30, self.level3_x, self.level3_y)
            # self.game.draw_text("Game Instructions", 30, self.game_instructions_x, self.game_instructions_y)
            # self.game.draw_text("Credits", 30, self.credit_x, self.credit_y)
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
                self.cursor_rect.midtop = (self.level1_x + self.offset, self.level1_y)
                self.state = 'Start Game Level 1'
        if self.game.UP_KEY:
            if self.state == 'Start Game Level 3':
                self.cursor_rect.midtop = (self.level2_x + self.offset, self.level2_y)
                self.state = 'Start Game Level 2'
            elif self.state == 'Start Game Level 2':
                self.cursor_rect.midtop = (self.level1_x + self.offset, self.level1_y)
                self.state = 'Start Game Level 1'
            elif self.state == 'Start Game Level 1':
                self.cursor_rect.midtop = (self.level3_x + self.offset, self.level3_y)
                self.state = 'Start Game Level 3'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start Game Level 1':
                self.game.playing = True
                self.game.current_level = Level(
                    'images/backgrounds/unterwasser1.png',
                    'sound/background_zombie.wav',
                    5, 'images/foes/feind_blau_80.png',
                    'images/foes/feind_blau_80.png',
                    'images/foes/feind_blau_80.png',
                    'images/heroes/krebsmonster_120.png',
                    -3)
            elif self.state == 'Start Game Level 2':
                self.game.playing = True
                self.game.current_level = Level(
                    'images/backgrounds/schafwiese_900.png',
                    'sound/background_funny_puppies.wav',
                    8, 'images/foes/schaf_orange.png',
                    'images/foes/schaf_orange.png',
                    'images/foes/schaf_orange.png',
                    'images/heroes/schaf_ship.png', -2)
            elif self.state == 'Start Game Level 3':
                self.game.playing = True
                self.game.current_level = Level(
                    'images/backgrounds/hoehle_900.png',
                    'sound/background_rough.wav',
                    12, 'images/foes/feind5_80.png',
                    'images/foes/feind5_80.png',
                    'images/foes/feind5_80.png',
                    'images/heroes/monster_grün_pfote_120.png', -1)
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            # tell main menu to stop displaying
            self.run_display = False


