import pandas as pd

def get_chart_metadata():
    return {
        "bubble": {
            "title": "Publicaciones por año",
            "xlabel": "Año",
            "ylabel": "Número de publicaciones",
            "colors": ['#0000AA', '#0000FF', '#0000CC', '#000099', '#000066', '#000033'],
            "scale": 100
        }
    }

def get_data():
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    publications = [11, 13, 18, 13, 22, 27]
    df = pd.DataFrame({'Año': years, 'Publicaciones': publications})
    return {
        "df": df,
        "metadata": get_chart_metadata()
    }
