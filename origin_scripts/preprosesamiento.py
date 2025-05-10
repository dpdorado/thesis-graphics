import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D

# ==========================
# 📦 DATOS BASE (Técnicas de preprocesamiento)
# ==========================
data = {
    2019: [1, 0, 0, 0, 3, 1, 2],
    2020: [2, 2, 0, 1, 4, 1, 3],
    2021: [3, 2, 0, 1, 3, 0, 0],
    2022: [1, 1, 0, 1, 2, 1, 1],
    2023: [0, 2, 1, 2, 6, 2, 1],
    2024: [1, 0, 2, 0, 9, 1, 4]
}

tecnicas = [
    "Removal of background",
    "Noise removal",
    "Gaussian filtering",
    "median filters",
    "CLAHE",
    "Otsu’s thresholding method",
    "Pectoral muscle suppression"
]

df = pd.DataFrame(data, index=tecnicas)

# ==========================
# 🔥 HEATMAP
# ==========================
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt="d", cmap="Blues", linewidths=0.5, linecolor='white')
plt.title("Frecuencia de uso de técnicas de preprocesamiento en los últimos años")
plt.xlabel("Año")
plt.ylabel("Técnica")
plt.tight_layout()
plt.savefig("heatmap_preprocesamiento.png")

# ==========================
# 📈 LÍNEAS TEMPORALES
# ==========================
colores_lineas = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
df.T.plot(figsize=(10, 6), marker='o', color=colores_lineas)
plt.title("Tendencia del uso de técnicas de preprocesamiento (2019–2024)")
plt.xlabel("Año")
plt.ylabel("Cantidad de publicaciones")
plt.legend(title="Técnica", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("lineas_preprocesamiento.png")

# ==========================
# 📊 BARRAS CON ETIQUETAS
# ==========================
totales = df.sum(axis=1).sort_values(ascending=False)
colores_barras = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']

plt.figure(figsize=(10, 6))
bars = plt.bar(totales.index, totales.values, color=colores_barras[:len(totales)])
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, str(int(height)),
             ha='center', va='bottom', color='black', fontsize=11)

plt.title("Total acumulado de uso por técnica de preprocesamiento (2019–2024)")
plt.xlabel("Técnica")
plt.ylabel("Número total de publicaciones")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("barras_totales_preprocesamiento.png")

# ==========================
# 🟦 GRÁFICO DE BURBUJAS
# ==========================
tecnicas_ordenadas = totales.index.tolist()[::-1]
valores = totales.values.tolist()[::-1]
tamanos = [v * 100 for v in valores]
colores_burbujas = colores_barras[:len(valores)]

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(tecnicas_ordenadas, valores, s=tamanos, c=colores_burbujas, alpha=0.9)

for i in range(len(tecnicas_ordenadas)):
    ax.text(tecnicas_ordenadas[i], valores[i], str(valores[i]),
            ha='center', va='center', color='white', fontsize=12)

ax.set_title("Proporción de uso de técnicas de preprocesamiento por cantidad de veces usadas")
ax.set_xlabel("Técnica")
ax.set_ylabel("Número total de publicaciones")

leyenda = [Line2D([0], [0], marker='o', color='w', label=tecnicas_ordenadas[i],
                  markerfacecolor=colores_burbujas[i], markersize=10)
           for i in range(len(tecnicas_ordenadas))]
ax.legend(handles=leyenda, title='Técnica', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig("burbujas_totales_preprocesamiento.png")
print("✅ Todos los gráficos generados correctamente.")
