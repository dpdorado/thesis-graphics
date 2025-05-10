import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D

# ==========================
# 📦 DATOS BASE (Arquitecturas)
# ==========================
data = {
    2019: [1, 5, 0, 0, 2, 0, 2],
    2020: [3, 3, 0, 2, 1, 0, 3],
    2021: [2, 3, 1, 2, 0, 0, 7],
    2022: [0, 2, 0, 0, 0, 0, 7],
    2023: [1, 4, 2, 0, 1, 1, 11],
    2024: [2, 6, 1, 1, 0, 4, 9]
}

arquitecturas = [
    "SVM",
    "Custom CNN",
    "R-CNN",
    "U-Net",
    "AlexNet",
    "Transformer",
    "Otros"
]

df = pd.DataFrame(data, index=arquitecturas)

# ==========================
# 🔥 HEATMAP
# ==========================
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt="d", cmap="Blues", linewidths=0.5, linecolor='white')
plt.title("Frecuencia de uso de las arquitecturas en los últimos años")
plt.xlabel("Año")
plt.ylabel("Arquitectura")
plt.tight_layout()
plt.savefig("heatmap_arquitecturas_azul.png")
print("✅ Gráfico guardado como heatmap_arquitecturas_azul.png")

# ==========================
# 📈 LÍNEAS TEMPORALES CON COLORES FUERTES
# ==========================
colores_lineas = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
df.T.plot(figsize=(10, 6), marker='o', color=colores_lineas)
plt.title("Tendencia del uso de arquitecturas entre 2019 y 2024")
plt.xlabel("Año")
plt.ylabel("Cantidad de publicaciones")
plt.legend(title="Arquitectura", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("lineas_arquitecturas_colores_final.png")
print("✅ Gráfico guardado como lineas_arquitecturas_colores_final.png")

# ==========================
# 📊 BARRAS POR ARQUITECTURA CON COLORES DIFERENTES + ETIQUETAS
# ==========================
totales = df.sum(axis=1).sort_values(ascending=False)
colores_barras = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']

plt.figure(figsize=(10, 6))
bars = plt.bar(totales.index, totales.values, color=colores_barras[:len(totales)])

# Agregar etiquetas sobre las barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
             str(int(height)),
             ha='center', va='bottom', color='black', fontsize=11)

plt.title("Total acumulado de uso por arquitectura (2019–2024)")
plt.xlabel("Arquitectura")
plt.ylabel("Número total de publicaciones")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("barras_totales_arquitecturas.png")
print("✅ Gráfico guardado como barras_totales_arquitecturas.png")

# ==========================
# 🟦 GRÁFICO DE BURBUJAS POR ARQUITECTURA (USO TOTAL, MÁS USADA AL FINAL)
# ==========================
datasets_ordenados = totales.index.tolist()[::-1]
valores = totales.values.tolist()[::-1]
tamanos = [v * 100 for v in valores]
colores_burbujas = colores_barras[:len(valores)]

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(datasets_ordenados, valores, s=tamanos, c=colores_burbujas, alpha=0.9)

# Etiquetas dentro de las burbujas
for i in range(len(datasets_ordenados)):
    ax.text(datasets_ordenados[i], valores[i], str(valores[i]),
            ha='center', va='center', color='white', fontsize=12)

# Títulos y ejes
ax.set_title("Proporción de uso de las arquitecturas por cantidad de veces usadas")
ax.set_xlabel("Arquitectura")
ax.set_ylabel("Número total de publicaciones")

# Leyenda personalizada
leyenda = [Line2D([0], [0], marker='o', color='w', label=datasets_ordenados[i],
                  markerfacecolor=colores_burbujas[i], markersize=10)
           for i in range(len(datasets_ordenados))]
ax.legend(handles=leyenda, title='Arquitectura', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig("burbujas_totales_arquitecturas.png")
print("✅ Gráfico guardado como burbujas_totales_arquitecturas.png")
