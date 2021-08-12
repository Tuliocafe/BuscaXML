from manipulacao import *
import os

listanfce = []
listanfcetemp = []
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

print(f'local do arquivo é:   {caminho_busca}')


if os.path.exists(caminho_busca) == True:
    while True:
        teste_vazio = detectar_arquivo(caminho_copia)
        menuprincipal()
        try:
            menu = int(input('Digite a Opção desejada: '))
            if menu == 1:
                localizarxml(caminho_busca, caminho_copia)
            elif menu == 2:
                sequencia(caminho_busca, caminho_copia)
            elif menu == 3:
                apagar_arquivo(teste_vazio, caminho_copia)
            elif menu == 9:
                break
            else:
                print('')
                print('Digito invalido favor tentar novamente')
                print('')
        except ValueError:
            print('')
            print('Digito invalido! Favor tentar novamente')
            print('')
            pass

else:
    print(f'{caminho_busca} nao encontada')
    exit = input('Pressione ENTER para fechar')
