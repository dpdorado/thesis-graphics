import pandas as pd

def get_chart_metadata():
    colors = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
    return {
        "heatmap": {
            "title": "Frecuencia de uso de métricas en los últimos años",
            "xlabel": "Año",
            "ylabel": "Métrica",
            "cmap": "Blues", "annot": True, "fmt": "d", "linewidths": 0.5, "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso de métricas (2019–2024)",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": colors
        },
        "bar": {
            "title": "Total acumulado de uso por métrica (2019–2024)",
            "xlabel": "Métrica",
            "ylabel": "Número total de publicaciones",
            "colors": colors
        },
        "bubble": {
            "title": "Proporción de uso de métricas",
            "xlabel": "Métrica",
            "ylabel": "Número total de publicaciones",
            "colors": colors,
            "scale": 100
        }
    }

def get_data():
    data = {
        2019: [6, 10, 9, 9, 2, 2, 0],
        2020: [8, 11, 7, 6, 2, 2, 1],
        2021: [8, 12, 10, 8, 5, 4, 1],
        2022: [3, 11, 9, 8, 5, 5, 1],
        2023: [9, 21, 15, 12, 10, 11, 2],
        2024: [13, 21, 16, 12, 17, 9, 3]
    }
    labels = ["AUC", "Accuracy", "Sensitivity", "Specificity", "PPV", "F1 Score", "MCC"]
    df = pd.DataFrame(data, index=labels)
    return { "df": df, "metadata": get_chart_metadata() }
