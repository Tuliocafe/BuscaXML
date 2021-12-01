import os
from zipfile import ZipFile

abc = []
try:
    abc[0].append('o1')
except:
    abc.append([])
    abc[0].append('o1')
print(abc)
var = 20005
var = str(var)
print(var[1:])
print(abc)
lista = [['d', 'a', 'b', 'c'], [1, 3, 2]]
lista[0].sort()
print(lista)

teste = 0
teste += 1
teste += 1
print(teste)
arquivo = r"c:\teste"
with ZipFile(arquivo + r"\123\arq.rar", "w") as rar:
    rar.write(arquivo + r"\123\1.txt")


# manipulador = open('C:\Program Files (x86)\TronSolution\TSEmissorNFCe.ini', 'r')
# for c in range(0, 8):
#     manipulador.readline()
# caminho_busca = manipulador.readline()[8:]
# caminho_busca = repr(caminho_busca.encode('utf-8', 'ignore'))[2:-2] + '\\'
# manipulador.close()
# print(caminho_busca)
#
# caminho_copia = 'c:\\Mafra\\XML_Separado\\'
# print(caminho_copia)
# os.startfile(caminho_copia)

from datetime import date
data = date.today()
print(data.month -1)
datastr = (date.month -1)


