import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
from matplotlib.lines import Line2D

# 📂 CREAR CARPETA DE SALIDA
output_folder = "graficos_output/publicos_priovbados"
os.makedirs(output_folder, exist_ok=True)

# 📦 DATOS BASE ORIGINAL
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

publicos = ["MIAS", "MMSD", "INBREAST", "Hologic", "DDSM", "BCBR-01", "WBC", "UCI",
            "CMMD", "NKI", "CDD-CESM", "BCDR", "TCIA", "BUSI", "Vindr-Mammo", "RIDER"]
privados = ["UPMC", "NCI", "INCAN", "LAPIMO EESC/USP", "Otros"]

# 📊 CREAR DATAFRAME COMPLETO
df = pd.DataFrame(data, index=datasets)

# 🎯 AGRUPAR
publicos_sum = df.loc[publicos].sum()
privados_sum = df.loc[privados].sum()

df_conjuntos = pd.DataFrame({
    'Públicos': publicos_sum,
    'Privados': privados_sum
})

colores = {'Públicos': '#0044CC', 'Privados': '#CC0000'}

# 🔥 1. HEATMAP
plt.figure(figsize=(8, 6))
sns.heatmap(df_conjuntos.T, annot=True, fmt="d", cmap="coolwarm", linewidths=0.5)
plt.title("Frecuencia de uso: Públicos vs Privados por Año")
plt.xlabel("Año")
plt.ylabel("Tipo")
plt.tight_layout()
plt.savefig(f"{output_folder}/heatmap_conjuntos.png")
plt.close()

# 📈 2. LÍNEAS DE TENDENCIA
plt.figure(figsize=(12, 6))
for conjunto in df_conjuntos.columns:
    plt.plot(df_conjuntos.index, df_conjuntos[conjunto], marker='o', label=conjunto, color=colores[conjunto], markersize=8)

plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.title("Tendencia de uso de Públicos vs Privados")
plt.xlabel("Año")
plt.ylabel("Número de publicaciones")
plt.tight_layout()
plt.savefig(f"{output_folder}/lineas_conjuntos.png")
plt.close()

# 📊 3. BARRAS ACUMULADAS
plt.figure(figsize=(8, 6))
totales = df_conjuntos.sum()
bars = plt.bar(totales.index, totales.values, color=[colores[k] for k in totales.index])
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 1, str(int(height)), ha='center', va='bottom', fontsize=10)

plt.title("Total acumulado Público vs Privado")
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_conjuntos.png")
plt.close()

# 🟦 4. BURBUJAS
plt.figure(figsize=(8, 6))
sizes = totales.values * 300
for i, conjunto in enumerate(totales.index):
    plt.scatter(conjunto, totales.iloc[i], s=sizes[i], color=colores[conjunto], alpha=0.7)
    plt.text(conjunto, totales.iloc[i], str(totales.iloc[i]), ha='center', va='center', color='white', fontsize=12)

plt.title("Proporción de uso (Burbujas)")
plt.tight_layout()
plt.savefig(f"{output_folder}/burbujas_conjuntos.png")
plt.close()

# 🥧 5. PIE CHART
plt.figure(figsize=(8, 8))
plt.pie(totales,
        labels=totales.index,
        colors=[colores[k] for k in totales.index],
        autopct='%1.1f%%',
        startangle=90)
plt.title('Distribución General Público vs Privado (Pie)')
plt.tight_layout()
plt.savefig(f"{output_folder}/pie_conjuntos.png")
plt.close()

# 🍩 6. DONUT CHART
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(totales,
                                  labels=totales.index,
                                  colors=[colores[k] for k in totales.index],
                                  autopct='%1.1f%%',
                                  startangle=90,
                                  pctdistance=0.85)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.title('Distribución General Público vs Privado (Donut)')
plt.tight_layout()
plt.savefig(f"{output_folder}/donut_conjuntos.png")
plt.close()

# 📊 7. BARRAS APILADAS POR AÑO
plt.figure(figsize=(12, 6))
df_conjuntos.plot(kind='bar', stacked=True, color=[colores['Públicos'], colores['Privados']], ax=plt.gca())
plt.title('Distribución Público y Privado Apilado por Año')
plt.xlabel('Año')
plt.ylabel('Número de publicaciones')
plt.xticks(rotation=45)
plt.legend(title='Tipo')
plt.tight_layout()
plt.savefig(f"{output_folder}/barras_apiladas_conjuntos.png")
plt.close()

print("✅ Tercer conjunto de gráficos generado: Públicos vs Privados ✅")
