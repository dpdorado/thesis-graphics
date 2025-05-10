import pandas as pd

def get_chart_metadata():
    base_colors = ['#0000FF', '#0000CC']
    return {
        "heatmap": {
            "title": "Frecuencia del tipo de técnica de aumento en los últimos años",
            "xlabel": "Año",
            "ylabel": "Técnica",
            "cmap": "Blues",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia de uso por tipo de técnica de aumento (2019–2024)",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": base_colors
        },
        "bar": {
            "title": "Total acumulado por tipo de técnica de aumento (2019–2024)",
            "xlabel": "Tipo de técnica",
            "ylabel": "Número total de publicaciones",
            "colors": base_colors
        },
        "bubble": {
            "title": "Proporción de uso por tipo de técnica de aumento",
            "xlabel": "Tipo de técnica",
            "ylabel": "Número total de publicaciones",
            "colors": base_colors,
            "scale": 200
        }
    }

def get_data():
    data = {
        2019: [4, 1],
        2020: [4, 0],
        2021: [3, 2],
        2022: [1, 2],
        2023: [9, 1],
        2024: [11, 3]
    }
    labels = ["Transformaciones geométricas", "Automatizado"]
    df = pd.DataFrame(data, index=labels)
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
