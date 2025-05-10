import pandas as pd

def get_chart_metadata():
    return {
        "heatmap": {
            "title": "Frecuencia de uso: Públicos vs Privados por Año",
            "xlabel": "Año",
            "ylabel": "Tipo",
            "cmap": "coolwarm",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia de uso de Públicos vs Privados",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones",
            "color_publico": "#0044CC",
            "color_privado": "#CC0000"
        },
        "bar": {
            "title": "Total acumulado Público vs Privado",
            "xlabel": "Tipo",
            "ylabel": "Total de publicaciones",
            "color_publico": "#0044CC",
            "color_privado": "#CC0000"
        },
        "bubble": {
            "title": "Proporción de uso (Burbujas)",
            "xlabel": "Tipo",
            "ylabel": "Total publicaciones",
            "scale": 300,
            "colors": ['#0044CC', '#CC0000']
        },
        "pie": {
            "title": "Distribución General Público vs Privado (Pie)",
            "colors": ['#0044CC', '#CC0000']
        },
        "donut": {
            "title": "Distribución General Público vs Privado (Donut)",
            "colors": ['#0044CC', '#CC0000']
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
        2019: [24, 3],
        2020: [26, 2],
        2021: [19, 6],
        2022: [18, 3],
        2023: [28, 0],
        2024: [38, 5]
    }

    df = pd.DataFrame(data, index=["Públicos", "Privados"]).T
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
