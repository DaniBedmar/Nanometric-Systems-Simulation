import os
import matplotlib.pyplot as plt
import numpy as np

# Directorio base donde se encuentran las carpetas
base_directory = "preasure"

# Obtener la lista de carpetas
carpetas = ["preasure01", "preasure02", "preasure03", "preasure04", "preasure05", "preasure06", "preasure08",
            "preasure10", "preasure12", "preasure14", "preasure16"]

# Etiquetas para la leyenda
leyenda_etiquetas = ['0.1 applied force', '0.2 applied force', '0.3 applied force', '0.4 applied force', '0.5 applied force',
                     '0.6 applied force', '0.8 applied force', '1.0 applied force', '1.2 applied force', '1.4 applied force',
                     '1.6 applied force']

# Listas para almacenar los datos de los archivos
flow_data = []
permeation_data = []

# Leer los archivos de cada carpeta
for carpeta in carpetas:
    # Ruta completa de la carpeta
    carpeta_path = os.path.join(base_directory, carpeta)
    
    # Leer el archivo flow.dat
    flow_file = os.path.join(carpeta_path, "flow.dat")
    flow_data.append(np.loadtxt(flow_file))
    
    # Leer el archivo permeation.dat
    permeation_file = os.path.join(carpeta_path, "permeation.dat")
    permeation_data.append(np.loadtxt(permeation_file))

# Crear una nueva figura y ejes para el gráfico de flow.dat
fig1, ax1 = plt.subplots()

# Generar el gráfico de flow.dat para cada archivo
for i, data in enumerate(flow_data):
    x = data[:, 0]
    y = data[:, 1]
    ax1.plot(x, y, label=leyenda_etiquetas[i])

# Personalizar el gráfico de flow.dat
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_title("Gráfico de flow.dat")
ax1.legend()

# Guardar el gráfico de flow.dat
fig1.savefig("flow_plot.png")

# Crear una nueva figura y ejes para el gráfico de permeation.dat
fig2, ax2 = plt.subplots()

# Generar el gráfico de permeation.dat para cada archivo
for i, data in enumerate(permeation_data):
    x = data[:, 0]
    y = data[:, 1]
    ax2.plot(x, y, label=leyenda_etiquetas[i])

# Personalizar el gráfico de permeation.dat
ax2.set_xlabel("tiempo [ps]")
ax2.set_ylabel("permeación de agua")
ax2.set_title("Evolución de la permeación en función de la fuerza aplicada")
ax2.legend()

# Guardar el gráfico de permeation.dat
fig2.savefig("permeation_plot.png")

# Mostrar los gráficos
plt.show()
