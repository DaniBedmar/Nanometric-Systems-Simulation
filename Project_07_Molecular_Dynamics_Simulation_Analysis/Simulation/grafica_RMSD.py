#Codi per crear gràfiques per cada una de les simulacions

import matplotlib.pyplot as plt
import os



archivo = f'RMSD.txt'
RMSD_1 = []
RMSD_2 = []
RMSD_3 = []
Steps = []
with open(archivo, 'r') as f:
    for x, linea in enumerate(f):
        if (x < 1010):
            columna1, columna2 = linea.split()  
            Steps.append(float(columna1))
            RMSD_1.append(float(columna2))
                
        if (1010 < x < 2021):
            columna1, columna2 = linea.split()
            RMSD_2.append(float(columna2))
                
        if (2021 < x):
            columna1, columna2 = linea.split()
            RMSD_3.append(float(columna2))
            
    fig, ax = plt.subplots()
    ax.plot(Steps, RMSD_1, label = '1237K')
    ax.plot(Steps, RMSD_2, label = '1337K')
    ax.plot(Steps, RMSD_3, label = '1437K')
    plt.ylabel('RMSD [Å]')
    plt.xlabel('Steps')
    plt.title('RMSD')
    plt.grid(False)
    plt.legend(bbox_to_anchor=(0.97,0.15),loc='lower right')
    plt.tight_layout()
    Image_path = os.path.join(os.getcwd(), f'Plots/RMSD.png')
    plt.savefig(Image_path)


