from moviepy.editor import *
import os

poss = str(input('digite a musica: '))
position = int(poss)
    
dir_mp4 = os.listdir('./downloads/smp4')
print(dir_mp4)
music = dir_mp4[position]
caminho = './downloads/smp4/'+music

video = VideoFileClip(caminho).rotate(180)
video.ipython_display(width = 280)