import os
import shutil
import re

rangexml = []
listanfce = []
listanfcetemp = []
caminho_procura = r'c:\Mafra\XML'
caminho_novo = r'c:\Mafra\XML_Novo'


def sequencia():
    serie = str(input('Digite a SERIE do XML ou pressione ENTER para 002: '))
    if serie == '':
        serie = '002'

    elif serie.isdigit() and len(serie) <= 3:
        serie = '0' * (3 - len(serie)) + serie

    elif len(serie) >= 4:
        print('Digito errado, tente novamente! ')

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

    else:
        print('Numero digitado errado')


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

    cont = 0
    for raiz, diretorios, arquivos in os.walk(caminho_procura):
        for arquivo in arquivos:
            print(arquivo)
            for x in nfce:
                if x in arquivo:
                    caminho_antigo = os.path.join(raiz, arquivo)
                    print(f' {cont +1} XML Encontrados: {caminho_antigo}  ')
                    mov_arquivonovo = os.path.join(caminho_novo, arquivo)
                    shutil.copy(caminho_antigo, mov_arquivonovo)
                    cont += 1

    print('')
    if cont == 0:
        print('=-'*20)
        print('      NENHUM XML encontrado')
        print('=-' * 20)
    if cont != 0:
        os.startfile(caminho_novo)


if os.path.exists(caminho_procura) == True:
    while True:
        print("""    ****************************** 
    ******   BuscaXML  V 1.0 *****
    ******************************
    ** MENU **** By Tulio Cafe ***
    1 Busca XML Individual
    2 Busca XML em serie
    3 Sair""")

        menu = int(input('Digite o numero: '))

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
    print('Pasta C:\\mafra\\xml nao encontada')
    exit = input('Pressione ENTER para fechar')
