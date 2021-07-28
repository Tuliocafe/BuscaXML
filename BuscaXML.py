import os
import shutil
import re

rangexml = []
listanfce = []
listanfcetemp = []
caminho_procura = r'c:\Mafra\XML'
caminho_novo = r'c:\Mafra\XML_Novo'


try:
    manipulador = open('C:\Program Files (x86)\TronSolution\TSEmissorNFCe.ini', 'r')
    for c in range(0, 8):
        manipulador.readline()
    caminho_procura = manipulador.readline()[8:]
    caminho_procura = repr(caminho_procura.encode('utf-8', 'ignore'))[2:-2]
    manipulador.close()

except FileNotFoundError:
    pass

print(f'local do arquivo é:   {caminho_procura}')


def sequencia():
    serie = str(input('Digite a SERIE do XML ou pressione ENTER para 002: '))
    if serie == '':
        serie = '002'

    elif serie.isdigit() and len(serie) <= 3:
        serie = '0' * (3 - len(serie)) + serie

    elif len(serie) >= 4:
        print('Digito errado, tente novamente! ')
        sequencia()

    else:
        print('Numero digitado errado')
        sequencia()

    print('')
    print('Deve colocar o NFCE inicial e o final ex: "30 a 40"')
    print('')
    numero = str(input('Qual sequencia (ex: xxx YYY) ? '))
    listanfcetemp = re.sub("[^0-9]", " ", numero).strip().split(' ')


    for n in range(0, len(listanfcetemp)):
        if listanfcetemp[n].isdigit():
            rangexml.append(listanfcetemp[n])
    try:
        for c in range(int(rangexml[0]), int(rangexml[1])):
            listanfce.append(str(serie + '0' * (9 - len(str(c))) + str(c)))
    except IndexError:
        print('**************************')
        print('Digito é invalido!!!')
        print('Favor inserir inicio e o final da serie!!')
        print('')
        sequencia()
    copiararquivos(listanfce)


def localizarxml():
    serie = str(input('Digite a SERIE da NFCE ou pressione ENTER para 002: '))
    if serie == '':
        serie = '002'

    elif serie.isdigit() and len(serie) <= 3:
        serie = '0' * (3 - len(serie)) + serie

    elif len(serie) >= 4:
        print('Digito errado, tente novamente! ')
        localizarxml()

    else:
        print('Numero digitado errado')
        localizarxml()

    listanfce.clear()
    print('')
    print("""Pode colocar varios NFCEs de uma vez.
o sistema vai ignorar letras e buscar todos os numeros que foram inceridos""")
    print('')
    numero = str(input('Quais NFCEs ? '))
    listanfcetemp = re.sub("[^0-9]", " ", numero).strip().split(' ')


    for n in range(0, len(listanfcetemp)):
        if listanfcetemp[n].isdigit():
            listanfce.append(serie + '0' * (9 - len((listanfcetemp[n]))) + listanfcetemp[n])
    copiararquivos(listanfce)


def copiararquivos(nfce):
    for item in nfce:
        print(f'Procurando item {item}')
    print('')
    try:
        os.mkdir(r'C:\Mafra\XML_Novo')
    except FileExistsError:
        pass

    encontrado = 0
    nao_encontrado = 0
    listanecontrado = []
    for x in nfce:
        for raiz, diretorios, arquivos in os.walk(caminho_procura):
            for arquivo in arquivos:
                if x in arquivo and '-nfe' in arquivo or x in arquivo and '-inu' in arquivo and '-ped' not in arquivo:
                    caminho_antigo = os.path.join(raiz, arquivo)
                    print(f' {encontrado +1} XML Encontrados: {caminho_antigo}  ')
                    arquivonovo = os.path.join(caminho_novo, arquivo)
                    shutil.copy(caminho_antigo, arquivonovo)
                    encontrado += 1
            if nao_encontrado != encontrado:
                nao_encontrado = encontrado
            else:
                listanecontrado.append(x)


    print('')
    if encontrado == 0:
        print('=-'*20)
        print('      NENHUM XML encontrado')
        print('=-' * 20)
    if encontrado != 0:
        os.startfile(caminho_novo)
        print('Item Não encontrados: ')
        for num, item in enumerate(listanecontrado, start=1):
            print(f'{num} - {item}')


if os.path.exists(caminho_procura) == True:
    while True:
        print("""    ****************************** 
    ******   BuscaXML  V 1.5 *****
    ******************************
    ** MENU **** By Tulio Cafe ***
    
    1 Busca XML Individual
    2 Busca XML em serie
    3 Sair""")

        menu = int(input('Digite a Opção desejada: '))

        try:
            if menu == 1:
                localizarxml()
            elif menu == 2:
                sequencia()
            elif menu == 3:
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
    print(f'{caminho_procura} nao encontada')
    exit = input('Pressione ENTER para fechar')
