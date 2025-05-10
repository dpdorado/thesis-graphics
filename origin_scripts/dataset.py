import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D
import os

# ==========================
# 📂 CREAR CARPETA DE SALIDA
# ==========================
output_folder = "graficos_output"
os.makedirs(output_folder, exist_ok=True)

# ==========================
# 📦 DATOS BASE
# ==========================
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
    "NKI", "CDD-CESM", "BCDR", "TCIA", "BUSI", "Vindr-Mammo", "RIDER", "UPMC", "NCI",
    "INCAN", "LAPIMO EESC/USP", "Otros"
]

publicos = ["MIAS", "MMSD", "INBREAST", "Hologic", "DDSM", "BCBR-01", "WBC", "UCI", "CMMD", "NKI", "CDD-CESM", "BCDR", "TCIA", "BUSI", "Vindr-Mammo", "RIDER"]
privados = ["UPMC", "NCI", "INCAN", "LAPIMO EESC/USP", "Otros"]

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
plt.figure(figsize=(14, 8))
sns.heatmap(df.drop('Tipo', axis=1).iloc[:, :-1], annot=True, fmt="d", cmap="coolwarm", linewidths=0.5)
plt.title("Frecuencia de uso de datasets (Públicos vs Privados)")
plt.xlabel("Año")
plt.ylabel("Dataset")
plt.tight_layout()
plt.savefig(f"{output_folder}/heatmap_publico_privado.png")
plt.close()
print("✅ Gráfico guardado: heatmap_publico_privado.png")

# ==========================
# 📈 2. TENDENCIA LINEAL GENERAL (CON NOMBRES)
# ==========================
plt.figure(figsize=(16, 10))
df_temp = df.drop('Tipo', axis=1).iloc[:, :-1].T
for dataset in publicos:
    plt.plot(df_temp.index, df_temp[dataset], marker='o', label=dataset, color=colores_publicos)
for dataset in privados:
    plt.plot(df_temp.index, df_temp[dataset], marker='s', label=dataset, color=colores_privados)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title="Datasets")
plt.grid(True, linestyle='--', alpha=0.5)
plt.title("Tendencia del uso de datasets públicos vs privados")
plt.xlabel("Año")
plt.ylabel("Número de publicaciones")
plt.tight_layout()
plt.savefig(f"{output_folder}/lineas_publico_privado_nombres.png")
plt.close()
print("✅ Gráfico guardado: lineas_publico_privado_nombres.png")

# ==========================
# 📊 3. BARRAS POR TIPO
# ==========================
totales = df.drop('Tipo', axis=1).sum(axis=1)
plt.figure(figsize=(14, 8))
colors = [colores_publicos if t == 'Público' else colores_privados for t in df['Tipo']]
bars = plt.bar(totales.index, totales.values, color=colors)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1, str(int(height)),
             ha='center', va='bottom', fontsize=10)
plt.title("Total acumulado de publicaciones por dataset")
plt.xticks(rotation=45, ha='right')
plt.legend(handles=[
    Line2D([0], [0], color=colores_publicos, lw=4, label='Públicos'),
    Line2D([0], [0], color=colores_privados, lw=4, label='Privados')
])
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_publico_privado.png")
plt.close()
print("✅ Gráfico guardado: barras_publico_privado.png")

# ==========================
# 🟦 4. BURBUJAS AGRUPADAS
# ==========================
plt.figure(figsize=(16, 10))
tamanos = totales.values * 300  # GRANDES
for i, dataset in enumerate(totales.index):
    color = colores_publicos if df.loc[dataset, 'Tipo'] == 'Público' else colores_privados
    plt.scatter(dataset, totales.iloc[i], s=tamanos[i], color=color, alpha=0.7)
    plt.text(dataset, totales.iloc[i], str(totales.iloc[i]), ha='center', va='center', color='white', fontsize=10)

plt.legend(handles=[
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colores_publicos, markersize=10, label='Públicos'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor=colores_privados, markersize=10, label='Privados')
])
plt.title("Proporción total de uso de datasets (burbujas grandes)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(f"{output_folder}/burbujas_publico_privado.png")
plt.close()
print("✅ Gráfico guardado: burbujas_publico_privado.png")

# ==========================
# 🥧 5. PIE CHART
# ==========================
plt.figure(figsize=(8, 8))
publico_total = df[df['Tipo'] == 'Público'].drop('Tipo', axis=1).sum().sum()
privado_total = df[df['Tipo'] == 'Privado'].drop('Tipo', axis=1).sum().sum()

plt.pie([publico_total, privado_total],
        labels=['Públicos', 'Privados'],
        colors=[colores_publicos, colores_privados],
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 12})
plt.title('Distribución General Público vs Privado (Pie)')
plt.tight_layout()
plt.savefig(f"{output_folder}/pie_publico_privado.png")
plt.close()
print("✅ Gráfico guardado: pie_publico_privado.png")

# ==========================
# 🍩 6. DONUT CHART
# ==========================
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie([publico_total, privado_total],
                                  labels=['Públicos', 'Privados'],
                                  colors=[colores_publicos, colores_privados],
                                  autopct='%1.1f%%',
                                  startangle=90,
                                  pctdistance=0.85,
                                  textprops={'fontsize': 12})
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('Distribución General Público vs Privado (Donut)')
plt.tight_layout()
plt.savefig(f"{output_folder}/donut_publico_privado.png")
plt.close()
print("✅ Gráfico guardado: donut_publico_privado.png")

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
plt.title('Distribución Público y Privado Apilado por Año')
plt.xlabel('Año')
plt.ylabel('Número de publicaciones')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Tipo')
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_apiladas_publico_privado.png")
plt.close()
print("✅ Gráfico guardado: barras_apiladas_publico_privado.png")
