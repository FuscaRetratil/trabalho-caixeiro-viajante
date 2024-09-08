from random import random, randint
import time
import math

berlin52 = [None]*52
ponto = {}
with open('berlin52.tsp','r') as arq:
    linhas = arq.readlines()[6:-2]
    for i in range(len(linhas)):
        berlin52[i] = linhas[i].split()
        ponto[int(berlin52[i][0])] = (float(berlin52[i][1]), float(berlin52[i][2]))
        berlin52[i] = [int(berlin52[i][0]), float(berlin52[i][1]), float(berlin52[i][2])]
        
            

#pop = [['B', 'D', 'A', 'C'], ['C', 'D', 'B', 'A'], ['D', 'A', 'B', 'C'], ['A', 'C', 'B', 'D'], ['B', 'C', 'A', 'D'], ['D', 'A', 'C', 'B'], ['C', 'A', 'B', 'D'], ['B', 'D', 'C', 'A'], ['A', 'D', 'B', 'C'], ['D', 'B', 'C', 'A']]


def individuo (pontos, tam_indiv = 51):
    tam_pontos = len(pontos)
    individuo = [None] * tam_indiv
    i=0
    while i < tam_indiv:
        num = randint(2, tam_pontos)
        if num not in individuo:
            individuo[i] = num
            i+=1
    return individuo

def populacao_inicial (pontos, tamanho, tam_gulosos, grafo):
    populacao = [None] * tamanho
    for i in range(tam_gulosos):
        inicio_guloso = randint(1,51)
        populacao[i] = guloso(grafo, inicio_guloso)
    for i in range(tam_gulosos, tamanho):
        populacao[i] = individuo(pontos)
    return populacao
    
def guloso (grafo, inicio):
    vertice_atual = inicio
    caminho_final = [vertice_atual]
    vertices_restantes = [i for i in range(len(grafo)) if i != vertice_atual and i!=0]
    custo = 0

    while len(vertices_restantes) != 0:
        distancia_minima = float('inf')
        proximo_vertice = None
        for i in vertices_restantes:
            distancia = distEuc(grafo[vertice_atual][1], grafo[vertice_atual][2], grafo[i][1], grafo[i][2])
            if distancia < distancia_minima:
                distancia_minima = distancia
                proximo_vertice = i
        custo += distancia_minima

        caminho_final = caminho_final + [proximo_vertice]  #adiciona ao caminho final
        vertices_restantes = [v for v in vertices_restantes if v != proximo_vertice]  #remove da lista de restantes
        vertice_atual = proximo_vertice  #atualiza o vertice atual

    custo += distEuc(grafo[vertice_atual][1], grafo[vertice_atual][2], grafo[caminho_final[0]][1],grafo[caminho_final[0]][2])
    caminho_final = caminho_final

    for i, ponto in enumerate (caminho_final):
        ponto += 1
        caminho_final[i] = ponto

    return caminho_final

def distEuc(x1,y1,x2,y2):
    distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distancia

def aptidao_individuo(individuo):
    tam_individuo = len(individuo)
    distancia = 0
    x, y = ponto[individuo[0]]
    distancia += distEuc(565, 575, x, y)
    pos = 0       
    for pos in range(tam_individuo - 1):
            x1, y1 = ponto[individuo[pos]]
            x2, y2 = ponto[individuo[pos+1]]
            distancia += distEuc(x1,y1,x2,y2)

    distancia += distEuc(x2, y2, 565, 575)
    return 1/distancia, distancia

def aptidao_populacao(populacao):
    tam_populacao = len(populacao)
    aptidao = [None]*tam_populacao
    custo = [None]*tam_populacao
    for i in range (tam_populacao):
        aptidao[i], custo[i] = aptidao_individuo(populacao[i])
    return aptidao, custo


def preenche_filho(filho, tamanho, pai, ponto_cruzamento):
    pos = ponto_cruzamento
    for gene in pai:
            if gene not in filho:
                if pos >= tamanho:
                    pos = 0
                filho[pos] = gene
                pos += 1
    return filho
                
    
def cruzamento_pais (pai1, pai2, taxa_cruzamento):
    if random() <= taxa_cruzamento:
        tam_pai = len(pai1)
        ponto_cruzamento = randint(1, tam_pai - 1)
        ponto_cruzamento2 = randint(ponto_cruzamento, tam_pai - 1)
        tam_filho = len(pai1)

        filho_1 = [None] * tam_filho
        filho_2 = [None] * tam_filho
        
        filho_1[ponto_cruzamento:ponto_cruzamento2 + 1] = pai1[ponto_cruzamento:ponto_cruzamento2+1]
        filho_2[ponto_cruzamento:ponto_cruzamento2 + 1] = pai2[ponto_cruzamento:ponto_cruzamento2+1]

        filho_1 = preenche_filho(filho_1, tam_pai, pai2, ponto_cruzamento2 + 1)
        filho_2 = preenche_filho(filho_2, tam_pai, pai1, ponto_cruzamento2 + 1)

        return filho_1, filho_2
    return pai1, pai2


def cruzamento(pais, taxa_cruzamento):
    tam_pais = len(pais)
    lista_filhos = [None] * tam_pais
    i = 0
    while i < tam_pais:
        filho1, filho2 = cruzamento_pais(pais[i], pais[i+1], taxa_cruzamento)
        lista_filhos[i] = filho1
        lista_filhos[i+1] = filho2
        i+=2
    return lista_filhos

