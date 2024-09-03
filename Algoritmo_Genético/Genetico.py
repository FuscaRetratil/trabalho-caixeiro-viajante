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
    #pos = 0
        
    for pos in range(len(cromossomo)-1):
        if (pos+1) == 52:
            x1, y1 = ponto[cromossomo[pos]]
            x2, y2 = ponto[cromossomo[0]]
            distancia += distEuc(x1,y1,x2,y2)
        else:
            x1, y1 = ponto[cromossomo[pos]]
            x2, y2 = ponto[cromossomo[pos+1]]
            distancia += distEuc(x1,y1,x2,y2)

        #pos += 1
        #if pos == len(cromossomo)-1:
            #print('aaa')
    return 1/distancia, distancia

def aptidao_populacao(populacao):
    aptidao = [None]*len(populacao)
    custo = [None]*len(populacao)
    for i in range (len(populacao)):
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
        tamanho = len(pai1)
        ponto_cruzamento = randint(1, len(pai1) - 1)
        ponto_cruzamento2 = randint(ponto_cruzamento, len(pai1)-1)
        tam_filho = len(pai1)

        filho_1 = [None] * tam_filho
        filho_2 = [None] * tam_filho
        
        filho_1[ponto_cruzamento:ponto_cruzamento2 + 1] = pai1[ponto_cruzamento:ponto_cruzamento2+1]
        filho_2[ponto_cruzamento:ponto_cruzamento2 + 1] = pai2[ponto_cruzamento:ponto_cruzamento2+1]

        filho_1 = preenche_filho(filho_1, tamanho, pai2, ponto_cruzamento2 + 1)
        filho_2 = preenche_filho(filho_2, tamanho, pai1, ponto_cruzamento2 + 1)

        filho_1 = mutacao(filho_1, 0.05)
        filho_2 = mutacao(filho_2, 0.05)

        return filho_1, filho_2
    return pai1, pai2


def cruzamento(pais, taxa_cruzamento):
    lista_filhos = [None] * len(pais)
    i =0
    while i < len(pais):
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
    p1 = randint(0, len(populacao) -1)
    p2 = randint(0, len(populacao) -1)
    if p1 != p2:
        if aptidao_individuo(populacao[p1]) > aptidao_individuo(populacao[p2]):
            return p1
    return p2
    
def roleta(dic):
    valores = list(dic.values())
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
        id_sel = funcao(populacao, lista_apt)
        lista_pais[i] = populacao[id_sel]
    return lista_pais

def selecao_sobreviventes(populacao, aptidoes, filhos, aptidoes_filhos):
    return filhos, aptidoes_filhos



def imprimir_populacao(pop, apt, geracao):
    for i, apt in zip(pop, apt):
        print(f"genótipo: {ind}, fenótipo: {int(ind, 2)} | função objetivo: {apt_}")
    print(
        f"Melhor solução da geracao {geracao} é {pop[apt.index(max(apt))]} e sua aptidão é {max(apt)}"
    )
    print("*****************************")


def evolucao(pontos, tamanho, taxa_cruzamento, taxa_mutacao, n_geracoes, funcao):
    total = [float('inf')]*2010
    maior_apt = float('-inf')
    pop = populacao_inicial(ponto.keys(), tamanho)
    lista_apt, custo = aptidao_populacao(pop)
    print(min(custo))
    
    for geracao in range(n_geracoes):
        print('geracao->', geracao)
        pais = selecao_pais(pop, lista_apt, funcao)
        filhos = cruzamento(pais, taxa_cruzamento)
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
        pop, lista_apt = selecao_sobreviventes(pop, lista_apt, filhos, apt_filhos)
        
    print('minimo encontrado em 500 geracoes ->', min(total))
    print('caminho ->', menor_caminho)
    return pop, lista_apt



def principal():
    pontos = ponto.keys()
    taxa_cruzamento = 0.9
    taxa_mutacao = 0.1
    tam_cromossomo = 51
    tam_populacao = 80
    n_geracoes = 500
    funcao = torneio
    pop, lista_apt = evolucao(pontos, tam_populacao, taxa_cruzamento, taxa_mutacao, n_geracoes, funcao)
    
    
    
if __name__ == '__main__':
    principal()
