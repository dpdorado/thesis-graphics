import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D

# ==========================
# 📦 DATOS BASE
# ==========================

# 1. Técnicas de extracción de características
data_extraccion = {
    2019: [2, 1, 0, 0, 1, 1, 3],
    2020: [1, 0, 1, 0, 0, 0, 5],
    2021: [3, 2, 0, 0, 0, 0, 6],
    2022: [6, 0, 1, 1, 1, 0, 2],
    2023: [1, 0, 1, 0, 1, 0, 7],
    2024: [1, 1, 1, 2, 1, 2, 10]
}
extraccion = ["GLCM", "GLRLM", "DCT", "DWT", "U-Net", "VGG", "Arquitectura"]
df1 = pd.DataFrame(data_extraccion, index=extraccion)

# 2. Métricas más usadas
data_metricas = {
    2019: [6, 10, 9, 9, 2, 2, 0],
    2020: [8, 11, 7, 6, 2, 2, 1],
    2021: [8, 12, 10, 8, 5, 4, 1],
    2022: [3, 11, 9, 8, 5, 5, 1],
    2023: [9, 21, 15, 12, 10, 11, 2],
    2024: [13, 21, 16, 12, 17, 9, 3]
}
metricas = ["AUC", "Accuracy", "Sensitivity", "Specificity", "PPV", "F1 Score", "MCC"]
df2 = pd.DataFrame(data_metricas, index=metricas)

# 3. Tipo de clasificación
data_clasificacion = {
    2019: [8, 0, 3],
    2020: [11, 0, 2],
    2021: [14, 1, 3],
    2022: [9, 4, 0],
    2023: [17, 3, 2],
    2024: [19, 3, 5]
}
clasificacion = [
    "Clasificación binaria (Benigno/Maligno)",
    "Normal/Benigno/Maligno",
    "Varias formas"
]
df3 = pd.DataFrame(data_clasificacion, index=clasificacion)

# ==========================
# 🔁 FUNCIÓN PARA GRAFICAR
# ==========================

def generar_graficos(df, titulo_base, nombre_archivo_base):
    colores = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
    totales = df.sum(axis=1).sort_values(ascending=False)

    # Heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df, annot=True, fmt="d", cmap="Blues", linewidths=0.5, linecolor='white')
    plt.title(f"Frecuencia de uso de {titulo_base} en los últimos años")
    plt.xlabel("Año")
    plt.ylabel(titulo_base.capitalize())
    plt.tight_layout()
    plt.savefig(f"heatmap_{nombre_archivo_base}.png")

    # Gráfico de líneas
    df.T.plot(figsize=(10, 6), marker='o', color=colores[:len(df)])
    plt.title(f"Tendencia del uso de {titulo_base} (2019–2024)")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de publicaciones")
    plt.legend(title=titulo_base.capitalize(), bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f"lineas_{nombre_archivo_base}.png")

    # Barras con etiquetas
    plt.figure(figsize=(10, 6))
    bars = plt.bar(totales.index, totales.values, color=colores[:len(totales)])
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
                 str(int(height)), ha='center', va='bottom', color='black', fontsize=11)
    plt.title(f"Total acumulado de uso por {titulo_base} (2019–2024)")
    plt.xlabel(titulo_base.capitalize())
    plt.ylabel("Número total de publicaciones")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"barras_totales_{nombre_archivo_base}.png")

    # Burbujas
    categorias_ordenadas = totales.index.tolist()[::-1]
    valores = totales.values.tolist()[::-1]
    tamanos = [v * 100 for v in valores]
    fig, ax = plt.subplots(figsize=(10, 6))
    scatter = ax.scatter(categorias_ordenadas, valores, s=tamanos,
                         c=colores[:len(valores)], alpha=0.9)

    for i in range(len(categorias_ordenadas)):
        ax.text(categorias_ordenadas[i], valores[i], str(valores[i]),
                ha='center', va='center', color='white', fontsize=12)

    ax.set_title(f"Proporción de uso de {titulo_base} por cantidad de veces usadas")
    ax.set_xlabel(titulo_base.capitalize())
    ax.set_ylabel("Número total de publicaciones")

    leyenda = [Line2D([0], [0], marker='o', color='w', label=categorias_ordenadas[i],
                      markerfacecolor=colores[i], markersize=10)
               for i in range(len(categorias_ordenadas))]
    ax.legend(handles=leyenda, title=titulo_base.capitalize(), bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f"burbujas_totales_{nombre_archivo_base}.png")

# ==========================
# 🚀 GENERAR TODOS LOS GRÁFICOS
# ==========================
generar_graficos(df1, "técnicas de extracción de características", "extraccion_caracteristicas")
generar_graficos(df2, "métricas", "metricas")
generar_graficos(df3, "tipos de clasificación", "tipos_clasificacion")
