import random
import math


<<<<<<< Updated upstream
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    num_vertices = len(linhas)
    grafo = [[0] * 3 for _ in range(num_vertices)]
    for i, linha in enumerate(linhas):
        valores = linha.split()
        grafo[i] = [int(valores[0]), float(valores[1]), float(valores[2])]
=======
def ler_arquivo(arquivo):
    grafo = {}
    with open(arquivo, 'r') as arq:
        for linha in arq:
            valores = linha.split()
            vertice_id = int(valores[0])
            grafo[vertice_id] = (float(valores[1]), float(valores[2]))
>>>>>>> Stashed changes
    return grafo


def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def vizinho_mais_proximo(grafo):
    print("Começando . . .")
<<<<<<< Updated upstream
    vertice_atual = random.choice(range(len(grafo)))
    caminho_final = [vertice_atual]
    vertices_restantes = [i for i in range(len(grafo)) if i != vertice_atual]
=======
    vertice_atual = random.choice(list(grafo.keys()))
    caminho_final = set()
    caminho_final.add(vertice_atual)
    vertices_restantes = set(grafo.keys())
    vertices_restantes.discard(vertice_atual)
>>>>>>> Stashed changes
    custo = 0

    while len(vertices_restantes) != 0:
        distancia_minima = float('inf')
        proximo_vertice = None
        for i in vertices_restantes:
            distancia = calcular_distancia(grafo[vertice_atual][0],  
                                           grafo[vertice_atual][1],  
                                           grafo[i][0], grafo[i][1])
            if distancia < distancia_minima:
                distancia_minima = distancia
                proximo_vertice = i
        custo += distancia_minima

<<<<<<< Updated upstream
        caminho_final = caminho_final + [proximo_vertice]  #adiciona ao caminho final
        vertices_restantes = [v for v in vertices_restantes if v != proximo_vertice]  #remove da lista de restantes
        vertice_atual = proximo_vertice  #atualiza o vertice atual

    custo += calcular_distancia(grafo[vertice_atual][1], grafo[vertice_atual][2], grafo[caminho_final[0]][1],grafo[caminho_final[0]][2])
    caminho_final = caminho_final + [caminho_final][0]
=======
        caminho_final.add(proximo_vertice)
        vertices_restantes.discard(proximo_vertice)
        vertice_atual = proximo_vertice

    custo += calcular_distancia(grafo[vertice_atual][0], grafo[vertice_atual][1],
                                grafo[list(caminho_final)[-1]][0], grafo[list(caminho_final)[-1]][1])
    caminho_final.add(list(caminho_final)[0])
>>>>>>> Stashed changes

    return custo


custos = ""
nome_arquivo = "coordenadas.txt"
for i in range(30):
    Grafo = ler_arquivo(nome_arquivo)
    custo = vizinho_mais_proximo(Grafo)
    custos += str(custo) + ","
    print(f"Execução {i + 1}: Custo = {custo}")

custos_lista = [float(custo) for custo in custos.strip(',').split(',')]

media_custos = sum(custos_lista) / len(custos_lista)
print(f"Média dos custos após 30 execuções: {media_custos}")
