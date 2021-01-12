from zeus import *
from SistemaZEUS.sistema import Sistema
from SistemaZEUS.image_mnp import edit_image
#from SistemadeReproduzing import arqmp3
import os

def system(ui):
    ui.l_titulo.hide()
    ui.barradeprogresso.hide()
    ui.pushButton.hide()
    
    
    def vtt(tipos):
        # MENU INICIAL
        
        ui.pb_download.disconnect()
        ui.rb_mp4.hide()
        ui.rb_mp3.hide()
        ui.rb_mp3_mp4.hide()
        ui.pushButton.close()

        ui.rb_playlist.show()
        ui.rb_umarq.show()
        ui.pb_download.setText("Proximo")
        ui.l_titulo.show()

        def veryCheckBox3():
        
            cont_play = ui.rb_playlist.isChecked()
            cont_arq  = ui.rb_umarq.isChecked()
            if cont_arq or cont_play:
                if cont_arq:
                    algoritimo1('Um Arquivo')
                else:
                    algoritimo1('Playlist')
        
        
        def tipo(opcao_cont):
            link = ui.line_link.text()
            
            tipoarq = '0'
            if opcao_cont['1'] == 'mp3' or opcao_cont['1'] == 'mp4' or opcao_cont['1'] == 'mp3_mp4':
                if opcao_cont['1'] == 'mp3':
                    tipoarq = '1'

                elif opcao_cont['1'] == 'mp4':
                    tipoarq = '2'
                else:
                    tipoarq = '3'
            caminho = os.path.abspath("./downloads/smp3")
            if opcao_cont['0'] == 'Playlist' or opcao_cont['0'] == 'Um Arquivo':
                if opcao_cont['0'] == 'Um Arquivo':
                    Sistema.downloadYT(link, caminho,tipoarq)
                else:
                    Sistema.DownloadPlaylist(link, caminho,tipoarq)
            else:
                print('Sua opção não é valida!\nRetornando para o menu principal...')
        tipo(tipos)
        ui.pb_download.clicked.connect(veryCheckBox3)
        

    def algoritimo1(tipo):
        ui.pushButton.disconnect()
        ui.pb_download.disconnect()
        def prox():
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
            vtt('nada')

        def texto():
            ui.rb_mp3.setText(".MP3")
            ui.rb_mp3_mp4.setText(".MP3 e .MP4")
            ui.rb_mp4.setText(".MP4")
            ui.pb_download.setText("Download")
            
        
        prox()
        texto()

        ui.pushButton.clicked.connect(voltar)

        saida = {'0':tipo}
        def veryCheckBox2():
            cont_mp3 = ui.rb_mp3.isChecked()
            cont_mp4  = ui.rb_mp4.isChecked()
            cont_mp3_mp4 = ui.rb_mp3_mp4.isChecked()
            if cont_mp3 or cont_mp3_mp4 or cont_mp4:
                if cont_mp3:
                    saida['1'] = 'mp3'
                    vtt(saida)
                elif cont_mp4:
                    saida['1'] = 'mp4'
                    vtt(saida)
                else:
                    saida['1'] = 'mp3_mp4'
                    vtt(saida)
                
                
        ui.pb_download.clicked.connect(veryCheckBox2)

    
    
    def veryCheckBox():
        def very33():
            cont_play = ui.rb_playlist.isChecked()
            cont_arq  = ui.rb_umarq.isChecked()
            if cont_arq or cont_play:
                if cont_arq:
                    algoritimo1('Um Arquivo')
                else:
                    algoritimo1('Playlist')
    
        ui.pb_download.clicked.connect(very33)

    def up_thumbneil(dir):
        imagem = edit_image.reduzir_tamanho(os.path.abspath('./SistemadeDownload/downloadimage'),os.path.abspath('./SistemadeDownload/downloadimagecache'))
        print(imagem)
        if imagem:
            ui.gpv_background.setStyleSheet("background-image: url(./SistemadeDownload/downloadimagecache/atual.png);\n"
    "background-repeat: no")
            return True
        else:
            return False


    def verificarpb():
         
        
        link = ui.line_link.text()
        
        cont_play = ui.rb_playlist.isChecked()
        cont_arq  = ui.rb_umarq.isChecked()
        controle_midia = ''
        if cont_play or cont_arq:
            if cont_arq:
                controle_midia = "Um arq"
            elif cont_play:
                controle_midia = "Playlist"
            tit = Sistema.titulo(link, controle_midia)
            if tit != False:
                ui.l_titulo.setText(tit)
                ui.l_titulo.show()
                veryCheckBox()
                up_thumbneil(os.path.abspath('./Zeus/SistemadeDownload/downloadimagecache/atual.png'))
            else:
                print('erro')
    ui.pb_verificar.clicked.connect(verificarpb)
            
            





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    system(ui)
    MainWindow.show()
    sys.exit(app.exec_())

