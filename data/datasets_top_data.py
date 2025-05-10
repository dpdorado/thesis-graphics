import pandas as pd

def get_chart_metadata():
    return {
        "heatmap": {
            "title": "Frecuencia de uso de datasets (Top 4 Públicos y Privados)",
            "xlabel": "Año",
            "ylabel": "Dataset",
            "cmap": "coolwarm",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia de uso de datasets (Top 4 Públicos y Privados)",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones"
        },
        "bar": {
            "title": "Total de publicaciones (Top 4 Públicos y Privados)",
            "xlabel": "Dataset",
            "ylabel": "Total de publicaciones"
        },
        "bubble": {
            "title": "Proporción de uso (Burbujas grandes)",
            "xlabel": "Dataset",
            "ylabel": "Total publicaciones",
            "scale": 300
        },
        "pie": {
            "title": "Distribución Público vs Privado (Pie Chart)",
            "colors": ['#0044CC', '#CC0000']
        },
        "donut": {
            "title": "Distribución Público vs Privado (Donut)",
            "colors": ['#0044CC', '#CC0000']
        },
        "stacked_bar": {
            "title": "Distribución Público y Privado Apilado por Año (Top 4)",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones",
            "colors": ['#0044CC', '#CC0000']
        }
    }

def get_data():
    data = {
        2019: [4, 6, 1, 0, 1, 1, 0, 0],
        2020: [11, 6, 0, 0, 1, 1, 0, 0],
        2021: [9, 7, 0, 0, 0, 0, 1, 1],
        2022: [8, 6, 0, 0, 0, 0, 1, 2],
        2023: [12, 10, 0, 0, 0, 0, 0, 0],
        2024: [15, 13, 0, 2, 1, 1, 0, 4],
    }

    datasets = ["DDSM", "MIAS", "INBREAST", "WBC", "Otros", "NCI", "UPMC", "INCAN"]

    publicos = ["DDSM", "MIAS", "INBREAST", "WBC"]

    df = pd.DataFrame(data, index=datasets)
    df["Tipo"] = ["Público" if d in publicos else "Privado" for d in datasets]

    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
