import pandas as pd

def get_chart_metadata():
    return {
        "heatmap": {
            "title": "Frecuencia de uso - Top 4 Públicos y Top 4 Privados",
            "xlabel": "Año",
            "ylabel": "Dataset",
            "cmap": "coolwarm",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia de uso - Top 4 Públicos y Privados",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones",
            "color_publico": "#0044CC",
            "color_privado": "#CC0000"
        },
        "bar": {
            "title": "Total de publicaciones - Top 8",
            "xlabel": "Dataset",
            "ylabel": "Total de publicaciones",
            "color_publico": "#0044CC",
            "color_privado": "#CC0000"
        },
        "bubble": {
            "title": "Proporción de publicaciones - Top 8 (Burbujas)",
            "xlabel": "Dataset",
            "ylabel": "Total publicaciones",
            "scale": 300,
            "colors": ['#0044CC', '#CC0000']
        },
        "pie": {
            "title": "Distribución Público vs Privado (Pie) - Top 8",
            "colors": ['#0044CC', '#CC0000']
        },
        "donut": {
            "title": "Distribución Público vs Privado (Donut) - Top 8",
            "colors": ['#0044CC', '#CC0000']
        },
        "stacked_bar": {
            "title": "Distribución Público y Privado Apilado por Año - Top 8",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones",
            "colors": ['#0044CC', '#CC0000']
        }
    }

def get_data():
    data = {
        2019: [6, 1, 1, 1, 4, 0, 0, 0],
        2020: [6, 0, 6, 0, 11, 1, 0, 0],
        2021: [7, 0, 3, 0, 9, 0, 1, 0],
        2022: [6, 0, 4, 0, 8, 0, 0, 0],
        2023: [10, 0, 4, 0, 12, 0, 2, 0],
        2024: [13, 0, 8, 0, 15, 0, 2, 0],
    }

    datasets = ["DDSM", "MIAS", "INBREAST", "WBC", "Otros", "NCI", "UPMC", "INCAN"]
    publicos = ["DDSM", "MIAS", "INBREAST", "WBC"]

    df = pd.DataFrame(data, index=datasets)
    df["Tipo"] = ["Público" if d in publicos else "Privado" for d in datasets]

    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
