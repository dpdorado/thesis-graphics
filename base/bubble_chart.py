from base.base_chart import BaseChart
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

class BubbleChart(BaseChart):
    def __init__(self, df, title, filename, config):
        super().__init__(df, title, filename)
        self.config = config

    def generate(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        scale = self.config.get("scale", 100)
        color_pub = self.config.get("color_publico", "#0044CC")
        color_priv = self.config.get("color_privado", "#CC0000")

        if self.df.shape[1] == 2 and "Tipo" in self.df.columns:
            # Tabla plana con columna "Tipo"
            x = self.df.columns[0]
            y = self.df.columns[1]
            data = self.df[[x, y, "Tipo"]]
            sizes = data[y] * scale
            scatter_colors = [color_pub if t == "Público" else color_priv for t in data["Tipo"]]

            ax.scatter(data[x], data[y], s=sizes, c=scatter_colors, alpha=0.9)
            for i in range(len(data)):
                ax.text(data[x].iloc[i], data[y].iloc[i], str(data[y].iloc[i]),
                        ha='center', va='center', color='white', fontsize=12)

            ax.legend(handles=[
                Line2D([0], [0], marker='o', color='w', label='Públicos',
                       markerfacecolor=color_pub, markersize=10),
                Line2D([0], [0], marker='o', color='w', label='Privados',
                       markerfacecolor=color_priv, markersize=10)
            ])
        else:
            # Matriz pivot
            df_numeric = self.df.drop("Tipo", axis=1) if "Tipo" in self.df.columns else self.df
            totals = df_numeric.sum(axis=1).sort_values(ascending=True)
            sizes = totals * scale

            if "Tipo" in self.df.columns:
                scatter_colors = [
                    color_pub if self.df.loc[idx, "Tipo"] == "Público" else color_priv
                    for idx in totals.index
                ]
            else:
                scatter_colors = None

            ax.scatter(totals.index, totals.values, s=sizes, c=scatter_colors, alpha=0.9)
            for i, name in enumerate(totals.index):
                ax.text(name, totals.iloc[i], str(totals.iloc[i]),
                        ha='center', va='center', color='white', fontsize=12)

            if "Tipo" in self.df.columns:
                ax.legend(handles=[
                    Line2D([0], [0], marker='o', color='w', label='Públicos',
                           markerfacecolor=color_pub, markersize=10),
                    Line2D([0], [0], marker='o', color='w', label='Privados',
                           markerfacecolor=color_priv, markersize=10)
                ])

        ax.set_title(self.config.get("title", self.title))
        ax.set_xlabel(self.config.get("xlabel", ""))
        ax.set_ylabel(self.config.get("ylabel", ""))
        self.save(fig, "bubble")
