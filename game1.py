from menu import *


class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        # define keys to move through the menu, keep track of players actions
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 900, 900
        # the text and icon for the game window
        pygame.display.set_caption("Mystery Invaders")
        icon = pygame.image.load('images/game_icon/ship_32.png')
        pygame.display.set_icon(icon)
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = 'fonts/8-BIT WONDER.TTF'
        # getter for default font
        # self.font = pygame.font.get_default_font()
        self.BACKGROUND = (125, 150, 50)
        self.TEXT_COLOR = (250, 250, 250)
        # til here game object
        # game passes itself as a parameter into the MainMenu class
        self.main_menu = MainMenu(self)
        self.level2 = MainMenu(self)
        self.level3 = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    # game loop
    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            # reset canvas in painting it a color
            self.display.fill(self.BACKGROUND)

            # todo game logic
            self.draw_text('Thanks for Playing', 40, self.DISPLAY_W / 2, self.DISPLAY_H / 2)
            self.window.blit(self.display, (0, 0))
            # shows physically the image on the screen
            pygame.display.update()
            self.reset_keys()

    # game events - player actions, pressed Keys
    def check_events(self):
        for event in pygame.event.get():
            # if player wants to quit
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                # current menu
                self.curr_menu.run_display = False
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

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.TEXT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
