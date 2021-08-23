import os
dir = os.listdir('c:\\python')
dir1 = os.scandir('c:\\python')
print(dir)
print(dir1)

print(type(dir1))

def copiaararquivos(nfce, caminho_busca,):
    encontrado = 0
    nao_encontrado = 0
    lista_nao_econtrado = []
    lista_encontrado = []
    for x in nfce:
        for raiz, diretorios, arquivos in os.walk(caminho_busca):
            print('raiz e', raiz)
            print('diretorio é', diretorios)
            # for arquivo in arquivos:
            #     if x in arquivo and '-nfe' in arquivo or x in arquivo and '-inu' in arquivo and '-ped' not in arquivo:
            #         caminho_arquivo = os.path.join(raiz, arquivo)
            #         print(f' {encontrado +1} -  XML Encontrados: {caminho_arquivo}  ')
            #         encontrado += 1
            #         lista_encontrado.append(caminho_arquivo)


# copiaararquivos(dir)
