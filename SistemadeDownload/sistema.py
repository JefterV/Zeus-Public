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
                

    def downloadYT(url, pasta, opcao):
        Sistema.remove_dir('./SistemadeDownload/downloadcache')  
        from pytube import YouTube
        while True:
            try:
                link = url
                if link == 'n':
                    break
                
            except:
                print("O link que você digitou é invalido, tente novamente!")
                
            else:
                try:
                    yt = YouTube(link)
                except:
                    print("Não foi possivel acessar as informações do link")
                    
                else:
                    print(yt.title)
                    

                    local = './SistemadeDownload/downloadcache'
                   
                    name = str(len(os.listdir()))
                    
                    
                    if opcao == '1':
                        o = yt.streams.all()
                    
                        b = o[0].download(local)
                        
                        name2 = os.listdir('./SistemadeDownload/downloadcache')
                        name3 = name2[0].replace('.mp4', '')
                        
                        try:
                            conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 = pasta+'/'+name3)
                        except:
                            os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                        else:
                            os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                        
                        

                    elif opcao == '2':
                        o = yt.streams.all()              
                        b = o[0].download(pasta)
                        
                        

                    elif opcao == '3':
                        o = yt.streams.all()
                    
                        b = o[0].download(local)
                        
                        name2 = os.listdir('./SistemadeDownload/downloadcache')
                        name3 = name2[0].replace('.mp4', '')
                        
                        
                        conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 = pasta+'/'+name3)
                        os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                        o[0].download(pasta)
                        
                        
                    
            
            Sistema.remove_dir('./SistemadeDownload/downloadcache')      
            break     
    
    def DownloadPlaylist(url, pasta, opcao):
        Sistema.remove_dir('./SistemadeDownload/downloadcache')  
        while True:
            
            try:
                link = url
                
            except:
                print("O link que você digitou é invalido, tente novamente!")
                
            else:

                try:
                    from  pytube  import  Playlist                
                    pl  =  Playlist(link)
                    
                except:
                    print('erro')
                else:
                    local = './SistemadeDownload/downloadcache'


                   
                    
                    
                    if opcao == '1':
                        for video in pl.videos:
                            video.streams.first().download(local)
                        
                            name2 = os.listdir('./SistemadeDownload/downloadcache')
                            name3 = name2[0].replace('.mp4', '')
                            
                            try:
                                conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 = pasta+'/'+name3)
                            except:
                                os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                            else:
                                os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                            
                       

                    elif opcao == '2':
                        for video in pl.videos:
                            video.streams.first().download(pasta)
                        
                       

                    elif opcao == '3':
                        for video in pl.videos:
                            video.streams.first().download(local)
                        
                            name2 = os.listdir('./SistemadeDownload/downloadcache')
                            name3 = name2[0].replace('.mp4', '')
                            
                            
                            conversao(mp4 = './SistemadeDownload/downloadcache/'+name2[0], mp3 =  pasta+'/'+name3)
                            os.remove('./SistemadeDownload/downloadcache/'+name2[0])
                            video.streams.first().download(pasta)
                            
                        
            break       

    def titulo(link):
        
        yt = YouTube(link)
        titulo = yt.title()
        return titulo