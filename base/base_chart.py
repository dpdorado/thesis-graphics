from abc import ABC, abstractmethod
from datetime import datetime
import os
import matplotlib.pyplot as plt

class BaseChart(ABC):
    def __init__(self, df, title, filename):
        self.df = df
        self.title = title
        self.filename = filename
        self.date = datetime.now().strftime("%Y%m%d")

    @abstractmethod
    def generate(self):
        pass

    def save(self, fig, chart_type):
        folder = f"graphics/outputs/{self.filename}"
        os.makedirs(folder, exist_ok=True)
        path = f"{folder}/{chart_type}_{self.filename}_{self.date}.png"
        fig.tight_layout()
        fig.savefig(path)
        plt.close(fig)
        print(f"✅ Saved: {path}")