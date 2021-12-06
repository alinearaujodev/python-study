# COLOQUE UMA MÚSICA PARA TOCAR

from pygame import mixer
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
input('Agora você escuta?')
