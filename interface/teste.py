from zeus import *
from SistemaZEUS.sistema import Sistema
from SistemaZEUS.image_mnp import edit_image
#from SistemadeReproduzing import arqmp3
import os

################ REPRODUÇÃO ################
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog, QMainWindow
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
############################################

controleTIPODODOWNLOAD = ''
class Janela1(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)
        self.system()
        self.show()

    def system(self):

        ######### ESCONDENDO Widgets...
        self.ui.l_titulo.hide()
        self.ui.barradeprogresso.hide()
        self.ui.pushButton.hide()

        #########


    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #    
        
    ########################### TERCEIRO BLOCO - PREPARANDO SISTEMA PARA UM NOVO DOWNLOAD ############################## 
    #  
    #  1 - Ocultando bloco 2, exibindo bloco 1
    #  +++
    #  2 - Verificando o tipo do arqself.uivo
    #  +++
    #  3 - Verificando o tipo do downaload
    #  +++
    #  4 - Realizando o download
    #  -------------------------------------------------------------------------------  
        
        def Download_arq(tipos):
            # Ocultando bloco 2
            
            self.ui.pb_download.disconnect()
            self.ui.rb_mp4.hide()
            self.ui.rb_mp3.hide()
            self.ui.rb_mp3_mp4.hide()
            self.ui.pushButton.close()
            ####

            # Exibindo bloco 1

            self.ui.rb_playlist.show()
            self.ui.rb_umarq.show()
            self.ui.pb_download.setText("Proximo")
            self.ui.l_titulo.show()
            ####

            def veryCheckBox3():
                """
                ESSA FUNÇÃO VERIFICA SE O BOTÃO DE CHECAGEM "UM ARQself.uiVO" OU "PLAYLIST" FOI PRESSIONADO.
                SE SIM, O PROGRAMA EXECUTA O SEGUNDO BLOCO DE COMANDO. 
                SE NÃO, O PROGRAMA NÃO REALIZA NENHUMA AÇÃO.
                """
                cont_play = self.ui.rb_playlist.isChecked()
                cont_arq  = self.ui.rb_umarq.isChecked()
                
                if cont_arq or cont_play:
                    if cont_arq:
                        
                        global controleTIPODODOWNLOAD 
                        controleTIPODODOWNLOAD = 'Um arq'
                        actionPLAY()
                        Bloco_2('Um Arqself.uivo')
                    else:
                        
                        controleTIPODODOWNLOAD = 'Playlist'
                        actionPLAY()
                        Bloco_2('Playlist')
                    
            
            
            def tipo(opcao_cont):
                """
                Essa função reliza o download do Arqself.uivo ou Playlist
                """

                link = self.ui.line_link.text()
                
                tipoarq = '0'

                # Verificando o tipo do arqself.uivo

                caminho  = ''
                if opcao_cont['1'] == 'mp3' or opcao_cont['1'] == 'mp4' or opcao_cont['1'] == 'mp3_mp4':
                    if opcao_cont['1'] == 'mp3':
                        tipoarq = '1'
                        caminho = os.path.abspath("./downloads/smp3")
                    elif opcao_cont['1'] == 'mp4':
                        tipoarq = '2'
                        caminho = os.path.abspath("./downloads/smp4")
                    else:
                        tipoarq = '3'
                        caminho = (os.path.abspath("./downloads/smp3"), os.path.abspath("./downloads/smp4"))
                
                
                # Verificando o tipo do download
                if opcao_cont['0'] == 'Playlist' or opcao_cont['0'] == 'Um Arquivo':
                    if opcao_cont['0'] == 'Um Arquivo':
                        Sistema.downloadYT(link, caminho,tipoarq)
                    else:
                        Sistema.DownloadPlaylist(link, caminho,tipoarq)
                else:
                    return False
            #tipo(tipos)
            self.ui.pb_download.clicked.connect(veryCheckBox3)


        
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        
        ##################### SEGUNDO BLOCO - DOWNLOAD #########################

        # 0 - Exibindo segundo bloco para o usuario 
        # +++
        # 1 - Atribself.uindo novas funções
        # +++
        # 2 - Atribself.uição de Texto
        # +++
        # 3 - Verifica se as caixas de verificação, estão checadas 
        # -------------------------------------------------------------------------------


        def Bloco_2(tipo):
            """
            Essa função está encarregada de 
            - Realizar o download
            - Verificar se os parametros exigidos estão devidamente preenchidos
            """
            
            self.ui.pushButton.disconnect()
            self.ui.pb_download.disconnect()
            

            
            def prox():
                """
                Essa função faz
                - Exibe o segundo bloco para o usuario
                - Exclself.ui o primeiro bloco da interface 
                """
                self.ui.rb_playlist.hide()
                self.ui.rb_umarq.hide()

                self.ui.rb_mp3 = QtWidgets.QRadioButton(self.ui.frame)
                self.ui.rb_mp3.setMinimumSize(QtCore.QSize(168, 17))
                self.ui.rb_mp3.setObjectName("rb_mp3")
                self.ui.gridLayout_12.addWidget(self.ui.rb_mp3, 0, 0, 1, 1)
                self.ui.rb_mp3_mp4 = QtWidgets.QRadioButton(self.ui.frame)
                self.ui.rb_mp3_mp4.setMinimumSize(QtCore.QSize(168, 17))
                self.ui.rb_mp3_mp4.setObjectName("rb_mp3_mp4")
                self.ui.gridLayout_12.addWidget(self.ui.rb_mp3_mp4, 0, 1, 1, 1)
                self.ui.rb_mp4 = QtWidgets.QRadioButton(self.ui.frame)
                self.ui.rb_mp4.setMinimumSize(QtCore.QSize(168, 17))
                self.ui.rb_mp4.setObjectName("rb_mp4")
                self.ui.gridLayout_12.addWidget(self.ui.rb_mp4, 1, 0, 1, 1)

                self.ui.rb_mp4.show()
                self.ui.rb_mp4.show()
                self.ui.rb_mp4.show()
                self.ui.pushButton.show()


            

            
            def voltar():
                """
                Se o usuario clicar no botão voltar, o sistema irá voltar desdo Primeiro bloco
                """
                Download_arq('nada')

            
            
            def texto():
                '''
                Essa função altera / impõe o texto nos botões
                '''

                self.ui.rb_mp3.setText(".MP3")
                self.ui.rb_mp3_mp4.setText(".MP3 e .MP4")
                self.ui.rb_mp4.setText(".MP4")
                self.ui.pb_download.setText("Download")
                
            
            prox()
            texto()

            self.ui.pushButton.clicked.connect(voltar)

            saida = {'0':tipo} # Essa variavel armazena o tipo do link - UM ARQself.uiVO OU PLAYLIST, EM SEGself.uiDA SERÃO ATRIBself.uiDOS NOVOS VALORES 


            
            def veryCheckBox2():
                
                cont_mp3 = self.ui.rb_mp3.isChecked()
                cont_mp4  = self.ui.rb_mp4.isChecked()
                cont_mp3_mp4 = self.ui.rb_mp3_mp4.isChecked()

                if cont_mp3 or cont_mp3_mp4 or cont_mp4:
                    if cont_mp3:
                        saida['1'] = 'mp3'
                        Download_arq(saida)
                    elif cont_mp4:
                        saida['1'] = 'mp4'
                        Download_arq(saida)
                    else:
                        saida['1'] = 'mp3_mp4'
                        Download_arq(saida)
                    
                    
            self.ui.pb_download.clicked.connect(veryCheckBox2)




    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    ######################### PRIMEIRO BLOCO - VERICAÇÃO ############################ 



        # 6 - Passando para o proximo bloco
        # 5 - Verificando os botões
        # +++
        # 4 - Redução de imagem
        # +++
        # 3 - Chamando a Segunda etapa de verificação
        # 2 - Download da thumbneil 
        # 1 - Verificando link
        # 0 - Verificando botões
        # -------------------------------------------------------------------------------


        def veryCheckBox():
            """
            ESSA FUNÇÃO VERIFICA SE O BOTÃO DE CHECAGEM "UM ARQself.uiVO" OU "PLAYLIST" FOI PRESSIONADO.
            SE SIM, O PROGRAMA EXECUTA O SEGUNDO BLOCO DE COMANDO. 
            SE NÃO, O PROGRAMA NÃO REALIZA NENHUMA AÇÃO.
            """

            def Verificacao():
                """
                VERIFICANDO...
                """
                cont_play = self.ui.rb_playlist.isChecked()
                cont_arq  = self.ui.rb_umarq.isChecked()

                if cont_arq or cont_play:
                    if cont_arq:
                        Bloco_2('Um Arquivo')
                    else:
                        Bloco_2('Playlist')

            self.ui.pb_download.clicked.connect(Verificacao)



    ##########################################



        
        def up_thumbneil(dir):
            """- Essa função realiza a redução da imagem.
            - Antes de reduzir a imagem é verificado se o downaload da imagem foi realizado.
            A imagem é armazenada em uma pasta de cache, após ser conclself.uido o download a imagem é deletada pelo sistema do Zeus.
            """

            imagem = edit_image.reduzir_tamanho(os.path.abspath('./SistemadeDownload/downloadimage'),os.path.abspath('./SistemadeDownload/downloadimagecache'))
            
            if imagem:
                self.ui.gpv_background.setStyleSheet("background-image: url(./SistemadeDownload/downloadimagecache/atual.png);\n"
        "background-repeat: no")
                return True
            else:
                return False




    ########################################



        def Primeira_etapa():
            """
            Essa função reliza
            - verificação do link
            - Download da Thumbneil
            - Captura do Titulo
            """
            
            link = self.ui.line_link.text() # Link inserido
            
            # Verificando os botões
            cont_play = self.ui.rb_playlist.isChecked()
            cont_arq  = self.ui.rb_umarq.isChecked()
            controle_midia = ''

            if cont_play or cont_arq:
                if cont_arq:
                    controle_midia = "Um arq"
                elif cont_play:
                    controle_midia = "Playlist"

                print(controle_midia)    
                # Verificando link 
                global controleTIPODODOWNLOAD 
                controleTIPODODOWNLOAD = controle_midia
                tit = Sistema.titulo(link, controle_midia)           
                if tit != False:
                    self.ui.l_titulo.setText(tit)
                    self.ui.l_titulo.show()
                    veryCheckBox()
                    actionPLAY() # 
                    up_thumbneil(os.path.abspath('./Zeus/SistemadeDownload/downloadimagecache/atual.png'))
                    
                    return True
                else:
                    return False
            else:
                return None
        self.ui.pb_verificar.clicked.connect(Primeira_etapa)
            
            
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

