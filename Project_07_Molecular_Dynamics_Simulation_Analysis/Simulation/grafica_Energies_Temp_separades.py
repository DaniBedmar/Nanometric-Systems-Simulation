#Codi per crear gràfiques per cada una de les simulacions

import matplotlib.pyplot as plt
import os

l=["1237K","1337K","1437K"]

for i in l:
    archivo = f'{i}/Energies_Temp.txt'
    pasos_tiempo = []
    kinetic = []
    temp = []
    potential = []
    
    with open(archivo, 'r') as f:
        for x, linea in enumerate(f):
            if x < 6002:
                columna1, columna2 = linea.split()  
                pasos_tiempo.append(float(columna1))
                kinetic.append(float(columna2))
                
            if (6002 < x < 12005):
                columna1, columna2 = linea.split()
                temp.append(float(columna2))
                
            if (12005 < x < 18008):
                columna1, columna2 = linea.split()
                potential.append(float(columna2))  
        plt.figure(1)
        plt.plot(pasos_tiempo,kinetic, '-', label=f'{i}')
        plt.xlabel('Time')
        plt.ylabel('Kinetic Energy (kcal/mol)')
        plt.title('Kinetic Energy evolution ')
        plt.grid(False)
        plt.legend(bbox_to_anchor=(0.97,0.15),loc='lower right')
        Image_path = os.path.join(os.getcwd(), f'Plots/Kinetic{i}.png')
        plt.savefig(Image_path)
        plt.close()

        plt.figure(2)
        plt.plot(pasos_tiempo,temp, '-', label = f'{i}')
        plt.xlabel('Time')
        plt.ylabel('Temperature (K)')
        plt.title('Temperature evolution')
        plt.grid(False)
        plt.legend(bbox_to_anchor=(0.97,0.15),loc='lower right')
        Image_path = os.path.join(os.getcwd(), f'Plots/Temperature evolution at {i}.png')
        plt.savefig(Image_path)

        plt.figure(3)
        plt.plot(pasos_tiempo,potential, '-', label = f'{i}')
        plt.xlabel('Time')
        plt.ylabel('Potetial Energy (kcal/mol)')
        plt.title('Potential Energy evolution')
        plt.grid(False)
        plt.legend(bbox_to_anchor=(0.97,0.15),loc='lower right')
        Image_path = os.path.join(os.getcwd(), f'Plots/Potential{i}.png')
        plt.savefig(Image_path)



