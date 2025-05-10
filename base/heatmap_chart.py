from base.base_chart import BaseChart
import matplotlib.pyplot as plt
import seaborn as sns

class HeatmapChart(BaseChart):
    def __init__(self, df, title, filename, config):
        super().__init__(df, title, filename)
        self.config = config

    def generate(self):
        df_filtered = self.df.drop('Tipo', axis=1) if 'Tipo' in self.df.columns else self.df
        fig = plt.figure(figsize=(10, 6))
        sns.heatmap(
            df_filtered,
            annot=self.config.get("annot", True),
            fmt=self.config.get("fmt", "d"),
            cmap=self.config.get("cmap", "Blues"),
            linewidths=self.config.get("linewidths", 0.5),
            linecolor=self.config.get("linecolor", "white")
        )
        plt.title(self.config.get("title", self.title))
        plt.xlabel(self.config.get("xlabel", ""))
        plt.ylabel(self.config.get("ylabel", ""))
        self.save(fig, "heatmap")

