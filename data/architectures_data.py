import pandas as pd

def get_chart_metadata():
    return {
        "heatmap": {
            "title": "Frecuencia de uso de las arquitecturas en los últimos años",
            "xlabel": "Año",
            "ylabel": "Arquitectura",
            "cmap": "Blues",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso de arquitecturas entre 2019 y 2024",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
        },
        "bar": {
            "title": "Total acumulado de uso por arquitectura (2019–2024)",
            "xlabel": "Arquitectura",
            "ylabel": "Número total de publicaciones",
            "colors": ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
        },
        "bubble": {
            "title": "Proporción de uso de las arquitecturas por cantidad de veces usadas",
            "xlabel": "Arquitectura",
            "ylabel": "Número total de publicaciones",
            "colors": ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011'],
            "scale": 100
        }
    }

def get_data():
    data = {
        2019: [1, 5, 0, 0, 2, 0, 2],
        2020: [3, 3, 0, 2, 1, 0, 3],
        2021: [2, 3, 1, 2, 0, 0, 7],
        2022: [0, 2, 0, 0, 0, 0, 7],
        2023: [1, 4, 2, 0, 1, 1, 11],
        2024: [2, 6, 1, 1, 0, 4, 9]
    }
    labels = ["SVM", "Custom CNN", "R-CNN", "U-Net", "AlexNet", "Transformer", "Otros"]
    df = pd.DataFrame(data, index=labels)
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }

