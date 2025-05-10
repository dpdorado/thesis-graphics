import pandas as pd

def get_chart_metadata():
    colors = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
    return {
        "heatmap": {
            "title": "Frecuencia de uso de técnicas de extracción de características en los últimos años",
            "xlabel": "Año",
            "ylabel": "Técnica",
            "cmap": "Blues", "annot": True, "fmt": "d", "linewidths": 0.5, "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso de técnicas de extracción de características (2019–2024)",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": colors
        },
        "bar": {
            "title": "Total acumulado por técnica de extracción (2019–2024)",
            "xlabel": "Técnica",
            "ylabel": "Número total de publicaciones",
            "colors": colors
        },
        "bubble": {
            "title": "Proporción de uso de técnicas de extracción por frecuencia",
            "xlabel": "Técnica",
            "ylabel": "Número total de publicaciones",
            "colors": colors,
            "scale": 100
        }
    }

def get_data():
    data = {
        2019: [2, 1, 0, 0, 1, 1, 3],
        2020: [1, 0, 1, 0, 0, 0, 5],
        2021: [3, 2, 0, 0, 0, 0, 6],
        2022: [6, 0, 1, 1, 1, 0, 2],
        2023: [1, 0, 1, 0, 1, 0, 7],
        2024: [1, 1, 1, 2, 1, 2, 10]
    }
    labels = ["GLCM", "GLRLM", "DCT", "DWT", "U-Net", "VGG", "Arquitectura"]
    df = pd.DataFrame(data, index=labels)
    return { "df": df, "metadata": get_chart_metadata() }