######################### BLOCO INDEPENDENTE- REPRODUÇÃO DE VIDEO ############################ 


        
        def previwACTVATE():
            link = self.ui.line_link.text()

            global controleTIPODODOWNLOAD 
            tipo = controleTIPODODOWNLOAD
            Sistema.up_previw(link, tipo)
            
            self.mediaPlayer.setMedia(QMediaContent())
            
            abrirVideo()
        

        def abrirVideo():     
            open_file()
            



        def init_ui():         
            self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)   
            videowidget = QVideoWidget(self)            
            videowidget.show()
              
            
            self.ui.hslider_music.sliderMoved.connect(set_position)
       
           
            vboxLayout = QVBoxLayout()
            vboxLayout.addWidget(videowidget)

            self.setLayout(vboxLayout)
            self.ui.videoSAIDA.setLayout(vboxLayout)
            
    
            self.mediaPlayer.setVideoOutput(videowidget)       
    
            self.mediaPlayer.stateChanged.connect(mediastate_changed)
            self.mediaPlayer.positionChanged.connect(position_changed)
            self.mediaPlayer.durationChanged.connect(duration_changed)
    


        def open_file():
            self.ui.pb_stop.disconnect()
            self.ui.pb_play.disconnect()
            self.ui.pb_play.clicked.connect(play_video)
            filename = os.path.abspath('./SistemadeDownload/previsu/vid.mp4')
    
            if filename != '':
                self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
                self.ui.pb_play.setEnabled(True)
            
    
        def play_video():
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer.pause()
    
            else:
                self.mediaPlayer.play()
    
    
        def mediastate_changed(state):
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                self.ui.pb_play.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause)
    
                )
    
            else:
                self.ui.pb_play.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay)
    
                )
    
        def position_changed(position):
            self.ui.hslider_music.setValue(position)
    
    
        def duration_changed(duration):
            self.ui.hslider_music.setRange(0, duration)
    
    
        def set_position(position):
            self.mediaPlayer.setPosition(position)
    
    
        def handle_errors():
            self.ui.pb_play.setEnabled(False)

        

        def actionPLAY():
            
            self.ui.pb_stop.setText('PREVIEW')
            self.ui.pb_stop.clicked.connect(previwACTVATE)

        
        init_ui()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Janela1()
    sys.exit(app.exec_())

