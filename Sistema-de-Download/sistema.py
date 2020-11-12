# UTF-8
from pytube import YouTube
from conv_mp3 import conversao
import os

while True:
    try:
        link = str(input("Digite o link: ")).strip()
    except:
        print("O link que você digitou é invalido, tente novamente!")
        continue
    else:
        try:
            yt = YouTube(link)
        except:
            print("Não foi possivel acessar as informações do link")
            var_controle = str(input("Deseja tentar novamente:[s/n] ")).lower().strip()
            if var_controle[0] == 'n':
                break
            else:
                continue
        else:
            print(yt.title)
            
            o = str(input("Este é o titulo video, correto?[s/n] ")).lower().strip().split()
            if o[0] == 'n':
                continue

            local = './Sistema-de-Download/downloadcache'
            ###
            print("ESCOLHA UMA DAS OPÇÕES\n [ 1 ] - ARQUIVO .MP3\n [ 2 ] - ARQUIVO .MP4\n [ 3 ] ARQUIVO .MP3 E .MP4")
            ###
            
            name = str(len(os.listdir()))
            
            opcao = str(input(": ")).strip()
            if opcao == '1':
                o = yt.streams.all()
               
                b = o[0].download(local)
                
                name2 = os.listdir('./Sistema-de-Download/downloadcache')
                name3 = name2[0].replace('.mp4', '')
                
                try:
                   conversao(mp4 = './Sistema-de-Download/downloadcache/'+name2[0], mp3 = '/downloads/smp3/'+name3)
                except:
                    os.remove('./Sistema-de-Download/downloadcache/'+name2[0])
                else:
                    os.remove('./Sistema-de-Download/downloadcache/'+name2[0])

            elif opcao == '2':
                o = yt.streams.all()              
                b = o[0].download('./downloads/smp4')

            elif opcao == '3':
                o = yt.streams.all()
               
                b = o[0].download(local)
                
                name2 = os.listdir('./Sistema-de-Download/downloadcache')
                name3 = name2[0].replace('.mp4', '')
                
                
                conversao(mp4 = './Sistema-de-Download/downloadcache/'+name2[0], mp3 = './downloads/smp3/'+name3)
                os.remove('./Sistema-de-Download/downloadcache/'+name2[0])
                o[0].download('./downloads/smp4')

            else:
                continue
               

          
# C:\Users\Jefinho\Desktop\BotYT
# https://www.youtube.com/watch?v=mxFstYSbBmc
# C:/Users/Jefinho/Desktop/BotYT/Sistema-de-Download/downloadcache
# https://youtu.be/kOtzu4Koap0 
# https://youtu.be/0mMu1D6VEAQ
# https://youtu.be/xmxUCIcO9No