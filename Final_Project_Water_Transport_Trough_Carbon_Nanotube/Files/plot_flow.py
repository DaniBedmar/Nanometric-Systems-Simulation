import os
import matplotlib.pyplot as plt
import numpy as np

# Directorio base donde se encuentran las carpetas
base_directory = "preasure"

# Obtener la lista de carpetas
carpetas = ["preasure01", "preasure02", "preasure03", "preasure04", "preasure05", "preasure06", "preasure08",
            "preasure10",  "preasure12", "preasure14", "preasure16"]

# Valores para el eje x
valores_x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6]

# Listas para almacenar los datos finales de los archivos flow.tcl
flow_data = []

# Leer los archivos flow.tcl de cada carpeta
for carpeta in carpetas:
    # Ruta completa de la carpeta
    carpeta_path = os.path.join(base_directory, carpeta)
    
    # Leer el archivo flow.tcl y obtener el último valor de la columna 2
    flow_file = os.path.join(carpeta_path, "flow.dat")
    with open(flow_file, "r") as file:
        lines = file.readlines()
        last_line = lines[-1]
        data_value = float(last_line.split()[1])  # Obtener el último valor de la columna 2 como un número decimal
        flow_data.append(data_value)

# Crear una nueva figura y ejes para el gráfico
fig, ax = plt.subplots()

# Generar el gráfico de los datos finales de flow.tcl
x = np.arange(len(carpetas))
ax.bar(x, flow_data)

# Personalizar el gráfico
ax.set_xticks(x)
ax.set_xticklabels(valores_x, rotation=90)
ax.set_xlabel("Força aplicada [Kcal/mol Å]")
ax.set_ylabel("Flux d'aigua")
ax.set_title("Flux d'aigua en funció de la pressió")

# Guardar el gráfico
fig.savefig("flow_plot.png")

# Mostrar el gráfico
plt.show()
