from base.base_chart import BaseChart
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

class BarChart(BaseChart):
    def __init__(self, df, title, filename, config):
        super().__init__(df, title, filename)
        self.config = config

    def generate(self):
        df_numeric = self.df.drop('Tipo', axis=1) if 'Tipo' in self.df.columns else self.df
        totals = df_numeric.sum(axis=1).sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(10, 6))

        if 'Tipo' in self.df.columns:
            tipo_series = self.df.loc[totals.index, 'Tipo']
            colores_publico = self.config.get("color_publico", '#0044CC')
            colores_privado = self.config.get("color_privado", '#CC0000')
            colors = [colores_publico if tipo == 'Público' else colores_privado for tipo in tipo_series]
        else:
            colors = self.config.get("colors", None)
            if colors and len(colors) < len(totals):
                colors = colors * (len(totals) // len(colors) + 1)
            colors = colors[:len(totals)] if colors else None

        bars = ax.bar(totals.index, totals.values, color=colors)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 0.5, str(int(height)),
                    ha='center', va='bottom', fontsize=11)

        ax.set_title(self.config.get("title", self.title))
        ax.set_xlabel(self.config.get("xlabel", ""))
        ax.set_ylabel(self.config.get("ylabel", ""))
        plt.xticks(rotation=45, ha='right')

        if 'Tipo' in self.df.columns:
            ax.legend(handles=[
                Line2D([0], [0], color=colores_publico, lw=4, label='Públicos'),
                Line2D([0], [0], color=colores_privado, lw=4, label='Privados')
            ])

        self.save(fig, "bar")
