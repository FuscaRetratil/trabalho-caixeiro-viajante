from matplotlib import pyplot as plt
# Dicionário com os pontos
pontos = {
    1: (565.0, 575.0), 2: (25.0, 185.0), 3: (345.0, 750.0), 4: (945.0, 685.0), 5: (845.0, 655.0), 
    6: (880.0, 660.0), 7: (25.0, 230.0), 8: (525.0, 1000.0), 9: (580.0, 1175.0), 10: (650.0, 1130.0), 
    11: (1605.0, 620.0), 12: (1220.0, 580.0), 13: (1465.0, 200.0), 14: (1530.0, 5.0), 15: (845.0, 680.0), 
    16: (725.0, 370.0), 17: (145.0, 665.0), 18: (415.0, 635.0), 19: (510.0, 875.0), 20: (560.0, 365.0), 
    21: (300.0, 465.0), 22: (520.0, 585.0), 23: (480.0, 415.0), 24: (835.0, 625.0), 25: (975.0, 580.0), 
    26: (1215.0, 245.0), 27: (1320.0, 315.0), 28: (1250.0, 400.0), 29: (660.0, 180.0), 30: (410.0, 250.0), 
    31: (420.0, 555.0), 32: (575.0, 665.0), 33: (1150.0, 1160.0), 34: (700.0, 580.0), 35: (685.0, 595.0), 
    36: (685.0, 610.0), 37: (770.0, 610.0), 38: (795.0, 645.0), 39: (720.0, 635.0), 40: (760.0, 650.0), 
    41: (475.0, 960.0), 42: (95.0, 260.0), 43: (875.0, 920.0), 44: (700.0, 500.0), 45: (555.0, 815.0), 
    46: (830.0, 485.0), 47: (1170.0, 65.0), 48: (830.0, 610.0), 49: (605.0, 625.0), 50: (595.0, 360.0), 
    51: (1340.0, 725.0), 52: (1740.0, 245.0)
}

# Colar o caminho que quer plotar
ordem = [1, 22, 31, 18, 3, 17, 21, 42, 7, 2, 30, 23, 20, 50, 29, 16, 46, 44, 34, 35, 36, 39, 40, 37, 38, 48, 24, 5, 15, 6, 4, 25, 12, 28, 27, 26, 47, 13, 14, 52, 11, 51, 
33, 43, 10, 9, 8, 41, 19, 45, 32, 49, 1]
# Distancia do caminho
distancia = 7544.36590190409

# Extrair as coordenadas na ordem especificada
x_coords = [pontos[chave][0] for chave in ordem]
y_coords = [pontos[chave][1] for chave in ordem]

print(x_coords)
# Criar o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='blue', linewidth=0.5)  # Linhas e marcadores

# Adicionar setas entre os pontos
for i in range(len(ordem) - 1):
    plt.annotate('', xy=(x_coords[i + 1], y_coords[i + 1]), xytext=(x_coords[i], y_coords[i]),
                 arrowprops=dict(arrowstyle='->', color='y', lw=1.5))

# Destacar o ponto inicial e final
plt.scatter([x_coords[0]], [y_coords[0]], color='purple', zorder=10, label='1')
plt.scatter([x_coords[1]], [y_coords[1]], color='red', zorder = 5, label='22')
plt.scatter([x_coords[-2]], [y_coords[-2]], color='grey', zorder = 5, label='49')

# Adicionar títulos e rótulos
plt.title('distancia = %d' %(distancia))
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.show()
