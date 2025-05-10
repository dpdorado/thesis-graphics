# data/publications_data.py
import pandas as pd

def get_chart_metadata():
    return {
        "heatmap": {
            "title": "Frecuencia de uso de datasets (Públicos vs Privados)",
            "xlabel": "Año",
            "ylabel": "Dataset",
            "cmap": "coolwarm",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso de datasets públicos vs privados",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones"
        },
        "bar": {
            "title": "Total acumulado de publicaciones por dataset",
            "xlabel": "Dataset",
            "ylabel": "Total de publicaciones"
        },
        "bubble": {
            "title": "Proporción total de uso de datasets (burbujas grandes)",
            "xlabel": "Dataset",
            "ylabel": "Total publicaciones",
            "scale": 300
        },
        "pie": {
            "title": "Distribución General Público vs Privado (Pie)"
        },
        "donut": {
            "title": "Distribución General Público vs Privado (Donut)"
        },
        "stacked_bar": {
            "title": "Distribución Público y Privado Apilado por Año",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones",
            "colors": ['#0044CC', '#CC0000']
        }
    }

def get_data():
    data = {
        2019: [6, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        2020: [6, 0, 6, 0, 11, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        2021: [7, 0, 3, 0, 9, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5],
        2022: [6, 0, 4, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2],
        2023: [10, 0, 4, 0, 12, 0, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2024: [13, 0, 8, 0, 15, 0, 2, 0, 2, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 4],
    }

    datasets = [
        "MIAS", "MMSD", "INBREAST", "Hologic", "DDSM", "BCBR-01", "WBC", "UCI", "CMMD",
        "NKI", "CDD-CESM", "BCDR", "TCIA", "BUSI", "Vindr-Mammo", "RIDER", "UPMC", "NCI",
        "INCAN", "LAPIMO EESC/USP", "Otros"
    ]

    publicos = [
        "MIAS", "MMSD", "INBREAST", "Hologic", "DDSM", "BCBR-01", "WBC", "UCI",
        "CMMD", "NKI", "CDD-CESM", "BCDR", "TCIA", "BUSI", "Vindr-Mammo", "RIDER"
    ]

    df = pd.DataFrame(data, index=datasets)
    df["Tipo"] = ["Público" if d in publicos else "Privado" for d in datasets]
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
