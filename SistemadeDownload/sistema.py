# UTF-8
from SistemaZEUS.conv_mp3 import conversao
import os

class Sistema:
    def remove_dir(caminho= ''):
        if caminho != '':
            dir = os.listdir(caminho)
           
            for file in dir:
                try:
                    os.remove(caminho+'/'+file)
                except:
                    pass
                

    def downloadYT():
        Sistema.remove_dir('./SistemadeDownload/downloadcache')  
        from pytube import YouTube
        while True:
            try:
                link = str(input("Digite o link ou 'N' para encerrar: ")).strip()
                if link == 'n':
                    break
                
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
                    
                    o = str(input("Este é o titulo do video, correto?[s/n] ")).lower().strip().split()
                    if o[0] == 'n':
                        continue

                    local = './SistemadeDownload/downloadcache'
                    ###
                    print("ESCOLHA UMA DAS OPÇÕES\n [ 1 ] - ARQUIVO .MP3\n [ 2 ] - ARQUIVO .MP4\n [ 3 ] - ARQUIVO .MP3 E .MP4")
                    ###
                    
                    name = str(len(os.listdir()))
                    
                    opcao = str(input("Sua opção: ")).strip()
                    if opcao == '1':
                        o = yt.streams.all()
                    
                        b = o[0].download(local)
                        
                        name2 = os.listdir('./SistemadeDownload/downloadcache')
                        name3 = name2[0].replace('.mp4', '')
                        
                        try:
                            conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 = './downloads/smp3/'+name3)
                        except:
                            os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                        else:
                            os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                        
                        var_controle = str(input('Deseja continuar:[s/n] ')) #DESATIVAR QUANDO IMPLEMENTAR INTERFACE
                        if var_controle == 'n':
                            break
                        else:
                            continue

                    elif opcao == '2':
                        o = yt.streams.all()              
                        b = o[0].download('./downloads/smp4')
                        
                        var_controle = str(input('Deseja continuar:[s/n] ')) #DESATIVAR QUANDO IMPLEMENTAR INTERFACE
                        if var_controle == 'n':
                            break
                        else:
                            continue

                    elif opcao == '3':
                        o = yt.streams.all()
                    
                        b = o[0].download(local)
                        
                        name2 = os.listdir('./SistemadeDownload/downloadcache')
                        name3 = name2[0].replace('.mp4', '')
                        
                        
                        conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 = './downloads/smp3/'+name3)
                        os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                        o[0].download('./downloads/smp4')
                        
                        var_controle = str(input('Deseja continuar:[s/n] ')) #DESATIVAR QUANDO IMPLEMENTAR INTERFACE
                        if var_controle == 'n':
                            break
                        else:
                            continue
                    else:
                        continue
            Sistema.remove_dir('./SistemadeDownload/downloadcache')      
            break     
    
    def DownloadPlaylist():
        Sistema.remove_dir('./SistemadeDownload/downloadcache')  
        while True:
            
            try:
                link = str(input("Digite o link ou 'N' para encerrar: ")).strip()
                if link[0] == 'n':
                    break
                else:
                    pass
            except:
                print("O link que você digitou é invalido, tente novamente!")
                continue
            else:

                try:
                    from  pytube  import  Playlist                
                    pl  =  Playlist(link)
                    print(pl)
                except:
                    print('erro')
                else:
                    local = './SistemadeDownload/downloadcache'


                    ###
                    print("ESCOLHA UMA DAS OPÇÕES\n [ 1 ] - ARQUIVOS .MP3\n [ 2 ] - ARQUIVOS .MP4\n [ 3 ] -  ARQUIVOS .MP3 E .MP4")
                    ### 
                    opcao = str(input("Sua opção: ")).strip()


                    #print(pl)
                    
                    
                    if opcao == '1':
                        for video in pl.videos:
                            video.streams.first().download(local)
                        
                            name2 = os.listdir('./SistemadeDownload/downloadcache')
                            name3 = name2[0].replace('.mp4', '')
                            
                            try:
                                conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 = './downloads/smp3/'+name3)
                            except:
                                os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                            else:
                                os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                            
                       

                    elif opcao == '2':
                        for video in pl.videos:
                            video.streams.first().download('./downloads/smp4')
                        
                        var_controle = str(input('Deseja continuar:[s/n] ')) #DESATIVAR QUANDO IMPLEMENTAR INTERFACE
                        if var_controle == 'n':
                            break
                        else:
                            continue

                    elif opcao == '3':
                        for video in pl.videos:
                            video.streams.first().download(local)
                        
                            name2 = os.listdir('./SistemadeDownload/downloadcache')
                            name3 = name2[0].replace('.mp4', '')
                            
                            
                            conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 = './downloads/smp3/'+name3)
                            os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                            video.streams.first().download('./downloads/smp4')
                            
                        var_controle = str(input('Deseja continuar:[s/n] ')) #DESATIVAR QUANDO IMPLEMENTAR INTERFACE
                        if var_controle == 'n':
                            break
                        else:
                            continue
                    else:
                        continue




# C:\Users\Jefinho\Desktop\BotYT
# https://www.youtube.com/watch?v=mxFstYSbBmc
# C:/Users/Jefinho/Desktop/BotYT/Sistema-de-Download/downloadcache

# https://youtu.be/0mMu1D6VEAQ
# https://youtu.be/xmxUCIcO9No
# https://www.youtube.com/watch?v=w_KZlDsJs94&list=RDw_KZlDsJs94&start_radio=1
# https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU