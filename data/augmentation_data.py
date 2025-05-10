import pandas as pd

def get_chart_metadata():
    base_colors = ['#0000FF', '#0000CC']
    return {
        "heatmap": {
            "title": "Frecuencia del aumento de datos en los últimos años",
            "xlabel": "Año",
            "ylabel": "Uso de aumento",
            "cmap": "Blues",
            "annot": True,
            "fmt": "d",
            "linewidths": 0.5,
            "linecolor": "white"
        },
        "line": {
            "title": "Tendencia del uso de aumento de datos (2019–2024)",
            "xlabel": "Año",
            "ylabel": "Cantidad de publicaciones",
            "colors": base_colors
        },
        "bar": {
            "title": "Total acumulado por uso de aumento (2019–2024)",
            "xlabel": "Uso de aumento",
            "ylabel": "Número total de publicaciones",
            "colors": base_colors
        },
        "bubble": {
            "title": "Proporción del uso por aumento de datos",
            "xlabel": "Uso de aumento",
            "ylabel": "Número total de publicaciones",
            "colors": base_colors,
            "scale": 200
        }
    }

def get_data():
    data = {
        2019: [5, 6],
        2020: [4, 9],
        2021: [5, 13],
        2022: [3, 10],
        2023: [10, 12],
        2024: [14, 13]
    }
    labels = ["SI", "NO"]
    df = pd.DataFrame(data, index=labels)
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
