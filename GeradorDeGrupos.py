import csv
import random

def ExtrairNomes(nomeDoArquivo, listaACadastrar):
    Arquivo = open(nomeDoArquivo, "r")
    arquivo_csv = csv.reader(Arquivo, delimiter=",")
    for lista in arquivo_csv:
        for nome in lista:
            listaACadastrar.append(nome)
    Arquivo.close()
    return listaACadastrar

def GerarGrupos(lista, numGrupos):
    divisaoExata = len(lista) // numGrupos
    matriz = []

    # criando matriz
    for i in range(numGrupos):
        matriz.append([])

    # distribuindo "pessoas exatas" entre os grupos
    if(len(lista)%numGrupos==0):
        for nome in lista:
            while True:
                aleatorio = int(random.randint(0, numGrupos-1))

                if len(matriz[aleatorio]) < divisaoExata:
                    matriz[aleatorio].append(nome)
                    break

    # distribuindo "pessoas não exatas" entre os grupos
    else:
        limite = numGrupos*(len(lista)//numGrupos)
        for pos in range(0, limite):
            while True:
                aleatorio = int(random.randint(0, numGrupos-1))

                if len(matriz[aleatorio]) < divisaoExata:
                    matriz[aleatorio].append(lista[pos])
                    break
        del(lista[0:limite])

        for nome in lista:
            while True:
                aleatorio = int(random.randint(0, numGrupos-1))

                if len(matriz[aleatorio]) < divisaoExata+1:
                    matriz[aleatorio].append(nome)
                    break

    return matriz

def MostrarListaAleatoria(lista):
    indice = int(1)
    for grupo in lista:
        print("--------------------------------")
        print(f"PARTICIPANTES DO GRUPO {indice}")
        for nome in grupo:
            print(f"-{nome}")
        indice+=1
        
