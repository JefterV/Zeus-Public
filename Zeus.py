#UTF-8
from SistemadeDownload.sistema import *
from SistemadeReproduzing.arqmp3 import *
import time
while True:
    # CABEÇALHO
    print("="*40)
    print("")
    print(F"{'BEM-VINDO, EU SOU O ZEUS!':^40}")
    print(f"{'© Jefter Viana':^60}")
    print("")
    print("="*40)

    print("\nCarregando Menu...")
    time.sleep(3)
    
    while True:
        var_controle = ''
        # MENU
        print("""[ 1 ] - Converter MP3 ---> MP4
[ 2 ] - YouTube 
[ 3 ] - Escutar musica
[ 4 ] - Encerrar""") 
        var_controle = str(input('Sua opção: '))

        # ESTRUTURA DE OPÇÕES 2
        if var_controle == '1' or var_controle == '2' or var_controle == '3':
            
            if var_controle == '1': #converter
                print('desenvolvendo')

            elif var_controle == '2': #download
                        print('[ 1 ] - Download de arquivos MP3 e MP4\n[ 2 ] - Download de PlayList')
                        opcao_cont = str(input('Sua opção: ')).strip() 
                        if opcao_cont == '1' or opcao_cont == '2':
                            if opcao_cont == '1':
                                Sistema.downloadYT()
                            else:
                                Sistema.DownloadPlaylist()
                        else:
                            print('Sua opção não é valida!\nRetornando para o menu principal...')
                            time.sleep(2)
                            continue

            elif var_controle == "3": #escutar
                play.music()

        elif var_controle == '4': #encerrar
            print('encerrando...')
            time.sleep(3)
            break

        else: #opção invalida
            print('ESSA OPÇÃO NÃO É VALIDA! DESEJA TENTAR NOVAMENTE?')
            var_controle = str(input('[s/n]: '))
            if var_controle == 'n':
                print('encerrando...')
                time.sleep(2)
                break
            else:
                continue 
    break