import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
import os

# 📂 CREAR CARPETA DE SALIDA
output_folder = "graficos_output/comparacion"
os.makedirs(output_folder, exist_ok=True)

# 📦 DATOS BASE
data = {
    2019: [6, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    2020: [6, 0, 6, 0, 11, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    2021: [7, 0, 3, 0, 9, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5],
    2022: [6, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2],
    2023: [10, 0, 4, 0, 12, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    2024: [13, 0, 8, 0, 15, 0, 2, 0, 2, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 4],
}

datasets = [
    "MIAS", "MMSD", "INBREAST", "Hologic", "DDSM", "BCBR-01", "WBC", "UCI", "CMMD",
    "NKI", "CDD-CESM", "BCDR", "TCIA", "BUSI", "Vindr-Mammo", "RIDER",
    "UPMC", "NCI", "INCAN", "LAPIMO EESC/USP", "Otros"
]

publicos_total = ["MIAS", "MMSD", "INBREAST", "Hologic", "DDSM", "BCBR-01", "WBC", "UCI", "CMMD", "NKI", "CDD-CESM", "BCDR", "TCIA", "BUSI", "Vindr-Mammo", "RIDER"]
privados_total = ["UPMC", "NCI", "INCAN", "LAPIMO EESC/USP", "Otros"]

# 📊 CREAR DATAFRAME
df = pd.DataFrame(data, index=datasets)
df['Tipo'] = ['Público' if d in publicos_total else 'Privado' for d in datasets]

# ✅ Filtrar SOLO top 4 públicos y privados
publicos = ["DDSM", "MIAS", "INBREAST", "WBC"]
privados = ["Otros", "NCI", "UPMC", "INCAN"]
datasets_filtrados = publicos + privados
df = df.loc[datasets_filtrados]

# 🎨 Colores
colores_publicos = '#0044CC'
colores_privados = '#CC0000'

# 🔥 HEATMAP
plt.figure(figsize=(12, 6))
sns.heatmap(df.drop('Tipo', axis=1), annot=True, fmt="d", cmap="coolwarm", linewidths=0.5)
plt.title("Frecuencia de uso de datasets (Top 4 Públicos y Privados)")
plt.xlabel("Año")
plt.ylabel("Dataset")
plt.tight_layout()
plt.savefig(f"{output_folder}/heatmap_top4.png")
plt.close()

# 📈 LÍNEAS DE TENDENCIA
plt.figure(figsize=(14, 8))
df_temp = df.drop('Tipo', axis=1).T

for dataset in publicos:
    plt.plot(df_temp.index, df_temp[dataset], marker='o', label=dataset, color=colores_publicos, markersize=8)
for dataset in privados:
    plt.plot(df_temp.index, df_temp[dataset], marker='s', label=dataset, color=colores_privados, markersize=8)

plt.legend(title="Datasets", bbox_to_anchor=(1.02, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.title("Tendencia de uso de datasets (Top 4 Públicos y Privados)")
plt.xlabel("Año")
plt.ylabel("Número de publicaciones")
plt.tight_layout()
plt.savefig(f"{output_folder}/lineas_top4.png")
plt.close()

# 📊 BARRAS ACUMULADAS
plt.figure(figsize=(12, 6))
totales = df.drop('Tipo', axis=1).sum(axis=1)
colors = [colores_publicos if df.loc[dataset, 'Tipo'] == 'Público' else colores_privados for dataset in totales.index]
bars = plt.bar(totales.index, totales.values, color=colors)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(int(height)), ha='center', va='bottom', fontsize=10)

plt.title("Total de publicaciones (Top 4 Públicos y Privados)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_top4.png")
plt.close()

# 🟦 BURBUJAS GRANDES
plt.figure(figsize=(14, 8))
tamanos = totales.values * 300
for i, dataset in enumerate(totales.index):
    color = colores_publicos if df.loc[dataset, 'Tipo'] == 'Público' else colores_privados
    plt.scatter(dataset, totales.iloc[i], s=tamanos[i], color=color, alpha=0.7)
    plt.text(dataset, totales.iloc[i], str(totales.iloc[i]), ha='center', va='center', color='white', fontsize=10)

plt.legend(handles=[
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colores_publicos, markersize=10, label='Públicos'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colores_privados, markersize=10, label='Privados')
])
plt.title("Proporción de uso (Burbujas grandes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_folder}/burbujas_top4.png")
plt.close()

# 🥧 PIE CHART
plt.figure(figsize=(8, 8))
publico_total = df[df['Tipo'] == 'Público'].drop('Tipo', axis=1).sum().sum()
privado_total = df[df['Tipo'] == 'Privado'].drop('Tipo', axis=1).sum().sum()

plt.pie([publico_total, privado_total],
        labels=['Públicos', 'Privados'],
        colors=[colores_publicos, colores_privados],
        autopct='%1.1f%%', startangle=90)
plt.title("Distribución Público vs Privado (Pie Chart)")
plt.tight_layout()
plt.savefig(f"{output_folder}/pie_top4.png")
plt.close()

# 🍩 DONUT CHART
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie([publico_total, privado_total],
                                  labels=['Públicos', 'Privados'],
                                  colors=[colores_publicos, colores_privados],
                                  autopct='%1.1f%%', startangle=90, pctdistance=0.85)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.title("Distribución Público vs Privado (Donut)")
plt.tight_layout()
plt.savefig(f"{output_folder}/donut_top4.png")
plt.close()

# 📊 BARRAS APILADAS
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
plt.title("Distribución Público y Privado Apilado por Año (Top 4)")
plt.xlabel("Año")
plt.ylabel("Número de publicaciones")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_apiladas_top4.png")
plt.close()

print("✅ TODOS los gráficos generados exitosamente.")
