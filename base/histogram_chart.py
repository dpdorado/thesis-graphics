# base/histogram_chart.py
from base.base_chart import BaseChart
import matplotlib.pyplot as plt

class HistogramChart(BaseChart):
    def generate(self):
        fig, ax = plt.subplots(figsize=(10, 6))
        self.df.hist(ax=ax)
        plt.suptitle(f"{self.title}")
        self.save(fig, "histogram")
