from base.heatmap_chart import HeatmapChart
from base.line_chart import LineChart
from base.bar_chart import BarChart
from base.bubble_chart import BubbleChart

class Category:
    def __init__(self, df, metadata, name = "Name", title = "Titles"):
        self.df = df
        self.metadata = metadata
        self.name = name
        self.title = title

    def generate_charts(self):
        HeatmapChart(self.df, self.title, self.name, self.metadata["heatmap"]).generate()
        LineChart(self.df, self.title, self.name, self.metadata["line"]).generate()
        BarChart(self.df, self.title, self.name, self.metadata["bar"]).generate()
        BubbleChart(self.df, self.title, self.name, self.metadata["bubble"]).generate()
