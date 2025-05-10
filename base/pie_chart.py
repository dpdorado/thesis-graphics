from base.base_chart import BaseChart
import matplotlib.pyplot as plt

class PieChart(BaseChart):
    def __init__(self, df, title, filename, config):
        super().__init__(df, title, filename)
        self.config = config

    def generate(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        df_numeric = self.df.drop('Tipo', axis=1) if 'Tipo' in self.df.columns else self.df
        values = df_numeric.iloc[0].values if df_numeric.shape[0] == 1 else df_numeric.sum(axis=0).values
        labels = df_numeric.columns.tolist()
        colors = self.config.get("colors")

        ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct=self.config.get("autopct", '%1.1f%%'),
            startangle=self.config.get("startangle", 90),
            textprops=self.config.get("textprops", {'fontsize': 12})
        )

        ax.set_title(self.config.get("title", self.title))
        ax.set_ylabel("")  # Eliminar etiqueta por defecto
        self.save(fig, "pie")
