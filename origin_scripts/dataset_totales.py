import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
import os

# ==========================
# 📂 CREAR CARPETA DE SALIDA
# ==========================
output_folder = "graficos_output/top8"
os.makedirs(output_folder, exist_ok=True)

# ==========================
# 📦 DATOS BASE
# ==========================
data = {
    2019: [6, 1, 1, 1, 4, 0, 0, 0],
    2020: [6, 0, 6, 0, 11, 1, 0, 0],
    2021: [7, 0, 3, 0, 9, 0, 1, 0],
    2022: [6, 0, 4, 0, 8, 0, 0, 0],
    2023: [10, 0, 4, 0, 12, 0, 2, 0],
    2024: [13, 0, 8, 0, 15, 0, 2, 0]
}

datasets = ["DDSM", "MIAS", "INBREAST", "WBC", "Otros", "NCI", "UPMC", "INCAN"]
publicos = ["DDSM", "MIAS", "INBREAST", "WBC"]
privados = ["Otros", "NCI", "UPMC", "INCAN"]

# ==========================
# 📊 DATAFRAME Y COLORES
# ==========================
df = pd.DataFrame(data, index=datasets)
df['Tipo'] = ['Público' if d in publicos else 'Privado' for d in datasets]

colores_publicos = '#0044CC'
colores_privados = '#CC0000'

# ==========================
# 🔥 1. HEATMAP
# ==========================
plt.figure(figsize=(12, 6))
sns.heatmap(df.drop('Tipo', axis=1), annot=True, fmt="d", cmap="coolwarm", linewidths=0.5)
plt.title("Frecuencia de uso - Top 4 Públicos y Top 4 Privados")
plt.xlabel("Año")
plt.ylabel("Dataset")
plt.tight_layout()
plt.savefig(f"{output_folder}/heatmap_top8.png")
plt.close()
print("✅ Gráfico guardado: heatmap_top8.png")

# ==========================
# 📈 2. LÍNEAS DE TENDENCIA (CON NOMBRES)
# ==========================
plt.figure(figsize=(14, 8))
df_temp = df.drop('Tipo', axis=1).T
for dataset in publicos:
    plt.plot(df_temp.index, df_temp[dataset], marker='o', label=dataset, color=colores_publicos)
for dataset in privados:
    plt.plot(df_temp.index, df_temp[dataset], marker='s', label=dataset, color=colores_privados)

plt.legend(title="Datasets", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.title("Tendencia de uso - Top 4 Públicos y Privados")
plt.xlabel("Año")
plt.ylabel("Número de publicaciones")
plt.tight_layout()
plt.savefig(f"{output_folder}/lineas_top8.png")
plt.close()
print("✅ Gráfico guardado: lineas_top8.png")

# ==========================
# 📊 3. BARRAS
# ==========================
totales = df.drop('Tipo', axis=1).sum(axis=1)
plt.figure(figsize=(12, 6))
colors = [colores_publicos if t == 'Público' else colores_privados for t in df['Tipo']]
bars = plt.bar(totales.index, totales.values, color=colors)
for i, v in enumerate(totales):
    plt.text(i, v + 1, str(int(v)), ha='center', fontsize=10)

plt.title("Total de publicaciones - Top 8")
plt.xticks(rotation=45)
plt.legend(handles=[
    Line2D([0], [0], color=colores_publicos, lw=4, label='Públicos'),
    Line2D([0], [0], color=colores_privados, lw=4, label='Privados')
])
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_top8.png")
plt.close()
print("✅ Gráfico guardado: barras_top8.png")

# ==========================
# 🟦 4. BURBUJAS (TAMAÑO GRANDE)
# ==========================
plt.figure(figsize=(14, 8))
tamanos = totales.values * 300  # BURBUJAS GRANDES
for i, dataset in enumerate(totales.index):
    color = colores_publicos if df.loc[dataset, 'Tipo'] == 'Público' else colores_privados
    plt.scatter(dataset, totales.iloc[i], s=tamanos[i], color=color, alpha=0.7)
    plt.text(dataset, totales.iloc[i], str(totales.iloc[i]), ha='center', va='center', color='white', fontsize=10)

plt.legend(handles=[
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colores_publicos, markersize=10, label='Públicos'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colores_privados, markersize=10, label='Privados')
])
plt.title("Proporción de publicaciones - Top 8 (Burbujas)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_folder}/burbujas_top8.png")
plt.close()
print("✅ Gráfico guardado: burbujas_top8.png")

# ==========================
# 🥧 5. PIE CHART
# ==========================
plt.figure(figsize=(8, 8))
publico_total = df[df['Tipo'] == 'Público'].drop('Tipo', axis=1).sum().sum()
privado_total = df[df['Tipo'] == 'Privado'].drop('Tipo', axis=1).sum().sum()
plt.pie([publico_total, privado_total], labels=['Públicos', 'Privados'], colors=[colores_publicos, colores_privados], autopct='%1.1f%%', startangle=90)
plt.title("Distribución Público vs Privado (Pie) - Top 8")
plt.tight_layout()
plt.savefig(f"{output_folder}/pie_top8.png")
plt.close()
print("✅ Gráfico guardado: pie_top8.png")

# ==========================
# 🍩 6. DONUT CHART
# ==========================
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie([publico_total, privado_total], labels=['Públicos', 'Privados'], colors=[colores_publicos, colores_privados], autopct='%1.1f%%', startangle=90, pctdistance=0.85)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.title("Distribución Público vs Privado (Donut) - Top 8")
plt.tight_layout()
plt.savefig(f"{output_folder}/donut_top8.png")
plt.close()
print("✅ Gráfico guardado: donut_top8.png")

# ==========================
# 📊 7. BARRAS APILADAS POR AÑO
# ==========================
df_apiladas = df.drop('Tipo', axis=1)
df_apiladas['Tipo'] = df['Tipo']
publicos_sum = df_apiladas[df_apiladas['Tipo'] == 'Público'].drop('Tipo', axis=1).sum()
privados_sum = df_apiladas[df_apiladas['Tipo'] == 'Privado'].drop('Tipo', axis=1).sum()

df_stacked = pd.DataFrame({
    'Públicos': publicos_sum,
    'Privados': privados_sum
})

plt.figure(figsize=(12, 6))
df_stacked.plot(kind='bar', stacked=True, color=[colores_publicos, colores_privados], ax=plt.gca())
plt.title("Distribución Público y Privado Apilado por Año - Top 8")
plt.xlabel("Año")
plt.ylabel("Número de publicaciones")
plt.xticks(rotation=45)
plt.legend(title='Tipo')
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_apiladas_top8.png")
plt.close()
print("✅ Gráfico guardado: barras_apiladas_top8.png")
