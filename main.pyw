from manipulacao import *
import PySimpleGUI as sg

versao = 'Versao do sistema: 2.0.5'

listanfce = []
caminho_busca = r'c:\Mafra\XML'
caminho_copia = r'c:\Mafra\XML_Novo'

try:
    manipulador = open('C:\Program Files (x86)\TronSolution\TSEmissorNFCe.ini', 'r')
    for c in range(0, 8):
        manipulador.readline()
    caminho_busca = manipulador.readline()[8:]
    caminho_busca = repr(caminho_busca.encode('utf-8', 'ignore'))[2:-2]
    manipulador.close()

except FileNotFoundError:
    pass

teste_vazio = detectar_arquivo(caminho_copia)




def sistema():
    menu_def = [['Arquivo', ['faznada', 'faznada2', 'Sair', ]],
                ['Editar', ['nadinha', ['soteste', 'jura', ], 'mada'], ],
                ['Ajuda', 'Sobre']]

    sg.theme('Dark Green 2')
    layout = [
        [sg.Menu(menu_def,)],
        # [sg.Titlebar('BuscaXML', icon=r'c:\mafra\CentralMafra\BuscaXML\xml.png')],
        [sg.Text(' '*65 + f'Local da busca é:  {caminho_busca}')],
        [sg.Text('Serie', size=(7, 0)), sg.Input(size=(3, 0), do_not_clear=False, key='serie')],
        [sg.Radio('Busca por NFC-E', 'tipo_busca', size=(20, 0), default=True, key='tipo_busca1')],
        [sg.Text('NFC-E', size=(7, 5)),
         sg.Multiline(size=(50, 10), do_not_clear=False, enter_submits=True, key='nfce')],
        [sg.Text('')],
        [sg.Radio('Busca por Sequencia NFC-E', 'tipo_busca')],
        [sg.Text('NFC-E de', size=(7, 0)), sg.Input(size=(10, 0), key='seq1'), sg.Text('a'),
         sg.Input(size=(10, 0), key='seq2')],
        [sg.Text('')],
        [sg.Button('Executar', size=(15, 2)),
         sg.Button('Checar Validade', size=(15, 2)),
         sg.Button('Excluir arquivos'),
         sg.Button('Sair', size=(5, 0))],
        [sg.Output(size=(60, 13))],
        [sg.Text('Desenvolvido por: Túlio Café'.rjust(100))]]

    janela = sg.Window("BuscaXML", layout)

    while True:
        event, value = janela.read()

        if event == 'Sair':
            break

        elif event == 'Executar' and value['tipo_busca1'] is True:
            try:
                localizarxml(caminho_busca, caminho_copia, value['serie'], value['nfce'])
            except:
                pass

        elif event == 'Executar' and value['tipo_busca1'] is False:

            sequencia(caminho_busca, caminho_copia, value['serie'], value['seq1'], value['seq2'])

        elif event == 'Checar Validade':
            validar_arquivos(caminho_copia)

        elif event == 'Excluir arquivos':
            popyn = sg.popup_yes_no("Deseja apagar TODOS os ARQUIVOS da pasta XML_novo",
                                    title='Apagar arquivo')
            if popyn == 'Yes':
                print('Funcao Em manutencao')

                # apagar_arquivo(teste_vazio, caminho_copia)
            else:
                pass

        elif event == 'Sobre':
            sg.popup(versao, title='Status', background_color='#458114')

        else:
            break
sistema()

