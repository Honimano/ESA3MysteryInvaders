from game import Game
import pygame

# Title: Projekt ESA3 - Mytseryinvaders
# @author Peggy Kleinert Matrikelnummer: 20202335
# References:
# Musiktitel Copyright: von Funny Puppies - GEMAfreie Musik von https://audiohub.de
# Musiktitel Copyright: Zombie Invasion (2015) - GEMAfreie Musik von https://audiohub.de
# Musiktitel Copyright: Rough draft - GEMAfreie Musik von https://audiohub.de
# Musiktitel Copyright: All over now - GEMAfreie Musik von https://audiohub.de
# Grafics - Peggy Kleinert
# tutorial: https://www.youtube.com/watch?v=FfWpgLFMI7w
# more references: https://www.youtube.com/watch?v=bmRFi7-gy5Y
# https://www.youtube.com/watch?v=a5JWrd7Y_14
# https://docs.python.org/3/library/

game = Game()
while True:
    game.curr_menu.display_menu()
    game.game_loop()
