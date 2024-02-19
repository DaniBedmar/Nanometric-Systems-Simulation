import matplotlib.pyplot as plt
import os
import numpy as np

# Leer el archivo de texto

l=["initial_conditions","1237K","1337K","1437K"]

for i in l:
    radio = []
    gofr = []
    archivo = f'{i}/gofr.txt'
    with open(archivo, 'r') as f:
        for x, linea in enumerate(f):
            if x<1001:
                r, g = linea.split()
                radio.append(float(r))
                gofr.append(float(g))
                
    # Crear la gráfica
    plt.figure(1)
    plt.plot(radio, gofr, '-', label = f'{i}')
    plt.xlabel('r [Å]')
    plt.ylabel('g(r)')
    plt.title(f'radial distribution function')
    plt.grid(False)
    plt.xticks(np.arange(0,10,1))
    plt.legend(loc='upper right')
    if (i == "initial_conditions"):
        Image_path = os.path.join(os.getcwd(), f'Plots/gofr_{i}.png')  
        plt.savefig(Image_path)
    if (i == "1437K"):
        Image_path = os.path.join(os.getcwd(), f'Plots/gofr_juntes.png')  
        plt.savefig(Image_path)
