import random
import math
import time
import networkx as nx
import matplotlib.pyplot as plt


def ler_arquivo(arquivo):
    grafo = {}
    with open(arquivo, 'r') as arq:
        for linha in arq:
            valores = linha.split()
            vertice_id = int(valores[0])
            grafo[vertice_id] = (float(valores[1]), float(valores[2]))
    return grafo


def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def vizinho_mais_proximo(grafo):
    print("Começando . . .")
    vertice_atual = random.choice(list(grafo.keys()))
    caminho_final = [vertice_atual]
    vertices_restantes = set(grafo.keys())
    vertices_restantes.discard(vertice_atual)
    custo = 0

    inicio = time.time()
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

        caminho_final.append(proximo_vertice)
        vertices_restantes.discard(proximo_vertice)
        vertice_atual = proximo_vertice

    custo += calcular_distancia(grafo[vertice_atual][0], grafo[vertice_atual][1],
                                grafo[caminho_final[0]][0],
                                grafo[caminho_final[0]][1])
    caminho_final.append(caminho_final[0])
    fim = time.time()
    tempo_execucao = fim - inicio

    return custo, caminho_final, tempo_execucao


def imprime_resultados(custos, tempos):
    media_custos = sum(custos) / len(custos)
    media_tempos = sum(tempos) / len(tempos)
    print(f"Média dos custos após 30 execuções: {media_custos}")
    print(f"Média dos tempos após 30 execuções: {media_tempos}")
    return media_custos, media_tempos


def salvar_resultados(custos, caminhos, tempos, arquivo_nome):
    with open(arquivo_nome, 'w') as arq_nome:
        for i, (custo, caminho, tempo) in enumerate(zip(custos, caminhos, tempos)):
            arq_nome.write(
                f"Execucao {i + 1}: Custo = {custo}, Caminho = {caminho} e Tempo = {tempo}\n")
        media_custos = sum(custos) / len(custos)
        media_tempos = sum(tempos) / len(tempos)
        arq_nome.write(f"Média dos custos após 30 execuções: {media_custos}\n")
        arq_nome.write(f"Média dos tempos após 30 execuções: {media_tempos}\n")


def plot_grafo(grafo, caminho):
    G = nx.Graph()
    for vertice, coordenadas in grafo.items():
        G.add_node(vertice, pos=coordenadas)
    for i in range(len(caminho) - 1):
        G.add_edge(caminho[i], caminho[i + 1])
    pos = nx.get_node_attributes(G, "pos")
    nx.draw(G, pos, with_labels=False, node_color="lightgreen",
            edge_color="gray", node_size=500, font_size=8)
    nx.draw_networkx_edges(G, pos, edgelist=[(caminho[i], caminho[i + 1])
                                             for i in range(len(caminho) - 1)], edge_color="red", width=2)
    plt.title("Grafo com Caminho do Vizinho Mais Próximo")
    plt.grid(True)
    plt.show()


def main():
    nome_arquivo = "coordenadas.txt"
    custos = []
    caminhos = []
    tempos = []
    for i in range(30):
        Grafo = ler_arquivo(nome_arquivo)
        custo, caminho, tempo = vizinho_mais_proximo(Grafo)
        custos.append(custo)
        caminhos.append(caminho)
        tempos.append(tempo)
        print(f"Execução {i + 1}: Custo = {custo}")

    imprime_resultados(custos, tempos)
    salvar_resultados(custos, caminhos, tempos, "resultados.txt")
    plot_grafo(Grafo, caminhos[0])


if __name__ == "__main__":
    main()
