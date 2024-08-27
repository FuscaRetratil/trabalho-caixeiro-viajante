from random import sample, randint

with open('Algoritmo_Genético//teste.txt','r') as arq:
    linhas, colunas = arq.readline().split()
    mapa = arq.read().split('\n')

PopulationSize = 10
coordenada = {}

for i in range(int(linhas)):
    mapa_linhas = mapa[i].split()
    j = -1
    if len(mapa_linhas) == int(colunas):
        for elemento in mapa_linhas:
            j += 1
            if elemento != '0':
                coordenada[elemento] = (i, j)

def Inicial_Population(DeliveryPoints):

    population = [i for i in DeliveryPoints.keys() if i!= 'R']
    inicial_population = []
    i = 0
    while i != PopulationSize:
        ip = sample(population, len(population))
        if ip not in  inicial_population:
            inicial_population.append(ip)
            i +=1
    return inicial_population

print(Inicial_Population(coordenada))

