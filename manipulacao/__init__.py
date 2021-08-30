import shutil
import re
import os
from zipfile import *
import xml.etree.ElementTree as et

rangexml = []
listanfce = []
listanfcetemp = []


def sequencia(caminho_busca, caminho_copia, serie, seq1, seq2):
    """ Busca o XML pela seguencia de um numero ao outro, (caminho da busca , caminho da copia do arquivo,
     serie, primeiro numero da sequencia, ultimo numero da sequencia.)"""

    if serie == '':
        serie = '002'
    elif serie.isdigit() and len(serie) <= 3:
        serie = '0' * (3 - len(serie)) + serie
    elif len(serie) >= 4:
        print('Digito errado, tente novamente! ')
    else:
        print('Numero digitado errado')

    numero = str(str(seq1) + ' ' + str(seq2))
    listanfcetemp = re.sub("[^0-9]", " ", numero).strip().split(' ')

    for n in range(0, len(listanfcetemp)):
        if listanfcetemp[n].isdigit():
            rangexml.append(listanfcetemp[n])

    try:
        for c in range(int(rangexml[0]), int(rangexml[1]) + 1):
            listanfce.append(str(serie + '0' * (9 - len(str(c))) + str(c)))

    except IndexError:
        print('**************************')
        print('Digito é invalido!!!')
        print('Favor inserir inicio e o final da serie!!')
        print('')

    copiaararquivos(listanfce, caminho_busca, caminho_copia)
    listanfcetemp.clear()
    listanfce.clear()
    rangexml.clear()


def localizarxml(caminho_busca, caminho_copia, serie, numero):
    """ Busca o XML pelo parametro informado no inicio (caminho da busca , caminho da copia do arquivo,
     serie e numero do NFCE)"""
    if serie == '':
        serie = '002'

    elif serie.isdigit() and len(serie) <= 3:
        serie = '0' * (3 - len(serie)) + serie

    elif len(serie) >= 4:
        print('Digito errado, tente novamente! ')

    else:
        print('Numero digitado errado')

    listanfcetemp = re.sub("[^0-9]", " ", numero).strip().split(' ')

    for n in range(0, len(listanfcetemp)):
        if listanfcetemp[n].isdigit():
            listanfce.append(serie + '0' * (9 - len((listanfcetemp[n]))) + listanfcetemp[n])
    copiaararquivos(listanfce, caminho_busca, caminho_copia)
    listanfce.clear()
    listanfcetemp.clear()


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
            if not diretorios:
                break
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
    try:
        for apagar in teste_vazio:
            os.remove(caminho_copia + "\\" + apagar)

    except:
        print('Digito Invalido')
        pass


def validar_arquivos(caminho):
    for _, diretorios, arquivoXML in os.walk(caminho):

        for arquivo in arquivoXML:
            arquivoabsoluto = caminho + '\\' + arquivo
            try:
                tree = et.parse(arquivoabsoluto)
                root = tree.getroot()
                for child in root.iter():
                    if child.tag == '{http://www.portalfiscal.inf.br/nfe}cNF':
                        print(f' Verificando nota {child.text}.', end=' ')
                    if child.tag == '{http://www.portalfiscal.inf.br/nfe}xJust':
                        print('Nota nao validada')
                    elif child.tag == '{http://www.portalfiscal.inf.br/nfe}xMotivo':
                        print('Validada')
            except:
                pass



        if not diretorios:
            break
