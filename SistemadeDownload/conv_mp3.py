#UTF-8
from moviepy.editor import *

def conversao(mp4 = '', mp3 = '' ):
    '''
    Está função converte arquivos de .mp4 para .mp3
    mp4_file: arquivo que será convertido, caso não esteja na mesma pasta do conversor é necessario informar o caminho.
    mp3_file: nome do arquivo que gera gerado
    '''
    mp4_file = mp4

    mp3_file = mp3+'.mp3'

    videoClip = VideoFileClip(mp4_file)

    audioclip = videoClip.audio

    audioclip.write_audiofile(mp3_file)

    audioclip.close()

    videoClip.close()
