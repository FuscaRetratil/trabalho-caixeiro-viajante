import random
import math
import time

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def KNN(Grafo):
    inicio = time.time()
    print("Começando . . .")
    vertice_atual = 0
    caminho_final = []
    vertices_restantes = []
    custo = 0
    
    for i in range(len(Grafo)):
        vertices_restantes.append(i)
    vertices_restantes.remove(vertice_atual)
    
    while len(vertices_restantes) != 0:
        distancia_minima = float('inf')
        proximo_vertice = None
        for i in vertices_restantes:
            distancia = calcular_distancia(vertice_atual, 0, i, 0)
            if distancia < distancia_minima:
                distancia_minima = distancia
                proximo_vertice = i
        custo += distancia_minima
        
        