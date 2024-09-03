import random
import math
import time


def ler_arquivo(nome_arquivo):
    grafo = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            valores = linha.split()
            grafo += [[int(valores[0]), float(valores[1]), float(valores[2])]]
    return grafo


def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def vmp(grafo):
    inicio = time.time()
    print("Começando . . .")
    vertice_atual = random.choice(range(len(grafo)))
    caminho_final = [vertice_atual]
    vertices_restantes = []
    custo = 0

    for i in range(len(grafo)):
        vertices_restantes.append(i)
    vertices_restantes.remove(vertice_atual)

    while len(vertices_restantes) != 0:
        distancia_minima = float('inf')
        proximo_vertice = None
        for i in vertices_restantes:
            distancia = calcular_distancia(grafo[vertice_atual][1], grafo[vertice_atual][2], grafo[i][1], grafo[i][2])
            if distancia < distancia_minima:
                distancia_minima = distancia
                proximo_vertice = i
        custo += distancia_minima

        caminho_final.append(proximo_vertice)
        vertices_restantes.remove(proximo_vertice)
        vertice_atual = proximo_vertice

    custo += calcular_distancia(vertice_atual, 0, caminho_final[0], 0)
    caminho_final.append(caminho_final[0])

    print("Caminho final:", caminho_final)
    print("Custo total:", custo)
    print("Tempo de execução:", time.time() - inicio)


nome_arquivo = "coordenadas.txt"
Grafo = ler_arquivo(nome_arquivo)
vmp(Grafo)
