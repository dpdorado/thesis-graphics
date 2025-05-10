from base.bubble_chart import BubbleChart

class Publications:
    def __init__(self, df, metadata, name = 'publications', title = 'Publicaciones'):
        self.df = df
        self.metadata = metadata
        self.name = name
        self.title = title

    def generate_charts(self):
        BubbleChart(self.df, self.title, self.name, self.metadata["bubble"]).generate()
