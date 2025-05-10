import pandas as pd

def get_data():
    data = {
        2019: [3, 1, 1, 2, 0, 1, 3],
        2020: [4, 1, 1, 1, 1, 2, 2],
        2021: [4, 1, 0, 0, 1, 0, 4],
        2022: [3, 0, 0, 0, 0, 0, 6],
        2023: [1, 0, 1, 0, 0, 0, 15],
        2024: [3, 1, 0, 0, 0, 2, 16]
    }
    labels = [
        "SVM",
        "Random forest (RF)",
        "Multi-layer perceptron (MLP)",
        "AlexNet",
        "ResNet",
        "U-Net",
        "Arquitectura"
    ]
    return pd.DataFrame(data, index=labels)