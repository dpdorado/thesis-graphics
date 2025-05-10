import pandas as pd

def get_chart_metadata():
    colors = ['#0000FF', '#0000CC', '#000099']
    return {
        "heatmap": {
            "title": "Frecuencia de tipos de clasificación en los últimos años",
            "xlabel": "Año",
            "ylabel": "Tipo",
            "cmap": "Blues", "annot": True, "fmt": "d", "linewidths": 0.5, "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso por tipo de clasificación (2019–2024)",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": colors
        },
        "bar": {
            "title": "Total acumulado por tipo de clasificación (2019–2024)",
            "xlabel": "Tipo",
            "ylabel": "Número total de publicaciones",
            "colors": colors
        },
        "bubble": {
            "title": "Proporción del uso por tipo de clasificación",
            "xlabel": "Tipo",
            "ylabel": "Número total de publicaciones",
            "colors": colors,
            "scale": 100
        }
    }

def get_data():
    data = {
        2019: [8, 0, 3],
        2020: [11, 0, 2],
        2021: [14, 1, 3],
        2022: [9, 4, 0],
        2023: [17, 3, 2],
        2024: [19, 3, 5]
    }
    labels = [
        "Clasificación binaria (Benigno/Maligno)",
        "Normal/Benigno/Maligno",
        "Varias formas"
    ]
    df = pd.DataFrame(data, index=labels)
    return { "df": df, "metadata": get_chart_metadata() }
