import matplotlib.pyplot as plt
from itertools import permutations
from sys import maxsize
import time

inicial = time.time()

# dicionário para armazenar os pontos da matriz e as suas respectivas coordenadas
pontos = {}

# abrir o arquivo .txt
with open("Força_Bruta//rota.txt", "r") as entrada:
    matriz = []
    for i in entrada:
        matriz.append(i.split())
    matriz.remove(matriz[0])

    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[l][c] != "0":
                pontos[matriz[l][c]] = [l, c]

# calcular manhattan as distâncias entre os pontos
def distancias(ponto1, ponto2):
    return abs(ponto1[0] - ponto2[0]) + abs(ponto1[1] - ponto2[1])

# separar o ponto "R" dos demais pontos
ponto_inicial = "R"
outros_pontos = [p for p in pontos.keys() if p != ponto_inicial]

permutações = permutations(outros_pontos)

# calcular todas as distâncias e encontrar a menor delas
rotas = {maxsize: ("R", "D")}

for i in list(permutações):
    rota = [ponto_inicial] + list(i) + [ponto_inicial]
    acumulador_distancia = 0
    for coordenada in range(len(rota) - 1):
        acumulador_distancia += distancias(pontos[rota[coordenada]], pontos[rota[coordenada + 1]])

    menor_rota = list(rotas.keys())
    if acumulador_distancia < int(menor_rota[0]):
        rotas.clear()
        rotas[acumulador_distancia] = rota

# tirar o ponto 'R' e formatar em uma única string visual
menor_rota_visual = list(rotas[min(rotas.keys())])
menor_rota_visual.remove("R")
if menor_rota_visual[-1] == ponto_inicial:
    menor_rota_visual.pop()

# printar na tela a menor rota e a menor distância
print('=== FlyFood ===')
print('A menor rota é:')
print(" -> ".join(menor_rota_visual))
print(f'A menor distância é: {min(rotas.keys())}')

final = time.time()
print("Tempo de execução: ", final - inicial)

# visualização dos gráficos
rota_completa = [ponto_inicial] + menor_rota_visual + [ponto_inicial]
x_coords = [pontos[p][1] for p in rota_completa]
y_coords = [pontos[p][0] for p in rota_completa]

plt.figure(figsize=(8, 8))
plt.plot(x_coords, y_coords, marker='o', color='b', linestyle='-', label='Rota')
for ponto, coord in pontos.items():
    plt.text(coord[1], coord[0], ponto, fontsize=12, ha='right')
plt.scatter(x_coords[0], y_coords[0], color='r', label='Ponto Inicial (R)')

plt.title("Visualização da Menor Rota - FlyFood")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")
plt.grid(True)
plt.legend()
plt.show()
