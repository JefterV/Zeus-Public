# UTF-8
import playsound
import os

#os.path 

class play:
    def music():
        poss = str(input('digite a musica: '))
        position = int(poss)
        from pathlib import Path
        dir_mp3 = os.listdir('./downloads/smp3')
        print(dir_mp3)
        musica = str(dir_mp3[position])
        caminho = './downloads/smp3/'+musica
        
        playsound.playsound(caminho)


    def repro(): #
        import pygame
        pygame.init()
        poss = str(input('digite a musica: '))
        position = int(poss)

        dir_mp3 = os.listdir('./downloads/smp3')
        print(dir_mp3)
        musica = str(dir_mp3[position])
        caminho = './downloads/smp3/'+musica
        print(caminho)
        pygame.mixer.music.load(caminho)
        pygame.mixer.music.play(5)
        #pygame.event.wait()
