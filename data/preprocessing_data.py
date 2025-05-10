import pandas as pd

def get_chart_metadata():
    return {
        "heatmap": {
            "title": "Frecuencia de uso de técnicas de preprocesamiento en los últimos años",
            "xlabel": "Año",
            "ylabel": "Técnica",
            "cmap": "Blues",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso de técnicas de preprocesamiento (2019–2024)",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
        },
        "bar": {
            "title": "Total acumulado de uso por técnica de preprocesamiento (2019–2024)",
            "xlabel": "Técnica",
            "ylabel": "Número total de publicaciones",
            "colors": ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011']
        },
        "bubble": {
            "title": "Proporción de uso de técnicas de preprocesamiento por cantidad de veces usadas",
            "xlabel": "Técnica",
            "ylabel": "Número total de publicaciones",
            "colors": ['#0000FF', '#0000CC', '#000099', '#000066', '#000044', '#000022', '#000011'],
            "scale": 100
        }
    }

def get_data():
    data = {
        2019: [1, 0, 0, 0, 3, 1, 2],
        2020: [2, 2, 0, 1, 4, 1, 3],
        2021: [3, 2, 0, 1, 3, 0, 0],
        2022: [1, 1, 0, 1, 2, 1, 1],
        2023: [0, 2, 1, 2, 6, 2, 1],
        2024: [1, 0, 2, 0, 9, 1, 4]
    }
    labels = [
        "Removal of background",
        "Noise removal",
        "Gaussian filtering",
        "median filters",
        "CLAHE",
        "Otsu’s thresholding method",
        "Pectoral muscle suppression"
    ]
    df = pd.DataFrame(data, index=labels)
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
