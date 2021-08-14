import shutil
import re
import os
from zipfile import *

rangexml = []
listanfce = []


def menuprincipal():
    print("""    ------------------------------ 
    ------   BuscaXML  V 1.6 -----
    ------------------------------
    -- MENU ---- By Tulio Cafe ---

    1 - Busca XML Individual
    2 - Busca XML pela sequencia ex: (de x a y)
    3 - Excluir arquivo da pasta XML_Novo
    9 - Sair
    """)


def sequencia(caminho_busca, caminho_copia, serie, seq1, seq2):
    if serie == '':
        serie = '002'

    elif serie.isdigit() and len(serie) <= 3:
        serie = '0' * (3 - len(serie)) + serie

    elif len(serie) >= 4:
        print('Digito errado, tente novamente! ')


    else:
        print('Numero digitado errado')


    # print('')
    # print('Deve colocar o numero da NFCE inicial e o final ex: "30 a 40"')
    # print('')

    numero = str(seq1 + ' ' + seq2)
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

    copiaararquivos(listanfce, caminho_busca, caminho_copia)


def localizarxml(caminho_busca, caminho_copia, serie, numero):
    """ Busca o XML pelo parametro informado no inicio"""
    # serie = str(input('Digite a SERIE da NFCE ou pressione ENTER para 002: '))
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
#     print("""Pode colocar varios NFCEs de uma vez.
# o sistema vai ignorar letras e buscar todos os numeros que foram inceridos""")
    print('')
    # numero = str(input('Quais NFCEs ? '))
    listanfcetemp = re.sub("[^0-9]", " ", numero).strip().split(' ')

    for n in range(0, len(listanfcetemp)):
        if listanfcetemp[n].isdigit():
            listanfce.append(serie + '0' * (9 - len((listanfcetemp[n]))) + listanfcetemp[n])
    copiaararquivos(listanfce, caminho_busca, caminho_copia)


def copiaararquivos(nfce, caminho_busca, caminho_copia):
    for item in nfce:
        print(f'Procurando item {item}')
    print('')
    try:
        os.mkdir(r'C:\Mafra\XML_Novo')
    except FileExistsError:
        pass

    encontrado = 0
    nao_encontrado = 0
    lista_nao_econtrado = []
    lista_encontrado = []
    for x in nfce:
        for raiz, diretorios, arquivos in os.walk(caminho_busca):
            for arquivo in arquivos:
                if x in arquivo and '-nfe' in arquivo or x in arquivo and '-inu' in arquivo and '-ped' not in arquivo:
                    caminho_arquivo = os.path.join(raiz, arquivo)
                    print(f' {encontrado +1} -  XML Encontrados: {caminho_arquivo}  ')
                    encontrado += 1
                    lista_encontrado.append(caminho_arquivo)
            if nao_encontrado != encontrado:
                nao_encontrado = encontrado
            else:
                lista_nao_econtrado.append(x)

    if len(lista_encontrado) >= 5:
        with ZipFile(caminho_copia+r"\XMLfaltante.rar", "w") as rar:
            for nome in lista_encontrado:
                rar.write(nome)
    else:
        for copia in lista_encontrado:
            shutil.copy(copia, copia.replace("XML", "XML_Novo"))

    print('')

    if encontrado == 0:
        print('=-'*20)
        print('      NENHUM XML encontrado')
        print('=-' * 20)
    if encontrado != 0:
        os.startfile(caminho_copia)
        print('Item Não encontrados: ')
        for num, item in enumerate(lista_nao_econtrado, start=1):
            print(f'{num} - {item}')


def detectar_arquivo(caminho_copia):
    try:
        teste_vazio = os.listdir(caminho_copia)
        if not teste_vazio:
            pass
        else:
            for verificar_arquivo in teste_vazio:
                if os.path.isdir(caminho_copia + "\\" + verificar_arquivo):
                    pass
                else:
                    print('Foi detectado arquivos na pasta XML_Novo.')
                    return teste_vazio
    except:
        pass

def apagar_arquivo(teste_vazio, caminho_copia):
    print("ESSE PROCEDIMENTO IRA APAGAR TODOS OS ARQUIVOS DA PASTA XML_novo.")
    try:
        for apagar in teste_vazio:
            os.remove(caminho_copia + "\\" + apagar)
        else:
            print('Digito Invalido')
    except:
        pass