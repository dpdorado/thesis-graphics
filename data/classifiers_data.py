import pandas as pd

def get_chart_metadata():
    colors = ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
    return {
        "heatmap": {
            "title": "Frecuencia de uso de modelos clasificadores en los últimos años",
            "xlabel": "Año",
            "ylabel": "Modelo clasificador",
            "cmap": "Blues",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso de modelos clasificadores (2019–2024)",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": colors
        },
        "bar": {
            "title": "Total acumulado de uso por modelo clasificador (2019–2024)",
            "xlabel": "Modelo clasificador",
            "ylabel": "Número total de publicaciones",
            "colors": colors
        },
        "bubble": {
            "title": "Proporción de uso de modelos clasificadores por cantidad de veces usados",
            "xlabel": "Modelo clasificador",
            "ylabel": "Número total de publicaciones",
            "colors": colors,
            "scale": 100
        }
    }

def get_data():
    data = {
        2019: [3, 1, 1, 2, 0, 1, 3],
        2020: [4, 1, 1, 1, 1, 2, 2],
        2021: [4, 1, 0, 0, 1, 0, 4],
        2022: [3, 0, 0, 0, 0, 0, 6],
        2023: [1, 0, 1, 0, 0, 0, 15],
        2024: [3, 1, 0, 0, 0, 2, 16]
    }
    labels = [
        "SVM",
        "Random forest (RF)",
        "Multi-layer perceptron (MLP)",
        "AlexNet",
        "ResNet",
        "U-Net",
        "Arquitectura"
    ]
    df = pd.DataFrame(data, index=labels)
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
