from base.heatmap_chart import HeatmapChart
from base.line_chart import LineChart
from base.bar_chart import BarChart
from base.bubble_chart import BubbleChart
from base.pie_chart import PieChart
from base.donut_chart import DonutChart
from base.stacked_bar_chart import StackedBarChart

class Datasets:
    def __init__(self, df, metadata, name="datasets", title="Uso de datasets públicos vs privados"):
        self.df = df
        self.metadata = metadata
        self.name = name
        self.title = title

    def generate_charts(self):
        HeatmapChart(self.df, self.title, self.name, self.metadata["heatmap"]).generate()
        LineChart(self.df, self.title, self.name, self.metadata["line"]).generate()
        BarChart(self.df, self.title, self.name, self.metadata["bar"]).generate()
        BubbleChart(self.df, self.title, self.name, self.metadata["bubble"]).generate()
        PieChart(self.df, self.title, self.name, self.metadata["pie"]).generate()
        DonutChart(self.df, self.title, self.name, self.metadata["donut"]).generate()
        StackedBarChart(self.df, self.title, self.name, self.metadata["stacked_bar"]).generate()
