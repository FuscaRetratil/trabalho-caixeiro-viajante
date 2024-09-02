from random import random, randint
from typing import List, Tuple, Callable
from math import floor
import math

berlin52 = [None]*52
ponto = {}

with open('berlin52.tsp','r') as arq:
    linhas = arq.readlines()[6:-2]
    for i in range(len(linhas)):
        berlin52[i] = linhas[i].split()
        ponto[int(berlin52[i][0])] = (float(berlin52[i][1]), float(berlin52[i][2]))
        
            

#pop = [['B', 'D', 'A', 'C'], ['C', 'D', 'B', 'A'], ['D', 'A', 'B', 'C'], ['A', 'C', 'B', 'D'], ['B', 'C', 'A', 'D'], ['D', 'A', 'C', 'B'], ['C', 'A', 'B', 'D'], ['B', 'D', 'C', 'A'], ['A', 'D', 'B', 'C'], ['D', 'B', 'C', 'A']]


def cromossomo (pontos, tam_cromo = 51):
    cromossomo = [None] * tam_cromo
    i=0
    while i < tam_cromo:
        num = randint(2, len(pontos))
        if num not in cromossomo:
            cromossomo[i] = num
            i+=1
    return cromossomo

def populacao_inicial (pontos, tamanho):
    populacao = [None] * tamanho
    for i in range(tamanho):
        populacao[i] = cromossomo(pontos)
    return populacao
    

def distEuc(x1,y1,x2,y2):
    distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distancia

def aptidao_individuo(cromossomo):
    distancia = 0
    pos = 0
    cromossomo.insert(0,1)
    cromossomo.insert(len(cromossomo),1)
    while pos in range(len(cromossomo)-1):
        x1,y1 = ponto[cromossomo[pos]]
        x2, y2 = ponto[cromossomo[pos+1]]
        distancia += distEuc(x1,y1,x2,y2)

        pos += 1
    return 1/distancia

def aptidao_populacao(populacao):
    aptidao = {}
    for i in range (len(populacao)):
        aptidao[i] = aptidao_individuo(populacao[i])
    return aptidao


def preenche_filho(filho, tamanho, pai, ponto_cruzamento):
    pos = ponto_cruzamento
    for gene in pai:
        if gene not in filho:
            while pos < tamanho and filho[pos] is not None:
                pos += 1
            if pos < tamanho:
                filho[pos] = gene
        #remenda
        if filho[52] == None:
            filho[52] = 1
    return filho
                
    
def cruzamento_pais (pai1, pai2, taxa_cruzamento):
    if random() <= taxa_cruzamento:
        ponto_cruzamento = randint(1, len(pai1) - 1)
        tam_filho = len(pai1)

        filho_1 = [None] * tam_filho
        filho_2 = [None] * tam_filho
        
        filho_1[:ponto_cruzamento] = pai1[:ponto_cruzamento]
        filho_2[:ponto_cruzamento] = pai2[:ponto_cruzamento]

        filho_1 = preenche_filho(filho_1, tam_filho, pai2, ponto_cruzamento)
        filho_2 = preenche_filho(filho_2, tam_filho, pai1, ponto_cruzamento)

        return filho_1, filho_2
    return pai1, pai2


def cruzamento(pais, taxa_cruzamento):
    lista_filhos = [None] * len(pais)
    for i in range(0, len(pais), 2):
        filho1, filho2 = cruzamento_pais(pais[i], pais[i+1], taxa_cruzamento)
        lista_filhos[i] = filho1
        lista_filhos[i+1] = filho2
    return lista_filhos

def mutacao(filho, taxa_mutacao):
    filho_mutado = filho
    indice_A = randint(0, len(filho)-1)
    indice_B = randint(0, len(filho)-1)
    print(filho[indice_A], filho[indice_B])
    if random() <= taxa_mutacao:
        troca(filho_mutado, indice_A, indice_B)
    return filho_mutado

def troca(lista, id1, id2):
    lista[id1], lista[id2] = lista[id2], lista[id1]
    
def torneio(populacao):
    p1 = randint(0, len(populacao) -1)
    p2 = randint(0, len(populacao) -1)
    if aptidao_individuo(populacao[p1]) > aptidao_individuo(populacao[p2]):
        return p1
    return p2
    
def roleta(dic):
    valores = list(dic)
    soma_atual = 0
    soma_roleta = sum(valores)
    n_sorteado = random() * soma_roleta
    for i, valor in enumerate(valores):
        soma_atual += valor
        if soma_atual >= n_sorteado:
            return i
    
def selecao_pais(populacao, lista_apt, funcao):
    lista_pais = [None] * len(populacao)
    for i in range(len(populacao)):
        id_sel = funcao(lista_apt)
        lista_pais[i] = populacao[id_sel]
    return lista_pais

def selecao_sobreviventes(populacao, aptidoes, filhos, aptidoes_filhos):
    return filhos, aptidoes_filhos

'''

def imprimir_populacao(pop, apt, geracao):
    for i, apt in zip(pop, apt):
        print(f"genótipo: {ind}, fenótipo: {int(ind, 2)} | função objetivo: {apt_}")
    print(
        f"Melhor solução da geracao {geracao} é {pop[apt.index(max(apt))]} e sua aptidão é {max(apt)}"
    )
    print("*****************************")


def evolucao(pontos, tamanho, taxa_cruzamento, taxa_mutacao, n_geracoes, funcao):
    pop = populacao_inicial(ponto.keys(), tamanho)
    lista_apt = list(aptidao_populacao(pop).values())
    for geracao in range(n_geracoes):
        pais = selecao_pais(pop, lista_apt, funcao)
        filhos = cruzamento(pais, taxa_cruzamento)
        apt_filhos = list(aptidao_populacao(filhos).values())
        pop, lista_apt = selecao_sobreviventes(pop, lista_apt, filhos, apt_filhos)
    return pop, lista_apt



def principal():
    pontos = ponto.keys()
    taxa_cruzamento = 0.6
    taxa_mutacao = 0.1
    tam_cromossomo = 51
    tam_populacao = 8
    n_geracoes = 4
    funcao = roleta
    pop, lista_apt = evolucao(pontos, tam_cromossomo, taxa_cruzamento, taxa_mutacao, n_geracoes, funcao)
    
    
    
if __name__ == '__main__':
    principal()




'''

