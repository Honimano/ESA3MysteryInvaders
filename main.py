from game import Game

# Title and

#Musiktitel Copyright: von Funny Puppies - GEMAfreie Musik von https://audiohub.de
#Musiktitel Copyright: Zombie Invasion (2015) - GEMAfreie Musik von https://audiohub.de
#Rough draft - GEMAfreie Musik von https://audiohub.de
#All over now - GEMAfreie Musik von https://audiohub.de
# Grafics -Peggy Kleinert
# tutorial: https://www.youtube.com/watch?v=FfWpgLFMI7w

game = Game()
while game.running:
    game.curr_menu.display_menu()
    game.game_loop()


