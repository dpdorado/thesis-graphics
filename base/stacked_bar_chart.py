import matplotlib.pyplot as plt
import pandas as pd
import os

class StackedBarChart:
    def __init__(self, df, title, name, config):
        self.df = df
        self.title = title
        self.name = name
        self.config = config

    def generate(self):
        output_path = f"graficos_output/{self.name}/stacked_bar.png"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        colors = self.config.get("colors", ['#0044CC', '#CC0000'])

        df_transformed = self.df.copy()

        if 'Tipo' in df_transformed.columns:
            tipo_col = df_transformed.pop('Tipo')
            df_transformed['Tipo'] = tipo_col
            publicos_sum = df_transformed[df_transformed['Tipo'] == 'Público'].drop('Tipo', axis=1).sum()
            privados_sum = df_transformed[df_transformed['Tipo'] == 'Privado'].drop('Tipo', axis=1).sum()

            df_result = pd.DataFrame({
                'Públicos': publicos_sum,
                'Privados': privados_sum
            })
        else:
            # Caso donde el índice ya es 'Públicos' y 'Privados'
            df_result = df_transformed.T

        plt.figure(figsize=(12, 6))
        df_result.plot(kind='bar', stacked=True, color=colors, ax=plt.gca())
        plt.title(self.title)
        plt.xlabel(self.config.get("xlabel", ""))
        plt.ylabel(self.config.get("ylabel", ""))
        plt.xticks(rotation=45)
        plt.legend(title='Tipo')
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()
