from base.base_chart import BaseChart
import matplotlib.pyplot as plt

class LineChart(BaseChart):
    def __init__(self, df, title, filename, config):
        super().__init__(df, title, filename)
        self.config = config

    def generate(self):
        df_numeric = self.df.drop('Tipo', axis=1) if 'Tipo' in self.df.columns else self.df
        df_transposed = df_numeric.T
        fig, ax = plt.subplots(figsize=(10, 6))
        df_transposed.plot(marker='o', color=self.config.get("colors"), ax=ax)
        ax.set_title(self.config.get("title", self.title))
        ax.set_xlabel(self.config.get("xlabel", ""))
        ax.set_ylabel(self.config.get("ylabel", ""))
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(title=self.title, bbox_to_anchor=(1.05, 1), loc='upper left')
        self.save(fig, "line")

