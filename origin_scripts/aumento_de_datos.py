import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.lines import Line2D

# ==========================
# 📦 DATOS BASE
# ==========================

# Aumento de datos
data_aumento = {
    2019: [5, 6],
    2020: [4, 9],
    2021: [5, 13],
    2022: [3, 10],
    2023: [10, 12],
    2024: [14, 13]
}
df_aumento = pd.DataFrame(data_aumento, index=["SI", "NO"])

# Tipo de técnica
data_tecnica = {
    2019: [4, 1],
    2020: [4, 0],
    2021: [3, 2],
    2022: [1, 2],
    2023: [9, 1],
    2024: [11, 3]
}
df_tecnica = pd.DataFrame(data_tecnica, index=[
    "Transformaciones geométricas", "Automatizado"])

# ==========================
# 🔁 FUNCIÓN PARA GRAFICAR
# ==========================
def graficar_categorias(df, titulo_base, nombre_base):
    colores = ['#0000FF', '#0000CC']
    totales = df.sum(axis=1).sort_values(ascending=False)

    # HEATMAP
    plt.figure(figsize=(8, 5))
    sns.heatmap(df, annot=True, fmt="d", cmap="Blues", linewidths=0.5, linecolor='white')
    plt.title(f"Frecuencia del {titulo_base} en los últimos años")
    plt.xlabel("Año")
    plt.ylabel(titulo_base.capitalize())
    plt.tight_layout()
    plt.savefig(f"heatmap_{nombre_base}.png")

    # LÍNEAS
    df.T.plot(figsize=(8, 5), marker='o', color=colores[:len(df)])
    plt.title(f"Tendencia del {titulo_base} entre 2019 y 2024")
    plt.xlabel("Año")
    plt.ylabel("Cantidad de publicaciones")
    plt.legend(title=titulo_base.capitalize(), bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f"lineas_{nombre_base}.png")

    # BARRAS
    plt.figure(figsize=(8, 5))
    bars = plt.bar(totales.index, totales.values, color=colores[:len(totales)])
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.3, str(int(height)),
                 ha='center', va='bottom', color='black', fontsize=10)
    plt.title(f"Total acumulado por {titulo_base} (2019–2024)")
    plt.xlabel(titulo_base.capitalize())
    plt.ylabel("Número total de publicaciones")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"barras_totales_{nombre_base}.png")

    # BURBUJAS
    categorias_ordenadas = totales.index.tolist()[::-1]
    valores = totales.values.tolist()[::-1]
    tamanos = [v * 200 for v in valores]

    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(categorias_ordenadas, valores, s=tamanos, c=colores[:len(valores)], alpha=0.9)
    for i in range(len(categorias_ordenadas)):
        ax.text(categorias_ordenadas[i], valores[i], str(valores[i]),
                ha='center', va='center', color='white', fontsize=11)

    ax.set_title(f"Proporción del uso por {titulo_base}")
    ax.set_xlabel(titulo_base.capitalize())
    ax.set_ylabel("Número total de publicaciones")
    leyenda = [Line2D([0], [0], marker='o', color='w', label=categorias_ordenadas[i],
                      markerfacecolor=colores[i], markersize=10)
               for i in range(len(categorias_ordenadas))]
    ax.legend(handles=leyenda, title=titulo_base.capitalize(), bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(f"burbujas_totales_{nombre_base}.png")

# ==========================
# 🚀 GENERAR LOS 8 GRÁFICOS
# ==========================
graficar_categorias(df_aumento, "aumento de datos", "aumento_datos")
graficar_categorias(df_tecnica, "tipo de técnica de aumento de datos", "tipo_tecnica_aumento")
