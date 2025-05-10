import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Datos
anios = [2019, 2020, 2021, 2022, 2023, 2024]
publicaciones = [11, 13, 18, 13, 22, 27]
tamanos = [i * 100 for i in publicaciones]  # Escalamos el tamaño de las burbujas

# Colores por año
colores = {
    2019: '#0000AA',  # Color añadido para 2019
    2020: '#0000FF',
    2021: '#0000CC',
    2022: '#000099',
    2023: '#000066',
    2024: '#000033'
}
color_lista = [colores[a] for a in anios]

# Crear gráfico
fig, ax = plt.subplots()
scatter = ax.scatter(anios, publicaciones, s=tamanos, c=color_lista, alpha=0.9)

# Añadir números dentro de las burbujas
for i in range(len(anios)):
    ax.text(anios[i], publicaciones[i], str(publicaciones[i]),
            ha='center', va='center', color='white', fontsize=12)

# Etiquetas
ax.set_title('Publicaciones por año')
ax.set_xlabel('Año')
ax.set_ylabel('Número de publicaciones')

# Leyenda personalizada
leyenda = [Line2D([0], [0], marker='o', color='w', label=str(a),
                  markerfacecolor=c, markersize=10)
           for a, c in colores.items()]
ax.legend(handles=leyenda, title='Año', loc='best')

# Ajuste y guardado
plt.tight_layout()
plt.savefig("publicaciones_por_anio.png")
print("✅ Gráfico guardado como publicaciones_por_anio.png")
