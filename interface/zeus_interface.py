from zeus import *
from SistemaZEUS.sistema import Sistema
from SistemaZEUS.image_mnp import edit_image
#from SistemadeReproduzing import arqmp3
import os

def system(ui):

    ######### ESCONDENDO Widgets...
    ui.l_titulo.hide()
    ui.barradeprogresso.hide()
    ui.pushButton.hide()

    #########


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #    
     
   ########################### TERCEIRO BLOCO - PREPARANDO SISTEMA PARA UM NOVO DOWNLOAD ############################## 
   #  
   #  1 - Ocultando bloco 2, exibindo bloco 1
   #  +++
   #  2 - Verificando o tipo do arquivo
   #  +++
   #  3 - Verificando o tipo do downaload
   #  +++
   #  4 - Realizando o download
   #  -------------------------------------------------------------------------------  
     
    def Download_arq(tipos):
        # Ocultando bloco 2
        
        ui.pb_download.disconnect()
        ui.rb_mp4.hide()
        ui.rb_mp3.hide()
        ui.rb_mp3_mp4.hide()
        ui.pushButton.close()
        ####

        # Exibindo bloco 1

        ui.rb_playlist.show()
        ui.rb_umarq.show()
        ui.pb_download.setText("Proximo")
        ui.l_titulo.show()
        ####

        def veryCheckBox3():
            """
            ESSA FUNÇÃO VERIFICA SE O BOTÃO DE CHECAGEM "UM ARQUIVO" OU "PLAYLIST" FOI PRESSIONADO.
            SE SIM, O PROGRAMA EXECUTA O SEGUNDO BLOCO DE COMANDO. 
            SE NÃO, O PROGRAMA NÃO REALIZA NENHUMA AÇÃO.
            """
            cont_play = ui.rb_playlist.isChecked()
            cont_arq  = ui.rb_umarq.isChecked()
            if cont_arq or cont_play:
                if cont_arq:
                    Bloco_2('Um Arquivo')
                else:
                    Bloco_2('Playlist')
        
        
        def tipo(opcao_cont):
            """
            Essa função reliza o download do Arquivo ou Playlist
            """

            link = ui.line_link.text()
            
            tipoarq = '0'

            # Verificando o tipo do arquivo

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
        tipo(tipos)
        ui.pb_download.clicked.connect(veryCheckBox3)


    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    
    ##################### SEGUNDO BLOCO - DOWNLOAD #########################

    # 0 - Exibindo segundo bloco para o usuario 
    # +++
    # 1 - Atribuindo novas funções
    # +++
    # 2 - Atribuição de Texto
    # +++
    # 3 - Verifica se as caixas de verificação, estão checadas 
    # -------------------------------------------------------------------------------


    def Bloco_2(tipo):
        """
        Essa função está encarregada de 
        - Realizar o download
        - Verificar se os parametros exigidos estão devidamente preenchidos
        """
        
        ui.pushButton.disconnect()
        ui.pb_download.disconnect()
        

        
        def prox():
            """
            Essa função faz
            - Exibe o segundo bloco para o usuario
            - Exclui o primeiro bloco da interface 
            """
            ui.rb_playlist.hide()
            ui.rb_umarq.hide()

            ui.rb_mp3 = QtWidgets.QRadioButton(ui.frame)
            ui.rb_mp3.setMinimumSize(QtCore.QSize(168, 17))
            ui.rb_mp3.setObjectName("rb_mp3")
            ui.gridLayout_12.addWidget(ui.rb_mp3, 0, 0, 1, 1)
            ui.rb_mp3_mp4 = QtWidgets.QRadioButton(ui.frame)
            ui.rb_mp3_mp4.setMinimumSize(QtCore.QSize(168, 17))
            ui.rb_mp3_mp4.setObjectName("rb_mp3_mp4")
            ui.gridLayout_12.addWidget(ui.rb_mp3_mp4, 0, 1, 1, 1)
            ui.rb_mp4 = QtWidgets.QRadioButton(ui.frame)
            ui.rb_mp4.setMinimumSize(QtCore.QSize(168, 17))
            ui.rb_mp4.setObjectName("rb_mp4")
            ui.gridLayout_12.addWidget(ui.rb_mp4, 1, 0, 1, 1)

            ui.rb_mp4.show()
            ui.rb_mp4.show()
            ui.rb_mp4.show()
            ui.pushButton.show()


        

        
        def voltar():
            """
            Se o usuario clicar no botão voltar, o sistema irá voltar desdo Primeiro bloco
            """
            Download_arq('nada')

        
         
        def texto():
            '''
            Essa função altera / impõe o texto nos botões
            '''

            ui.rb_mp3.setText(".MP3")
            ui.rb_mp3_mp4.setText(".MP3 e .MP4")
            ui.rb_mp4.setText(".MP4")
            ui.pb_download.setText("Download")
            
        
        prox()
        texto()

        ui.pushButton.clicked.connect(voltar)

        saida = {'0':tipo} # Essa variavel armazena o tipo do link - UM ARQUIVO OU PLAYLIST, EM SEGUIDA SERÃO ATRIBUIDOS NOVOS VALORES 


        
        def veryCheckBox2():
            
            cont_mp3 = ui.rb_mp3.isChecked()
            cont_mp4  = ui.rb_mp4.isChecked()
            cont_mp3_mp4 = ui.rb_mp3_mp4.isChecked()

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
                
                
        ui.pb_download.clicked.connect(veryCheckBox2)




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
        ESSA FUNÇÃO VERIFICA SE O BOTÃO DE CHECAGEM "UM ARQUIVO" OU "PLAYLIST" FOI PRESSIONADO.
        SE SIM, O PROGRAMA EXECUTA O SEGUNDO BLOCO DE COMANDO. 
        SE NÃO, O PROGRAMA NÃO REALIZA NENHUMA AÇÃO.
        """

        def Verificacao():
            """
            VERIFICANDO...
            """
            cont_play = ui.rb_playlist.isChecked()
            cont_arq  = ui.rb_umarq.isChecked()

            if cont_arq or cont_play:
                if cont_arq:
                    Bloco_2('Um Arquivo')
                else:
                    Bloco_2('Playlist')

        ui.pb_download.clicked.connect(Verificacao)



##########################################



    
    def up_thumbneil(dir):
        """- Essa função realiza a redução da imagem.
        - Antes de reduzir a imagem é verificado se o downaload da imagem foi realizado.
        A imagem é armazenada em uma pasta de cache, após ser concluido o download a imagem é deletada pelo sistema do Zeus.
        """

        imagem = edit_image.reduzir_tamanho(os.path.abspath('./SistemadeDownload/downloadimage'),os.path.abspath('./SistemadeDownload/downloadimagecache'))
        
        if imagem:
            ui.gpv_background.setStyleSheet("background-image: url(./SistemadeDownload/downloadimagecache/atual.png);\n"
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
        
        link = ui.line_link.text() # Link inserido
        
        # Verificando os botões
        cont_play = ui.rb_playlist.isChecked()
        cont_arq  = ui.rb_umarq.isChecked()
        controle_midia = ''

        if cont_play or cont_arq:
            if cont_arq:
                controle_midia = "Um arq"
            elif cont_play:
                controle_midia = "Playlist"

            # Verificando link 
            tit = Sistema.titulo(link, controle_midia)           
            if tit != False:
                ui.l_titulo.setText(tit)
                ui.l_titulo.show()
                veryCheckBox()
                up_thumbneil(os.path.abspath('./Zeus/SistemadeDownload/downloadimagecache/atual.png'))
                return True
            else:
                return False
        else:
            return None
    ui.pb_verificar.clicked.connect(Primeira_etapa)
            
            
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    system(ui)
    MainWindow.show()
    sys.exit(app.exec_())

