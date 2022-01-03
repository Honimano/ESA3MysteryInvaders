from menu import *


class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        # define keys to move through the menu, keep track of players actions
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 900, 900
        # the text and icon for the game window
        pygame.display.set_caption("Mystery Invaders")
        icon = pygame.image.load('images/game_icon/ship_32.png')
        pygame.display.set_icon(icon)
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name1 = 'fonts/8-BIT WONDER.TTF'
        self.font_name2 = 'fonts/FreeSansBold.ttf'
        self.BACKGROUND = (125, 150, 50)
        self.background_img = pygame.image.load('images/heroes/krebsmonster_200.png')
        self.TEXT_COLOR = (250, 250, 250)
        self.text_color_main_line = (150, 50, 200)
        # til here game object
        # game passes itself as a parameter into the MainMenu class
        self.main_menu = MainMenu(self)
        self.current_level = None
        self.level2 = MainMenu(self)
        self.level3 = MainMenu(self)
        self.curr_menu = self.main_menu

# game loop level1
    def game_loop(self):
        self.current_level.load()
        self.current_level.game_loop(self.window)

# game events - player actions, pressed Keys

    def check_events(self):
        for event in pygame.event.get():
            # if player wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # if something on the keyboard is pressed
            if event.type == pygame.KEYDOWN:
                # enter key press
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    # after the frame or game loop keys need to be set back to false
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text_menu(self, text, size, x, y):
        font_menu = pygame.font.Font(self.font_name1, size)
        text_surface = font_menu.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_text_explain(self, text, size, x, y):
        font_text_explain = pygame.font.Font(self.font_name2, size)
        text_surface = font_text_explain.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def draw_text_main_line(self, text, size, x, y):
        font_text_main_line = pygame.font.Font(self.font_name1, size)
        text_surface = font_text_main_line.render(text, True, self.text_color_main_line)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)





