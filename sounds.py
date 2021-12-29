import pygame
from pygame import mixer


# Musik free without Gema taken from see references beneath:

#Musiktitel Copyright: von Funny Puppies - GEMAfreie Musik von https://audiohub.de
#Musiktitel Copyright: Zombie Invasion (2015) - GEMAfreie Musik von https://audiohub.de
#Rough draft - GEMAfreie Musik von https://audiohub.de
#All over now - GEMAfreie Musik von https://audiohub.de

#backgroundsound level 1
backgroundsound_level1 = mixer.music.load('sound/background_funny_puppies.wav')
# -1 plays on loop
mixer.music.play(-1)
#backgroundsound level 2
backgroundsound_level2 = mixer.music.load('sound/background_zombie.wav')
# -1 plays on loop
mixer.music.play(-1)
#backgroundsoud level3
backgroundsound_level3 = mixer.music.load('sound/background_rough.wav')
# -1 plays on loop
mixer.music.play(-1)

bullet_Sound = mixer.Sound('sound/laser.wav')

explosion_Sound = mixer.Sound('sound/explosion.wav')