def mutacao(filho, taxa_mutacao):
    filho_mutado = filho
    indice_A = randint(0, len(filho)-1)
    indice_B = randint(0, len(filho)-1)
    if random() <= taxa_mutacao:
        troca(filho_mutado, indice_A, indice_B)
    return filho_mutado

def troca(lista, id1, id2):
    lista[id1], lista[id2] = lista[id2], lista[id1]
    
def torneio(populacao, lista_apt):
    tam_populacao = len(populacao)
    p1 = randint(0, tam_populacao -1)
    p2 = randint(0, tam_populacao -1)
    if p1 != p2:
        if aptidao_individuo(populacao[p1]) > aptidao_individuo(populacao[p2]):
            return p1
    return p2
    
    
def selecao_pais(populacao, lista_apt, funcao):
    tam_populacao = len(populacao)
    lista_pais = [None] * tam_populacao
    for i in range(tam_populacao):
        id_sel = funcao(populacao, lista_apt)
        lista_pais[i] = populacao[id_sel]
    return lista_pais



def selecao_sobreviventes(populacao, aptidoes, filhos, aptidoes_filhos):
    pop = populacao + filhos
    apt = aptidoes + aptidoes_filhos
    
    pop_aptidao = ordena_populacao(pop, apt)

    tam_populacao = len(populacao)

    nova_populacao = [individuo for individuo, i in pop_aptidao[:tam_populacao]]
    nova_aptidao = [aptidao for i, aptidao in pop_aptidao[:tam_populacao]]
    
    return nova_populacao, nova_aptidao

def heapify(arr, n, i, pos_apt):
    maior = i 
    esq = 2 * i + 1  
    dir = 2 * i + 2  
    
    if esq < n and arr[esq][pos_apt] < arr[maior][pos_apt]:
        maior = esq

    if dir < n and arr[dir][pos_apt] < arr[maior][pos_apt]:
        maior = dir

    if maior != i:
        arr[maior], arr[i] = arr[i], arr[maior]  
        
        heapify(arr, n, maior, pos_apt)

def heap_sort(pop_apt, pos_apt):
    n = len(pop_apt)

    for i in range(n // 2 - 1, -1, -1):
        heapify(pop_apt, n, i, pos_apt)

    for i in range(n - 1, 0, -1):
        pop_apt[0], pop_apt[i] = pop_apt[i], pop_apt[0]
        heapify(pop_apt, i, 0, pos_apt)


def ordena_populacao(populacao, lista_apt):
    populacao = list(zip(populacao, lista_apt))
    heap_sort(populacao,1)
    return populacao


def evolucao(pontos, tamanho, qtd_guloso, grafo, taxa_cruzamento, taxa_mutacao, n_geracoes, funcao):
    total = [float('inf')]*n_geracoes
    maior_apt = float('-inf')
    pop = populacao_inicial(ponto.keys(), tamanho, qtd_guloso, grafo)
    lista_apt, custo = aptidao_populacao(pop)
    print(min(custo))
    
    for geracao in range(n_geracoes):
        print('geracao->', geracao)
        pais = selecao_pais(pop, lista_apt, funcao)

        filhos = cruzamento(pais, taxa_cruzamento)
        filhos = mutacao(filhos, taxa_mutacao)

        apt_filhos, custos = aptidao_populacao(filhos)

        total[geracao] = min(custos)
        aptidao_geracao = max(apt_filhos)
        if maior_apt < aptidao_geracao:
            maior_apt = aptidao_geracao
            indice_caminho = apt_filhos.index(maior_apt)
            menor_caminho = filhos[indice_caminho]
        print('maior aptidao', maior_apt)
        print('custo-geracao->', min(custos))
        print('menor-custo->', min(total))
        print('****************************************************')
        pop, lista_apt = selecao_sobreviventes(pop, lista_apt, filhos, apt_filhos)
    menor_custo = min(total)
    print('CUSTO MÍNIMO ENCONTRADO EM %d GERACOES ->' %(n_geracoes), menor_custo)
    print('CAMINHO DE MENOR CUSTO ->', menor_caminho)
    return menor_caminho, menor_custo



def principal():
    inicio_cronometro = time.time()
    qtd_gulosos = 35
    grafo = berlin52
    pontos = ponto.keys()
    taxa_cruzamento = 0.9
    taxa_mutacao = 0.05
    tam_populacao = 100




    n_geracoes = 100

    funcao = torneio
    custo_total = 0
    menor_custo = float('inf')
    for i in range(30):
        caminho, custo_f = evolucao(pontos, tam_populacao, qtd_gulosos, grafo, taxa_cruzamento, taxa_mutacao, n_geracoes, funcao)
        custo_total += custo_f
        if custo_f < menor_custo:
            menor_custo = custo_f
            caminho_f = caminho
    
    print('----------------------------------------------')
    print('MEDIA DO CUSTO ->>>>', custo_total/30)
    print()
    fim_cronometro = time.time()
    tempo = fim_cronometro - inicio_cronometro
    print('MEDIA DE T(s) ->>>>>>', tempo/30)
    print('menor custo entre todas as iterações ->>>>>>>', menor_custo)
    print()
    print('CAMINHO DE MENOR CUSTO->>>>>>', caminho_f)
    custo_total = 0
    
    
if __name__ == '__main__':
    principal()