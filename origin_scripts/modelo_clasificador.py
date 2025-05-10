import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D

# ==========================
# 📦 DATOS BASE (Modelos clasificadores más usados)
# ==========================
data = {
    2019: [3, 1, 1, 2, 0, 1, 3],
    2020: [4, 1, 1, 1, 1, 2, 2],
    2021: [4, 1, 0, 0, 1, 0, 4],
    2022: [3, 0, 0, 0, 0, 0, 6],
    2023: [1, 0, 1, 0, 0, 0, 15],
    2024: [3, 1, 0, 0, 0, 2, 16]
}

modelos = [
    "SVM",
    "Random forest (RF)",
    "Multi-layer perceptron (MLP)",
    "AlexNet",
    "ResNet",
    "U-Net",
    "Arquitectura"
]

df = pd.DataFrame(data, index=modelos)

# ==========================
# 🔥 HEATMAP
# ==========================
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, fmt="d", cmap="Blues", linewidths=0.5, linecolor='white')
plt.title("Frecuencia de uso de modelos clasificadores en los últimos años")
plt.xlabel("Año")
plt.ylabel("Modelo clasificador")
plt.tight_layout()
plt.savefig("heatmap_modelos_clasificadores.png")

# ==========================
# 📈 LÍNEAS TEMPORALES
# ==========================
colores_lineas = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
df.T.plot(figsize=(10, 6), marker='o', color=colores_lineas)
plt.title("Tendencia del uso de modelos clasificadores (2019–2024)")
plt.xlabel("Año")
plt.ylabel("Cantidad de publicaciones")
plt.legend(title="Modelo", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("lineas_modelos_clasificadores.png")

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

plt.title("Total acumulado de uso por modelo clasificador (2019–2024)")
plt.xlabel("Modelo clasificador")
plt.ylabel("Número total de publicaciones")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("barras_totales_modelos_clasificadores.png")

# ==========================
# 🟦 GRÁFICO DE BURBUJAS
# ==========================
modelos_ordenados = totales.index.tolist()[::-1]
valores = totales.values.tolist()[::-1]
tamanos = [v * 100 for v in valores]
colores_burbujas = colores_barras[:len(valores)]

fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(modelos_ordenados, valores, s=tamanos, c=colores_burbujas, alpha=0.9)

for i in range(len(modelos_ordenados)):
    ax.text(modelos_ordenados[i], valores[i], str(valores[i]),
            ha='center', va='center', color='white', fontsize=12)

ax.set_title("Proporción de uso de modelos clasificadores por cantidad de veces usados")
ax.set_xlabel("Modelo clasificador")
ax.set_ylabel("Número total de publicaciones")

leyenda = [Line2D([0], [0], marker='o', color='w', label=modelos_ordenados[i],
                  markerfacecolor=colores_burbujas[i], markersize=10)
           for i in range(len(modelos_ordenados))]
ax.legend(handles=leyenda, title='Modelo', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.savefig("burbujas_totales_modelos_clasificadores.png")
print("✅ Gráficos de modelos clasificadores generados correctamente.")
